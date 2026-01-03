from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///database/etf_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # needs to false to be used with fastAPI
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Constituent(Base):
    """
    Stores uploaded ETF constituent data
    """
    __tablename__ = "constituents"
    
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True)
    weight = Column(Float)
class Price(Base):
    """
    Stores historical price data from prices.csv
    """
    __tablename__ = "prices"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    constituent = Column(String, index=True)
    price = Column(Float)

# Create tables
Base.metadata.create_all(bind=engine)


"""
Sources used:
https://gerrysabar.medium.com/fastapi-simple-crud-with-mysql-sqlalchemy-e60dd04a5c7e
https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e
"""

