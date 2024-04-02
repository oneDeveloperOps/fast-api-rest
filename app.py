from fastapi import FastAPI
from models import product
from database.connection import engine

app = FastAPI()

product.Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"index": "product scrapper api"}

@app.get("/scraped-products/{scrape_id}")
def fetchScrapedProducts(scrape_id: int):
    return { 'scrape_id': scrape_id }