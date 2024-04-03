from pymemcache.client import base

class MemcachedService:
    def __init__(self, host = 'localhost', port = 11211):
        self.__client = base.Client((host, port))
    
    def setProductCache(self, product):
        self.__client.set(str(hash(product.product_title)), product.product_price.encode('ascii', 'ignore'))
        return True
    
    def getProductCache(self, productTitle):
        return self.__client.get(str(hash(productTitle)))
    