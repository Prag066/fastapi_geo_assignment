'''
This is for crud operation and return the error message if error
'''
from datetime import datetime
from sqlalchemy.orm import Session
from model import AddressBook
import schema,logging
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from fastapi import HTTPException

# intialize logging
# # setup loggers
# remove the default looging of fastapi
logging.getLogger("uvicorn").handlers.clear()
log = logging.getLogger("app-log:")
logging.basicConfig(filename='fastapi.log',encoding='utf-8', filemode='a',format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

# intialize geopy  
geolocator = Nominatim(user_agent="crudapitest")

# method for creating address
def create_address(db: Session, address: schema.AddressCreate):
    location = geolocator.geocode(address.Place)
    data = location.raw
    loc_data = data['display_name'].split()
    address.Lat = data['lat']
    address.Lon = data['lon']
    try:
        postalcode = int(loc_data[-2].strip(','))
    except Exception as e:
        log.error(f'{address.Place} address is not valid.')
        raise HTTPException(status_code=404, detail="Please enter valid Address.")

    address.ZipCode = postalcode
    obj = AddressBook(**address.dict())
    db.add(obj)
    db.commit()
    log.info(f'address created for {address.Place}')
    return obj

# method for geting data from database
def get_all_address(db: Session):
    logging.info(f'get address list from datbase')
    return db.query(AddressBook).all()

# method for geting data from database by address id
def get_address(db: Session, aid):
    logging.info(f'get address list from datbase by address id {aid}')
    return db.query(AddressBook).filter(AddressBook.id == aid).first()

# # method for geting data from database by distance and lat and lon
def get_address_by_location(db: Session, distance, lat, lon):
    get_ids = []
    query = db.query(AddressBook).all()
    for i in query:
        distannce_in_km = geodesic((i.Lat, i.Lon),(lat,lon)).km
        if distance >= distannce_in_km:
            get_ids.append(i.id)
    logging.info(f'get address list from datbase by distance {distance}, lat {lat} and lon {lon}')
    return list(db.query(AddressBook).filter(AddressBook.id.in_(get_ids)))

# method for updating data from database 
def update_address(db: Session, aid, address: schema.AddressCreate):
    obj = db.query(AddressBook).filter(AddressBook.id == aid).first()
    obj.Place = address.Place
    location = geolocator.geocode(address.Place)
    data = location.raw
    loc_data = data['display_name'].split()
    obj.Lat = data['lat']
    obj.Lon = data['lon']
    try:
        postalcode = int(loc_data[-2].strip(','))
    except:
        log.error(f'{address.Place} address is not valid.')
        raise HTTPException(status_code=404, detail="Please enter valid Address.") 
    obj.ZipCode = postalcode
    obj.updated_date = datetime.now()
    db.commit()
    logging.info(f'update address for {address.Place}')
    return obj

# method for deleting data from database
def delete_address(db: Session, aid):
    db.query(AddressBook).filter(AddressBook.id == aid).delete()
    logging.warning(f'address has been deleted for address id {aid}')
    db.commit()


