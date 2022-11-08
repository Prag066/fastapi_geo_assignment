from fastapi import FastAPI, HTTPException, Response, Depends
import schema
from typing import List
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, engine
from model import Base


Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/address_list/", response_model=List[schema.AddressBook])
def get_address(db: Session = Depends(get_db)):
    return crud.get_all_address(db=db)

@app.post("/address_create/", response_model=schema.AddressInfo)
def create_address(address: schema.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)

def get_addressbook_obj(db, aid):
    obj = crud.get_address(db=db, aid=aid)
    if obj is None:
        raise HTTPException(status_code=404, detail="Address Not Found")
    return obj

@app.put("/address/{aid}", response_model=schema.AddressInfo)
def update_address(aid: int, address: schema.AddressCreate, db: Session = Depends(get_db)):
    get_addressbook_obj(db=db, aid=aid)
    obj = crud.update_address(db=db, aid=aid, address=address)
    return obj

@app.delete("/address/{aid}")
def delete_address(aid: int, db: Session = Depends(get_db)):
    get_addressbook_obj(db=db, aid=aid)
    crud.delete_address(db=db, aid=aid)
    return {"details": "Address deleted", "status_code": 204}
