from fastapi import FastAPI, Header
from models import product
from database.connection import engine
from services import scrapeService

#Could be replaced with JWT for more better authentication
AUTH_STRING='xyz'

app = FastAPI()

# TABLE SYNC
product.Base.metadata.create_all(bind=engine)

def matchAuthString(auth):
    print(auth)
    if (AUTH_STRING != auth):
        return False
    return True

#Using main app.py as controller and router for assignment purpoes only!
@app.get("/start-scraping/{no_of_pages}")
def startScraping(authorization: str = Header(None), no_of_pages: int = 1):
    print(authorization)
    isAuth = matchAuthString(authorization)

    if (isAuth == False):
        return { "msg": "Unauthorized" }

    scrapeId = scrapeService.ScrapeService(no_of_pages).startScraping()
    return { "msg": "To get data of scraped products please use scraped products api with given scrapeId", 'scrape_id': scrapeId }

@app.get("/scraped-products/{scrape_id}")
def fetchScrapedProducts(authorization: str = Header(None), scrape_id: str = None):

    isAuth = matchAuthString(authorization)

    if (isAuth == False): 
        return { "msg": "Unauthorized" }

    print(scrape_id)
    scrapedData = scrapeService.ScrapeService(0).fetchScrapeData(scrape_id)
    return { 'data': scrapedData }