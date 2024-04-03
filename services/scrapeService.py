from .baseScrapper import BaseScrapper
from .retryService import Retry
import uuid

class ScrapeService():
    def __init__(self, page):
        self.__page = page

    def startScraping(self):
        # scraping on the basis of pages
        try:
            scrape_id = str(uuid.uuid4())
            for i in range(1, self.__page + 1):
                try:
                    # scraping for number of pages provided in api body
                    BaseScrapper(i, scrape_id).scrapeProductData()
                except:
                    # retrying here
                    SLEEP = 5
                    RETRY_COUNT = 3
                    Retry(BaseScrapper(i, scrape_id).scrapeProductData, SLEEP, RETRY_COUNT)
            return scrape_id
        except:
            raise Exception("Someting went wrong!") 

