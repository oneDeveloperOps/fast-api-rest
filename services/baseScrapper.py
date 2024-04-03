import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('../fast-api-rest')
from models import product
from database import connection
from retryService import Retry
from sqlalchemy import text

class BaseScrapper(object):
    def __init__(self, page: int, scrapeId: int) -> None:
        self.__page = page
        self.__scrapeId = scrapeId
        self.__db = connection.getConnection()

    def __fetchPageData(self):
        try:
            self.__headers = { 'accept': 'text/html' }
            self.__url = "https://dentalstall.com/shop/page/" + str(self.__page)
            self.__res = requests.get(self.__url, headers=self.__headers)
        except requests.exceptions.RequestException as e:
            raise e
    
    def __isInsertableProduct(self, productId: int):
        pass

    def __insertProductInDB(self, title: str, image: str, price: str):
        
        newProduct = product.Product(scrape_id = self.__scrapeId, product_title = title, product_price = price, path_to_image = image)
        
        trans = self.__db.begin()
        
        self.__db.execute(text('INSERT INTO products (scrape_id, product_title, product_price, path_to_image) VALUES (:scrape_id, :title, :price, :image)'), {
            "title": newProduct.product_title,
            "price": newProduct.product_price,
            "scrape_id": newProduct.scrape_id,
            "image": newProduct.path_to_image,
        })
        
        trans.commit()

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
        
BaseScrapper(1,1).scrapeProductData()