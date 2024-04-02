import requests
from bs4 import BeautifulSoup
import sys

sys.path.append('../fastapi')

from constants import scrapeConstants
from models import product
from database import connection
from retryService import Retry

class BaseScrapper(object):
    def __init__(self, page: int, scrapeId: int) -> None:
        self.__page = page
        self.__scrapeId = scrapeId

    def __fetchPageData(self):
        try:
            self.__headers = { 'accept': 'text/html' }
            self.__url = scrapeConstants.BASE_URL + str(self.__page)
            self.__res = requests.get(self.__url, headers=self.__headers)
        except requests.exceptions.RequestException as e:
            raise e
    
    def __isAlreadyInCache(self, productId: int):
        pass

    def _insertProductInDB(self, title: str, image: str, price: str):
        

    def scrapeProductData(self):
        # feching data and extracting the same
        self.__fetchPageData()
        self.__decodedContent = self.__res.content.decode('utf-8')
        self.__soup = BeautifulSoup(self.__decodedContent, 'html.parser')
        self.__soupLiProducts = self.__soup.find_all('li', 'type-product')
        for productLiSoup in self.__soupLiProducts:
            image = productLiSoup.findAll('img', attrs={'class': 'size-woocommerce_thumbnail'})[0].attrs['data-lazy-src']
            title = productLiSoup.findAll('h2', attrs={'class': 'woo-loop-product__title'})[0].find('a').text
            price = productLiSoup.findAll('span', attrs={'class': 'woocommerce-Price-amount'})[0].find('bdi').text
            self.__insertProductInDB(title, image, price)