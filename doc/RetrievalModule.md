## Modelo de recuperación: Language Model con suavizado Dirichlet

El módulo recuperador implementa un **modelo probabilístico de lenguaje (Language Model for Information Retrieval)** basado en la aproximación *query likelihood*. La puntuación de un documento \(D\) para una consulta \(Q\) se calcula como:

\[
P(Q|D) = \prod_{w \in Q} P(w|D)
\]

donde \(P(w|D)\) se estima mediante suavizado de Dirichlet:

\[
P(w|D) = \frac{\text{tf}(w,D) + \mu \cdot P(w|C)}{|D| + \mu}
\]

siendo \(\text{tf}(w,D)\) la frecuencia del término en el documento, \(|D|\) la longitud del documento, \(P(w|C)\) la probabilidad del término en toda la colección y \(\mu\) el parámetro de suavizado.

**Referencias bibliográficas:**

- **Ponte, J. M., & Croft, W. B. (1998).** *A language modeling approach to information retrieval.* In Proceedings of the 21st annual international ACM SIGIR conference on Research and development in information retrieval (pp. 275–281). ACM. [http://sigir.hosting.acm.org/wp-content/uploads/2017/06/p202.pdf](http://sigir.hosting.acm.org/wp-content/uploads/2017/06/p202.pdf)  
  (Definición fundamental del modelo de lenguaje aplicado a recuperación de información.)

- **Zhai, C., & Lafferty, J. (2001).** *A study of smoothing methods for language models applied to ad hoc information retrieval.* In Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval (pp. 334–342). ACM. [https://sigir.org/wp-content/uploads/2017/06/p268.pdf](https://sigir.org/wp-content/uploads/2017/06/p268.pdf)  
  (Justificación del suavizado de Dirichlet y su efecto en el rendimiento.)

---
# Arquitectura y flujo

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
