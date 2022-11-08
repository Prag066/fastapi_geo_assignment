from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from database import Base

class AddressBook(Base):
    __tablename__ = "addressbook"
    id = Column(Integer, primary_key=True)
    Lat = Column(Integer, default=0)
    Lon = Column(Integer, default=0)
    Place = Column(String(700))
    ZipCode = Column(String(10)) 
    updated_date = Column(DateTime)