#!/usr/bin/env python3
"""Script interactivo para probar queries en Elasticsearch."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import asyncio
from elasticsearch import AsyncElasticsearch
from RetrievalModule.Infrastructure.elasticsearch_retriever import ElasticsearchRetriever
from RetrievalModule.Application.lmir_retriever import LMIRScoreFunction
from RetrievalModule.Infrastructure.elasticsearch_query_preprocesor import ElasticsearchQueryPreprocessor
from IndexModule.Config.settings import Settings
from collections import Counter
import math


async def main():
    # Función auxiliar para tokenizar contenido consistentemente
    async def tokenize_content(content: str, client: AsyncElasticsearch, index_name: str) -> list[str]:
        """Tokeniza contenido usando el mismo analizador que Elasticsearch."""
        if not content:
            return []
        
        response = await client.indices.analyze(
            index=index_name,
            body={
                "analyzer": "spanish_analyzer",
                "text": content
            }
        )
        return [token["token"] for token in response["tokens"]]

    settings = Settings()
    
    ES_HOST = os.getenv("ES_HOST", settings.elasticsearch_hosts[0] if settings.elasticsearch_hosts else "https://localhost:9200")
    ES_USER = os.getenv("ES_USER", settings.elasticsearch_username)
    ES_PASS = os.getenv("ES_PASS", settings.elasticsearch_password)
    INDEX_NAME = os.getenv("ES_INDEX", settings.index_name)
    
    print("=" * 60)
    print("   PROBADOR INTERACTIVO DE QUERIES - ELASTICSEARCH + LMIR")
    print("=" * 60)
    print(f"\n  Host: {ES_HOST}")
    print(f"  Índice: {INDEX_NAME}")
    
    es_config = {
        "hosts": [ES_HOST],
        "verify_certs": False,  # Desabilitar verificación para certificados auto-firmados
        "request_timeout": 30
    }
    if ES_USER and ES_PASS:
        es_config["basic_auth"] = (ES_USER, ES_PASS)
    
    client = AsyncElasticsearch(**es_config)
    retriever = ElasticsearchRetriever(client, INDEX_NAME)
    preprocessor = ElasticsearchQueryPreprocessor(client, INDEX_NAME)
    
    try:
        info = await client.info()
        print(f"\n✅ Conectado a Elasticsearch {info['version']['number']}")
    except Exception as e:
        print(f"\n❌ Error de conexión: {e}")
        print("\n Asegúrate de que Elasticsearch esté corriendo.")
        print(" En Docker: docker run -p 9200:9200 -e 'discovery.type=single-node' elasticsearch:8.11.0")
        return
    
    count = await retriever.count()
    print(f"📄 Documentos en el índice: {count}")
    
    if count == 0:
        print("\n⚠️  No hay documentos en el índice")
        print("   Asegúrate de haber ejecutado el pipeline de indexación primero.")
        return
    
    print("\n" + "=" * 60)
    print("   MODO INTERACTIVO")
    print("=" * 60)
    print("   Escribe tu query y presiona Enter")
    print("   Escribe 'salir' para terminar")
    print("   Escribe 'stats' para ver estadísticas del modelo")
    print("=" * 60 + "\n")
    
    # Variables para acumular estadísticas
    all_doc_term_freqs = {}
    all_doc_lengths = {}
    all_collection_freq = Counter()
    candidates_cache = None
    scorer_cache = None
    query_tokens_cache = None
    
    while True:
        try:
            query = input("Query: ").strip()
        except EOFError:
            break
        
        if query.lower() in ['salir', 'exit', 'quit']:
            break
        
        if query.lower() == 'stats':
            if scorer_cache:
                stats = scorer_cache.get_statistics()
                print("\n  📊 Estadísticas del modelo LMIR:")
                print(f"     Documentos: {stats['num_documents']}")
                print(f"     Tamaño vocabulario: {stats['vocabulary_size']}")
                print(f"     Tokens totales: {stats['total_collection_tokens']}")
                print(f"     Longitud promedio docs: {stats['average_document_length']:.1f}")
                print(f"     μ (mu): {stats['mu']}")
            else:
                print("\n  No hay datos cargados. Haz una query primero.")
            continue
        
        if not query:
            continue
        
        # Usar el mismo preprocesamiento que el sistema real
        query_tokens = await preprocessor.preprocess(query)
        print(f"\n  🔤 Tokens: {query_tokens}")
        
        # Aumentar candidatos para mejor recall
        candidates = await retriever.get_candidate_documents(query_tokens, top_n=200)
        print(f"  🔍 Candidatos encontrados: {len(candidates)}")
        
        if not candidates:
            print("  ❌ Sin resultados\n")
            continue
        
        doc_term_freqs = {}
        doc_lengths = {}
        collection_freq = Counter()
        
        for doc in candidates:
            # Usar el mismo tokenizado que Elasticsearch
            tokens = await tokenize_content(doc.content, client, INDEX_NAME)
            doc_lengths[doc.doc_id] = len(tokens)
            tf = Counter(tokens)
            doc_term_freqs[doc.doc_id] = tf
            collection_freq.update(tokens)
        
        # Actualizar cache
        all_doc_term_freqs.update(doc_term_freqs)
        all_doc_lengths.update(doc_lengths)
        all_collection_freq.update(collection_freq)
        candidates_cache = candidates
        query_tokens_cache = query_tokens
        
        # Usar mu=100 para mayor discriminación entre documentos
        scorer = LMIRScoreFunction(mu=100.0)
        scorer.load_statistics(doc_term_freqs, doc_lengths, collection_freq)
        scorer_cache = scorer
        
        scores = []
        for doc in candidates:
            score = scorer.compute_log_p_query_given_doc(query_tokens, doc.doc_id)
            scores.append((score, doc))
        
        scores.sort(reverse=True, key=lambda x: x[0])
        
        # Normalizar scores a 0-100 para mejor legibilidad
        if scores:
            max_score = scores[0][0]
            min_score = scores[-1][0]
            score_range = max_score - min_score if max_score != min_score else 1
        
        print(f"\n  📋 Top {min(5, len(scores))} resultados:")
        print("  " + "-" * 55)
        
        for i, (score, doc) in enumerate(scores, 1):
            # Normalizar score a 0-100
            norm_score = 100 * (score - min_score) / score_range if score_range > 0 else 0
            print(f"\n  {i}. Score: {norm_score:.1f}/100 (raw: {score:.4f})")
            print(f"     📌 {doc.title[:70]}")
            print(f"     🔗 {doc.url[:60]}")            
            # Mostrar detalles del cálculo para el primer documento
            
            preview = doc.content.replace('\n', ' ')
            print(f"     📄 {preview}")
        
        print("\n" + "  " + "-" * 55 + "\n")
    
    await client.close()
    print("\n👋 ¡Adiós!")


if __name__ == "__main__":
    asyncio.run(main())
