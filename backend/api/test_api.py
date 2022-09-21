from fastapi import APIRouter
from schemas.test_schema import ContactSchema
from models.test_model import ContactModel
from crud.test_crud import TestCrud
router = APIRouter()
contacts = {}


@router.get('/test')
def test():
    return {'message':'test'}

@router.post('/contact')
def test_full(contact:ContactSchema):
    # contact_id = len(contacts) + 1
    # contacts[contact_id] = contact
    # print(contacts)
    # return contacts[contact_id]
    c_model = ContactModel()
    c_model.first_name = contact.first_name
    c_model.last_name = contact.last_name
    c_model.email = contact.email
    tc = TestCrud()
    res = tc.insert_contact(c_model)
    return res

@router.delete('/contact/{contact_name}')
def delete_contact(contact_name: str):
    tc = TestCrud()
    res = tc.delete_contact(contact_name)
    return res