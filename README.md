# fastapi_geo_assignment
for assignment

This application use "geopy" for geo location related data
Swagger Docs is available for this application.
for swagger document endpoint - http://127.0.0.1:8000/docs

Prerequisite
Python 3.7+ should be installed

instruction to run the app
1. create vertual environment
python3 -m venv env

2. activate the vertual environment
source env/bin/activate

3. install the required packages
pip install --upgrade -r requirements.txt

4. run the application
uvicorn main:app --reload

Application endpoints details
/address_list/ 
-> this will return all addresses from Addressbook

/address_list_by_location/
-> provide the distance(in kilometer), latitude and longitude so it will return inrange address list 

/address_create/
-> to create the address using the format
{
  "Lat": 0,
  "Lon": 0,
  "Place": "string",
  "ZipCode": 0
}

/update-address/{aid}
-> get the address id and pass to the aid parameter and also use the formate to update the data for the given id
{
  "Lat": 0,
  "Lon": 0,
  "Place": "string",
  "ZipCode": 0
}

/delete-address/{aid}
-> get the address id and pass to the aid parameter to delete the address from addressbook

Note: 
1. aid refers address id which get be get from address_list endpoint
2. This Application also using Logging on request and it is stored in the fastapi.log file.
