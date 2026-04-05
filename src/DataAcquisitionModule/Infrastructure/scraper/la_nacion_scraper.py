from DataAcquisitionModule.Infrastructure.scraper.base_scraper import BaseScraper
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

class LaNacionScraper(BaseScraper):
    
    """Scraper específico para La Nación, extiende BaseScraper para manejar casos particulares de este sitio"""

    def extract_authors(self, article, soup=None):
        """
        Extrae una lista de autores del HTML de una nota de LA NACION.
        """
        soup = soup or BeautifulSoup(article.html, 'html.parser')
        authors = set()  

        # 1. Intentar desde JSON-LD 
        # Buscar por id o por tipo
        script = soup.find('script', id='Schema_NewsArticle')
        
        if script and script.string:
            try:
                data = json.loads(script.string)
                # Buscar en 'author' (puede ser dict o list)
                if 'author' in data:
                    author_data = data['author']
                    if isinstance(author_data, list):
                        for item in author_data:
                            if isinstance(item, dict) and 'name' in item:
                                authors.add(item['name'])
                    elif isinstance(author_data, dict) and 'name' in author_data:
                        authors.add(author_data['name'])
            except (json.JSONDecodeError, AttributeError, TypeError):
                pass

        if not authors:
            return article.authors

        return list(authors)
    
    def extract_date(self, article, soup=None):

        soup = soup or BeautifulSoup(article.html, 'html.parser')
       
        script = soup.find('script', id='Schema_NewsArticle')
        
        if script and script.string:
            try:
                data = json.loads(script.string)

                if 'datePublished' in data:
                    date_str = data.get("datePublished")

                    if date_str:
                        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))

            except (json.JSONDecodeError, AttributeError, TypeError):
                pass

        # Si hay algún error 
        return article.publish_date

    def extract_content(self, article, soup) -> str:
       
        soup = soup or BeautifulSoup(article.html, 'html.parser')
        paragraphs = soup.find_all(['p', 'h2']) 
        texts = []
        for elem in paragraphs:
            # Incluir solo párrafos con la clase 'com-paragraph'
            if elem.name == 'p' and 'com-paragraph' not in elem.get('class', []):
                continue
            # separator=' ' inserta espacios entre elementos inline
            text = elem.get_text(separator=' ', strip=True)
            # Normalizar espacios múltiples a uno solo
            text = re.sub(r'\s+', ' ', text)
            texts.append(text)
        return '\n\n'.join(texts)  