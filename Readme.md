INSTALLATION STEPS:

Clone repo then install deps:
1 -> sudo apt install python3-pip
2 -> pip install fastapi
3 -> pip install SQLAlchemy
4 -> pip install beautifulsoup4
5 -> pip install pymemcache
6 -> sudo apt install memcached -> sudo systemctl start memcached -> sudo systemctl status memcached
7 -> sudo apt install uvicorn

START server: 

HOW TO CALL APIS:

open localhost:8000/docs to access swagger copy curl and import it in postman

1 -> pass authorization = xyz in headers kept it simple auth as for now

APIS:

localhost:8000/start-scraping/{no_of_pages}
description:
    1- no_of_pages is the number of pages you want to pass for scraping
    2- Api will return scrape id through with you can look for scraped products using the second API

SAMPLE CURL: 

curl -X 'GET' \
  'http://localhost:8000/start-scraping/1' \
  -H 'authorization: xyz'


/scraped-products/{scrape_id}
description:
    1- scrape_id is the number of pages you want to pass for scraping
    2- Api will return scrape id through with you can look for scraped products using the second API

SAMPLE CURL:

curl -X 'GET' \
  'http://localhost:8000/scraped-products/1' \
  -H 'authorization: xyz'



TO check all data import product.db in DBeaver or any of your fav db viewer
Execute Select * from products to explore scraped data

If a product is already inserted during the session and price does not change then we check data in memcache to prevent insertion in sql

