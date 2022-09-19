from optparse import Option
import uvicorn
from fastapi import FastAPI, Request, Path, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

class Contact(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

devices = {
    # 1: {
    #     "name": "Iphone 14",
    #     "price": 1300,
    #     "brand" : "Apple"
    # },
    # 2: {
    #     "name": "Iphone 13",
    #     "price": 1000,
    #     "brand" : "Apple"
    # },
    # 3: {
    #     "name": "Ipod",
    #     "price": 300,
    #     "brand" : "Apple"
    # },
    # 4: {
    #     "name": "Nokia",
    #     "price": 130,
    #     "brand" : "Nokia"
    # }
}

contacts = {}

@app.get('/')
async def root():
    return len(devices)

@app.post('/contact')
def test_full(contact: Contact):
    contact_id = len(contacts) + 1
    contacts[contact_id] = contact
    print(contacts)
    return contacts[contact_id]

@app.get('/device-id/{device_id}')
def get_device(device_id: int = Path(None, description='Device ID',gt=0,le=4)):
    return devices[device_id]

@app.get('/device-name')
def get_device(name: str = Query(None, title="name", description="Name of device")):
    for device_id in devices:
        if devices[device_id].name == name:
            return devices[device_id]
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No device found")

@app.post('/create-device')
def create_device(item: Item):
        device_id = len(devices) + 1
        devices[device_id] = item
        print(devices)
        return devices[device_id]

@app.put('/update-device/{device_id}')
def update_device(device_id: int, item: UpdateItem):
    if device_id not in devices:
        return {'Error': 'Device does not exist.'}
    if item.name != None:
        devices[device_id].name = item.name
    if item.price != None:
        devices[device_id].price = item.price
    if item.brand != None:
        devices[device_id].brand = item.brand
    return devices[device_id]

@app.delete('/delete-device')
def delete_device(device_id: int = Query(..., description="ID of device", ge=0)):
    if device_id not in devices:
        return {'Error': 'ID does not exists'}
    del devices[device_id]
    return {'Success': 'Item deleted'}

if __name__ == '__main__':
    uvicorn.run('app:app',port=8000,reload=True)