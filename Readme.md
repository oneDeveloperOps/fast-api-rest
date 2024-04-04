INSTALLATION STEPS:

Clone repo then install deps:
1 -> sudo apt install python3-pip
2 -> pip install fastapi
3 -> pip install SQLAlchemy
4 -> pip install beautifulsoup4
5 -> pip install pymemcache

HOW TO CALL APIS:

open localhost:8000/docs to access swagger

1 -> pass authorization = xyz in headers kept it simple auth as for now

APIS:

localhost:8000/start-scraping/{no_of_pages}
description:
    1- no_of_pages is the number of pages you want to pass for scraping
    2- Api will return scrape id through with you can look for scraped products using the second API

/scraped-products/{scrape_id}
description:
    1- scrape_id is the number of pages you want to pass for scraping
    2- Api will return scrape id through with you can look for scraped products using the second API

TO check all data import product.db in DBeaver or any of your fav db viewer
Execute Select * from products to explore scraped data

If a product is already inserted during the session and price does not change then we check data in memcache to prevent insertion in sql

