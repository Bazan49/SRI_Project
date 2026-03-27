from urllib.parse import urlparse
from DataAcquisitionModule.Infrastructure.scraper.cubadebate_scraper import CubadebateScraper
from DataAcquisitionModule.Infrastructure.scraper.base_scraper import BaseScraper
from DataAcquisitionModule.Infrastructure.scraper.telemundo_scraper import TeleMundoScraper

class ScraperFactory:

    @staticmethod
    def get_scraper(url):
        # Extraer el dominio
        source = urlparse(url).netloc.lower()  # ej: 'www.cubadebate.cu'

        # Diccionario de mapping source → scraper
        scrapers = {
            "cubadebate.cu": CubadebateScraper,
            "www.cubadebate.cu": CubadebateScraper,  
            "telemundo.com": TeleMundoScraper,
            "www.telemundo.com": TeleMundoScraper
        }

        # Devolver scraper adecuado o BaseScraper por defecto
        return scrapers.get(source, BaseScraper)()