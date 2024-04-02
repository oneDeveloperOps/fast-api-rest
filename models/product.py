from database.connection import Base
from sqlalchemy import Integer, String, Column

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    scrape_id = Column(Integer)
    product_title = Column(String)
    product_price = Column(Integer)
    path_to_image = Column(String)