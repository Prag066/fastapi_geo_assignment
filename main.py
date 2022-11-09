'''
This is the main module to run the application
'''
from fastapi import FastAPI, HTTPException, Depends, Query
import schema, crud
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from model import Base

Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

# database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# get all Address list 
@app.get("/address_list/", response_model=List[schema.AddressBook])
def get_address(db: Session = Depends(get_db)):
    return crud.get_all_address(db=db)

# get Address by location and distance
@app.get("/address_list_by_location/", response_model=List[schema.AddressBook])
def get_address_by_location(distance: float=Query(description="distance in KM"),lat: float=Query(description="latitude"), lon: float=Query(description="longitude"), db: Session = Depends(get_db)):
    return crud.get_address_by_location(distance=distance,lat=lat, lon=lon, db=db)

# create request for Address
@app.post("/address_create/", response_model=schema.AddressInfo)
def create_address(address: schema.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)

# check the address if it exists using address id
def get_addressbook_obj(db, aid):
    obj = crud.get_address(db=db, aid=aid)
    if obj is None:
        raise HTTPException(status_code=404, detail=f"Address Not Found for {aid}")
    return obj

# update request for Address
@app.put("/update-address/{aid}", response_model=schema.AddressInfo)
def update_address(aid: int, address: schema.AddressCreate, db: Session = Depends(get_db)):
    get_addressbook_obj(db=db, aid=aid) # geting Address object if exists
    obj = crud.update_address(db=db, aid=aid, address=address) # updating the address record based on Address Id
    return obj

# delete request for Address
@app.delete("/delete-address/{aid}")
def delete_address(aid: int, db: Session = Depends(get_db)):
    get_addressbook_obj(db=db, aid=aid) # geting Address object if exists
    crud.delete_address(db=db, aid=aid) # deleting the address record based on Address Id
    return {"details": "Address deleted", "status_code": 204}
