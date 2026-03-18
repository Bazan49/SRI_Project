import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Asegura que el paquete `src/` esté en el path cuando se ejecuta desde la raíz
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from DI.continer import SearchContainer
from DataAcquisitionModule.Scraper.scrapedDocument import ScrapedDocument

container = SearchContainer()
container.wire(modules=[__name__])

async def main():
    index_service = container.index_service()
    
    # Tus documentos scraped
    scraped_docs = [
    ScrapedDocument(
        source="bbc",
        url="https://example.com/noticia-1",
        url_normalized="https://example.com/noticia-1",
        title="La economía global muestra signos de recuperación",
        content="La economía mundial está mostrando señales de recuperación tras la crisis reciente. Expertos destacan el crecimiento en varios sectores clave.",
        authors=["Juan Pérez"],
        date=datetime(2024, 3, 10),
        indexed=False,
        embeddings_generated=False
    )
]
    
    await index_service.index_scraped_documents(scraped_docs)
    print("✅ Indexación completada")

if __name__ == "__main__":
    asyncio.run(main())
