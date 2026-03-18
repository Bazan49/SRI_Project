from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from DataAcquisitionModule.Scraper.scrapedDocument import ScrapedDocument

@dataclass
class SearchDocument:
    """Documento limpio para indexación (sin estado interno del pipeline)"""
    source: str
    url: str
    title: str
    content: str
    authors: Optional[List[str]]
    date: datetime

