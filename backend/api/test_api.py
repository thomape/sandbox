from fastapi import APIRouter, Query
from schemas.test_schema import ContactSchema
from models.test_model import ContactModel
from crud.test_crud import TestCrud
router = APIRouter()
contacts = {}


@router.get('/get-all-contacts')
def test():
    return {'message':'test'}

@router.post('/create-contact')
def create_contact(contact:ContactSchema):
    c_model = ContactModel()
    c_model.first_name = contact.first_name
    c_model.last_name = contact.last_name
    c_model.email = contact.email
    tc = TestCrud()
    res = tc.create_contact(c_model)
    return res

@router.delete('/delete-contact')
def delete_contact(contact_id:int):
    print('hi')
    tc = TestCrud()
    res = tc.delete_contact(contact_id)
    return res
    