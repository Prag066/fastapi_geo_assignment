from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Float
from database import Base

class AddressBook(Base):
    __tablename__ = "addressbook"
    id = Column(Integer, primary_key=True)
    Lat = Column(Float, default=0)
    Lon = Column(Float, default=0)
    Place = Column(String(700))
    ZipCode = Column(String(10)) 
    updated_date = Column(DateTime)