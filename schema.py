'''
This is to define the schema use for intracting the database
'''
from datetime import datetime
from pydantic import BaseModel
from typing import List

class AddressBookBase(BaseModel):
    '''
    Base Model
    '''
    Lat: float
    Lon: float
    Place: str
    ZipCode: int
    updated_date = datetime

class AddressCreate(AddressBookBase):
    '''
    for create Address from base model
    '''
    pass

class AddressBook(AddressBookBase):
    '''
    Orm config for auto update Address Id 
    '''
    id: int
    class Config:
        orm_mode = True

class AddressInfo(AddressBook):
    '''
    for fetch the address information from AddressBook
    '''
    pass