# RetrievalModule - Arquitectura y flujo

## 🧠 Panorama general
`RetrievalModule` es el módulo responsable de recuperar documentos relevantes para una query del usuario. Está diseñado con capas claras (Domain + Infrastructure + Application) y usa ElasticSearch + LMIR (Language Model for Information Retrieval) por ahora.

El flujo principal es:
1. Se recibe query del usuario.
2. Se preprocesa con el mismo analizador Elasticsearch (`spanish_analyzer`).
3. Se consultan candidatos en Elasticsearch (match bool should). 
4. Se calculan scores con el modelo probabilístico LMIR (Dirichlet).
5. Se ordenan candidatos y se devuelven resultados con snippet.

---

## 🧩 Componentes (capas) de RetrievalModule

### 1) Domain (lógica + interfaces)

- `QueryPreprocessor` (`RetrievalModule/Domain/query_preprocessor.py`):
  - Interfaz abstracta para tokenizar/preprocesar query.
  - Método async: `preprocess(text: str) -> List[str]`.

- `RetrieverRepository` (`RetrievalModule/Domain/retriever_repository.py`):
  - Interfaz abstracta para obtener candidatos de búsqueda.
  - Método async: `get_candidate_documents(query_terms, top_n)`.

- `StatsRepository` (`RetrievalModule/Domain/stats_repository.py`):
  - Interfaz abstracta para cargar estadísticas necesarias para LMIR.
  - Métodos async: `get_doc_term_freqs()`, `get_doc_lengths()`, `get_collection_freq()`.

- `RetrievalResult` (`RetrievalModule/Domain/retrieval_result.py`):
  - DTO de resultado final con fields: url, title, content, score, source, snippet.

---

### 2) Infrastructure (implementaciones reales)

- `ElasticsearchRetriever` (`RetrievalModule/Infrastructure/elasticsearch_retriever.py`):
  - Implementa `RetrieverRepository`.
  - `get_candidate_documents` usa query bool/should sobre campo `content`.
  - `get_all_documents`, `count`.

- `ElasticsearchQueryPreprocessor` (`RetrievalModule/Infrastructure/elasticsearch_query_preprocesor.py`):
  - Implementa `QueryPreprocessor`.
  - Usa `client.indices.analyze` con `spanish_analyzer` para obtener tokens concordantes con indexación.

- `ElasticsearchStatsRepository` (`RetrievalModule/Infrastructure/elasticsearch_stats_repository.py`):
  - Implementa `StatsRepository`.
  - Recorre todos los documentos con scroll, tokeniza contenido con mismo analizador y calcula:
    - doc_term_freqs
    - doc_lengths
    - collection_freq

---

### 3) Application (orquestación de recuperación)

- `LMIRScoreFunction` (`RetrievalModule/Application/lmir_retriever.py`):
  - Modelo de puntuación de query-likelihood con suavizado Dirichlet.
  - Operaciones clave:
    - `load_statistics(doc_term_freqs, doc_lengths, collection_freq)`
    - `compute_p_w_given_d(term, doc_id)`
    - `compute_log_p_query_given_doc(query_tokens, doc_id)`
    - `get_statistics()`

- `RetrievalAppService` (`RetrievalModule/Application/retrieval_service.py`):
  - Orquesta funcionalidad principal de búsqueda.
  - Flujo:
    1. `await _ensure_stats_loaded()` (carga las estadísticas la primera vez)
    2. `query_tokens = await preprocessor.preprocess(query)`.
    3. `candidates = await repository.get_candidate_documents(query_tokens, top_candidates)`.
    4. Para cada candidato: `log_prob = scorer.compute_log_p_query_given_doc(...)`.
    5. Sort descendente por score.
    6. Build response con `RetrievalResult.to_dict()` y snippet.

- `get_stats()` retorna estadísticas LMIR.

---

## 🔍 Reglas importantes y detalles de implementación

- **Preprocesamiento y stemming**: se usa `ElasticsearchQueryPreprocessor` para evitar mismatch tokenización. Ej: "economia" → "economi".

- **Escorings negativos**:
  - `LMIRScoreFunction` devuelve log-probabilidad; se normaliza en `RetrievalAppService` a 0-100 para visualización.
  - `mu` es el hiperparámetro crítico (por defecto 100 ).

- **Candidatos**:
  - Se seleccionan desde Elasticsearch con `top_n` (200 por defecto).
  - LMIR ordena entre esos candidatos, por lo que la calidad de initial candidate set es clave.


## 🧪 Cómo probar rápidamente

1. Coloca ElasticSearch corriendo en URL de `Settings`.
2. Ejecuta `python test_elasticsearch_retriever.py`.
3. Ingresa query (por ejemplo "economia", "latin").
4. Revisa `stats` con `stats`.
5. Verifica que la salida muestre tokenización y scores.

---
