

from datetime import datetime
from pydantic import BaseModel
from typing import List

class AddressBookBase(BaseModel):
    Lat: int
    Lon: int
    Place: str
    ZipCode: str
    updated_date = datetime

class AddressCreate(AddressBookBase):
    pass

class AddressBook(AddressBookBase):
    id: int
    class Config:
        orm_mode = True

class AddressInfo(AddressBook):
    pass