# Módulo de Embeddings: Flujo Completo, Configuración, Ventajas y Desventajas

## Introducción

El **Módulo de Embeddings** es un componente clave del sistema de búsqueda e indexación de documentos. Utiliza técnicas de procesamiento de lenguaje natural (NLP) para convertir texto en representaciones vectoriales (embeddings), permitiendo búsquedas semánticas eficientes basadas en similitud de significado en lugar de coincidencias exactas de palabras.

Este módulo integra varios componentes: chunking de documentos, generación de embeddings, almacenamiento vectorial y búsqueda. Está diseñado para manejar documentos largos dividiéndolos en fragmentos manejables, codificándolos en vectores de alta dimensión y almacenándolos en una base de datos vectorial para consultas rápidas.

## Flujo Completo

El flujo de trabajo del módulo sigue una arquitectura limpia (Clean Architecture) con capas de dominio, infraestructura y casos de uso. Aquí va el proceso paso a paso:

### 1. **Adquisición de Documentos**
   - Los documentos se obtienen desde fuentes externas (ej. scrapers de noticias como Cubadebate o TeleMundo).
   - Cada documento incluye: título, contenido, autor, fecha, URL, etc.


### 2. **Chunking (División en Fragmentos)**
   - **Propósito**: Dividir documentos largos en chunks más pequeños para mejorar la precisión de los embeddings.
   - **Implementación**: Usa `NewspaperChunker` que divide por párrafos y sub-párrafos si son muy largos.
   - **Metadata**: Cada chunk incluye metadata como ID del documento, fuente, URL, título, fecha de publicación, tipo de chunk, etc.
   - **Salida**: Lista de objetos `Chunk` con texto y metadata.

### 3. **Generación de Embeddings**
   - **Modelo**: Utiliza `SentenceTransformer` con el modelo `intfloat/multilingual-e5-large` (768 dimensiones).
   - **Proceso**: Convierte el texto de cada chunk en un vector numérico de 768 dimensiones.
   - **Normalización**: Los embeddings están normalizados (L2), lo que facilita cálculos de similitud coseno.
   - **Salida**: Array de NumPy con embeddings para todos los chunks.

### 4. **Almacenamiento Vectorial**
   - **Base de Datos**: ChromaDB (vectorial persistente).
   - **Operaciones**:
     - `add`: Almacena IDs, embeddings, documentos y metadata.
     - `search`: Realiza búsquedas por similitud usando distancia coseno.
     - `update` / `delete`: Para modificaciones.
   - **Persistencia**: Los datos se guardan en `./chroma_db` con SQLite para persistencia.

### 5. **Indexación**
   - **Caso de Uso**: `VectorIndexer` coordina el flujo completo.
   - **Proceso**: Toma una lista de `ScrapedDocument`, los chunkiza, genera embeddings y los almacena.
   - **Salida**: Número total de chunks indexados.

### 6. **Búsqueda**
   - **Caso de Uso**: `VectorSearcher` maneja consultas.
   - **Proceso**: Codifica la query en embedding, busca los k vecinos más cercanos en el espacio vectorial.
   - **Salida**: Diccionario con documentos, metadata, distancias e IDs relevantes.

### 7. **Integración con API (Opcional)**
   - Exposición vía FastAPI para endpoints de búsqueda.
   - Documentación automática con Swagger.

## Configuración

### Dependencias
- **Python**: 3.8+
- **Librerías**:
  - `sentence-transformers`: Para embeddings.
  - `chromadb`: Para almacenamiento vectorial.
  - `numpy`: Para arrays.
  - `dependency-injector`: Para inyección de dependencias.
- **Instalación**: `pip install sentence-transformers chromadb numpy dependency-injector`

### Configuración del Contenedor
Usa `EmbeddingsContainer` para inyección de dependencias:
- **Chunker**: `NewspaperChunker` con `max_tokens=400`, `overlap=50`.
- **Embedder**: `SentenceTransformerEmbedder` con modelo `intfloat/multilingual-e5-large`.
- **Vector Store**: `ChromaVectorStore` con colección `"test_documents"` y path `./chroma_db`.

### Variables de Entorno
- `HF_TOKEN`: Para acceso a Hugging Face (opcional, reduce rate limits).

### Ejecución
- **Indexación**: Ejecuta `test_embeddings.py` para probar el flujo completo.
- **Búsqueda**: Usa `VectorSearcher` con queries en español o inglés.

## Ventajas

- **Búsqueda Semántica**: Encuentra contenido relevante por significado, no solo palabras clave.
- **Multilingüe**: Soporte para español, inglés y otros idiomas con e5-large.
- **Escalabilidad**: ChromaDB maneja miles de documentos eficientemente.
- **Modularidad**: Arquitectura limpia permite reemplazar componentes (ej. cambiar a FAISS).
- **Rendimiento**: Embeddings precomputados permiten búsquedas en milisegundos.
- **Persistencia**: Datos guardados en disco, sobreviven reinicios.
- **Facilidad de Uso**: APIs simples para indexar y buscar.

## Desventajas

- **Requisitos de Hardware**: Modelo grande (e5-large) requiere GPU para velocidad; en CPU es lento.
- **Consumo de Memoria**: Embeddings de 768 dims por chunk consumen RAM/disco.
- **Dependencia de Modelo**: Cambiar modelo requiere re-indexar todo.
- **Limitaciones de Chunking**: División por párrafos puede no capturar contexto largo.
- **Latencia Inicial**: Primera carga del modelo toma tiempo.
- **Complejidad de Configuración**: Requiere ajuste de parámetros (max_tokens, k, etc.).
- **Dependencias Externas**: Hugging Face puede tener rate limits sin token.

## Ejemplos de Uso

### Indexación
```python
container = EmbeddingsContainer()
indexer = container.vector_indexer()
total = indexer.index(documents)  # Lista de ScrapedDocument
print(f"Indexados {total} chunks")
```

### Búsqueda
```python
searcher = container.vector_searcher()
results = searcher.search("inteligencia artificial", k=5)
for doc, meta, dist in zip(results['documents'], results['metadatas'], results['distances']):
    print(f"{meta['title']}: {dist:.4f}")
```

