from fastapi import APIRouter, Query
from schemas.schemas import AccountSchema, ContactSchema
from models.models import AccountModel, ContactModel
from crud.crud import Crud
from datetime import date
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
    crud = Crud()
    res = crud.create_contact(c_model)
    return res

@router.delete('/delete-contact')
def delete_contact(contact_id:int):
    crud = Crud()
    res = crud.delete_contact(contact_id)
    return res
    

@router.post('/signin')
def signin(account:AccountSchema):
    a_model = AccountModel()
    #a_model.id = account.id
    a_model.email = account.email
    a_model.user_pwd = account.password
    a_model.created_on = date.today()
    a_model.last_login = date.today()
    crud = Crud()
    res = crud.signin(a_model)
    return res