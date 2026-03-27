from DataAcquisitionModule.Infrastructure.network.fetcher import Fetcher

class ProcessURL:

    def __init__(self, scraper):
        self.scraper = scraper

    def execute(self, url, html=None):

        try:
            
            if html is None:
                html = Fetcher.fetch(url)

            return self.scraper.extract(url, html)

        except Exception as e:
            print(f"Error procesando {url}: {e}")
            return None