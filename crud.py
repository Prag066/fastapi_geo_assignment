from datetime import datetime
from sqlalchemy.orm import Session
from model import Base, AddressBook
import schema,re
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="crudapitest")
def create_address(db: Session, address: schema.AddressCreate):
    # obj = AddressBook(**address.dict())
    location = geolocator.geocode(address.Place)
    data = location.raw
    loc_data = data['display_name'].split()
    # postal_code = re.search(r'.*(\d{5}(\-\d{4})?)$', data['display_name'])
    # print("postal_code",postal_code)
    address.Lat = data['lat']
    address.Lon = data['lon']
    # address.ZipCode = address.ZipCode if  address.ZipCode is not None else loc_data[-2]
    obj = AddressBook(**address.dict())
    db.add(obj)
    db.commit()
    return obj

def get_all_address(db: Session):
    return db.query(AddressBook).all()

def get_address(db: Session, aid):
    return db.query(AddressBook).filter(AddressBook.id == aid).first()

def get_address_by_location(db: Session, zipcode):
    return db.query(AddressBook).filter(AddressBook.ZipCode == zipcode).first()

def update_address(db: Session, aid, address: schema.AddressCreate):
    obj = db.query(AddressBook).filter(AddressBook.id == aid).first()
    obj.Lat = address.Lat 
    obj.Lon = address.Lon
    obj.Place = address.Place
    obj.ZipCode = address.ZipCode
    obj.updated_date = datetime.now()
    db.commit()
    return obj

def delete_address(db: Session, aid):
    db.query(AddressBook).filter(AddressBook.id == aid).delete()
    db.commit()


