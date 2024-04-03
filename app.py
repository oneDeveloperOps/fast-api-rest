from fastapi import FastAPI
from models import product
from database.connection import engine
from services import scrapeService

app = FastAPI()

product.Base.metadata.create_all(bind=engine)

#Using main app.py as controller and router for assignment purpoes only!
@app.get("/start-scraping/{no_of_pages}")
def startScraping(no_of_pages: int):
    scrapeId = scrapeService.ScrapeService(no_of_pages).startScraping()
    return { "msg": "To get data of scraped products please use scraped products api with given scrapeId", 'scrape_id': scrapeId }

@app.get("/scraped-products/{scrape_id}")
def fetchScrapedProducts(scrape_id: str):
    print(scrape_id)
    scrapedData = scrapeService.ScrapeService(0).fetchScrapeData(scrape_id)
    return { 'data': scrapedData }