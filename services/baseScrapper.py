import requests
from bs4 import BeautifulSoup
import sys

sys.path.append('../fastapi')

from constants import scrapeConstants
from retryService import Retry

class BaseScrapper(object):
    def __init__(self, page):
        self.__page = page

    def __fetchPageData(self):
        try:
            headers = { 'accept': 'text/html' }
            url = scrapeConstants.BASE_URL + str(self.__page)
            self.__res = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            raise e
    
    def __isAlreadyInCache(self, productId):
        pass

    def scrapeProductData(self):
        html = self.__fetchPageData()
        decodedContent = self.__res.content.decode('utf-8')
        soup = BeautifulSoup(decodedContent, 'html.parser')
        soupLiProducts = soup.find_all('li', 'type-product')
        for productLiSoup in soupLiProducts:
            image = productLiSoup.findAll('img', attrs={'class': 'size-woocommerce_thumbnail'})[0].attrs['data-lazy-src']
            title = productLiSoup.findAll('h2', attrs={'class': 'woo-loop-product__title'})[0].find('a').text
            

BaseScrapper(1).scrapeProductData()