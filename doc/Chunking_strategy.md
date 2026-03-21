# Estrategia de Chunking para Periodismo Digital

## 📋 Resumen Ejecutivo

La estrategia de chunking actual implementada en `NewspaperChunker` está optimizada específicamente para artículos noticiosos, respetando la estructura editorial natural de las noticias mientras mantiene la coherencia semántica necesaria para búsquedas efectivas.

## 🎯 Estrategia Actual: NewspaperChunker

### Arquitectura General

```python
class NewspaperChunker(Chunker):
    def __init__(self, max_tokens: int = 400, overlap: int = 50):
        self.max_tokens = max_tokens
        self.overlap = overlap
```

### Algoritmo de Chunking

#### 1. **División por Párrafos Naturales**
- **Separador**: Doble salto de línea (`\n\s*\n`)
- **Lógica**: Divide el texto en párrafos editoriales naturales
- **Ventaja**: Respeta la estructura periodística (lead, cuerpo, conclusión)

#### 2. **Manejo de Párrafos Largos**
- **Condición**: Si un párrafo excede `max_tokens`
- **Estrategia**: Subdivisión con overlap deslizante
- **Overlap**: `overlap` tokens de contexto entre subchunks

#### 3. **Estimación de Tokens**
- **Método**: `len(text) // 4` (aproximación simple)
- **Ratio**: 1 token ≈ 4 caracteres
- **Limitación**: No usa modelos de tokenización reales

### Parámetros de Configuración

| Parámetro | Valor por Defecto | Rango Recomendado | Descripción |
|-----------|-------------------|-------------------|-------------|
| `max_tokens` | 400 | 300-500 | Tamaño máximo de tokens por chunk |
| `overlap` | 50 | 30-80 | Tokens de superposición entre chunks |

### Estructura de Metadatos

```python
@dataclass
class ChunkMetadata:
    doc_id: str                    # ID único del documento
    source: str                    # Fuente (ej: "clarin", "bbc")
    url: str                       # URL completa del artículo
    title: str                     # Título de la noticia
    publication_date: datetime     # Fecha de publicación
    chunk_type: str = "paragraph"  # Tipo: "paragraph" o "paragraph_subchunk"
    chunk_number: int = 0          # Número secuencial del chunk
    estimated_tokens: int = 0      # Tokens estimados en el chunk
```

## ✅ Ventajas de la Estrategia Actual

### 1. **Respeta Estructura Editorial**
- Mantiene párrafos como unidades semánticas naturales
- Preserva la narrativa periodística (lead → desarrollo → conclusión)

### 2. **Metadatos Enriquecidos**
- Información completa del documento en cada chunk
- Facilita búsquedas facetadas por fuente, fecha, tipo
- Soporte para trazabilidad completa

### 3. **Flexibilidad Configurable**
- Parámetros ajustables según necesidades
- Manejo inteligente de párrafos largos vs. cortos
- Overlap configurable para mantener contexto

### 4. **Eficiencia Computacional**
- Algoritmo simple y rápido
- Sin dependencias de modelos de ML complejos
- Estimación de tokens lightweight

## ⚠️ Limitaciones y Áreas de Mejora

### 1. **Estimación de Tokens Simplista**
- No usa tokenizadores reales (GPT, BERT, etc.)
- Puede subestimar tokens en textos complejos
- **Solución**: Integrar `tiktoken` o similar

### 2. **Sin Overlap Entre Párrafos**
- Chunks de párrafos diferentes no comparten contexto
- Puede perder continuidad narrativa
- **Solución**: Implementar ventana deslizante global

### 3. **No Prioriza Contenido Crítico**
- Trata todos los párrafos igual
- No destaca título, lead, o conclusiones
- **Solución**: Ponderación por importancia editorial

### 4. **Falta de Análisis Semántico**
- No entiende significado del contenido
- No agrupa temas relacionados
- **Solución**: Integrar embeddings semánticos

## 🔄 Evolución de Estrategias

### Fase 1: NewspaperChunker (Actual)
- ✅ Funcional y probado
- ✅ Respeta estructura periodística
- ✅ Metadatos completos

### Fase 2: SemanticNewsChunker (Próxima)
- 🔄 Análisis semántico avanzado
- 🔄 Priorización de contenido crítico
- 🔄 Overlap inteligente

### Fase 3: HybridChunker (Futuro)
- 📋 Combinación de múltiples estrategias
- 📋 Adaptación automática por tipo de contenido
- 📋 Optimización por métricas de búsqueda

## 📈 Métricas de Rendimiento

### Configuración Actual (max_tokens=100, overlap=10)
- **Chunks generados**: 3
- **Tokens promedio por chunk**: ~30
- **Tiempo de procesamiento**: < 1ms
- **Memoria utilizada**: Mínima

### Recomendaciones de Producción
- **max_tokens**: 400 (equilibra contexto vs. precisión)
- **overlap**: 50 (20-25% del chunk size)
- **Monitoreo**: Tokens reales vs. estimados

## 🛠️ Integración con el Sistema

### Dependencias del Chunking
```python
# En el flujo de indexación
from .Document_Chunking.a_chunker import NewspaperChunker

chunker = NewspaperChunker(max_tokens=400, overlap=50)
chunks = chunker.chunk(text, metadata=doc_metadata)

# Cada chunk se indexa con sus metadatos
for chunk in chunks:
    await index_service.index_chunk(chunk)
```

### Compatibilidad con Embeddings
- ✅ Funciona con cualquier modelo de embeddings
- ✅ Chunks optimizados para contexto de 512-1024 tokens
- ✅ Metadatos preservan información de trazabilidad

## 📚 Referencias y Mejores Prácticas

### Fuentes Consultadas
- [LangChain Chunking Strategies](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [LlamaIndex Node Parsers](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/)
- [Semantic Chunking Research](https://arxiv.org/abs/2309.08553)

### Patrones Recomendados
1. **Test A/B**: Comparar estrategias en métricas de búsqueda
2. **Monitoreo**: Tokens reales vs. estimados
3. **Feedback Loop**: Ajustar parámetros basado en resultados
4. **Versionado**: Mantener versiones de estrategias para reproducibilidad

---

**Última actualización**: Marzo 2026
**Versión**: 1.0
**Autor**: Sistema de Recuperación de Información