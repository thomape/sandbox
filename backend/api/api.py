from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from schemas.schemas import AccountSchema, ContactSchema
from models.models import AccountModel, ContactModel
from crud.crud import ContactOperations, AccountOperations
import datetime as dt
from api.auth import SecurityService


router = APIRouter()
http_basic = HTTPBasic()
ss = SecurityService()


@router.get('/')
def home(credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)
    return {'message':'Home'}

@router.get('/get-all-contacts')
def test(credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)
    return {'message':'test'}

@router.post('/create-contact')
def create_contact(contact:ContactSchema,credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)

    c_model = ContactModel()
    c_model.first_name = contact.first_name
    c_model.last_name = contact.last_name
    c_model.email = contact.email
    ops = ContactOperations()
    res = ops.create_contact(c_model)
    return res

@router.delete('/delete-contact')
def delete_contact(c_model:ContactSchema,credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)

    ops = ContactOperations()
    res = ops.delete_contact(c_model)
    return res
    

@router.post('/signin')
def sign_in(account:AccountSchema,credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)

    a_model = AccountModel()
    a_model.email = account.email
    a_model.user_pwd = account.password
    ops = AccountOperations()
    res = ops.sign_in(a_model)
    return res

@router.post('/signup')
def sign_up(account:AccountSchema,credentials: HTTPBasicCredentials = Depends(http_basic)):
    ss.verify(credentials)

    a_model = AccountModel()
    a_model.email = account.email
    a_model.user_pwd = account.password
    a_model.created_on = dt.datetime.now()
    a_model.last_login = dt.datetime.now()
    a_model.login_attempts = 0
    ops = AccountOperations()
    res = ops.sign_up(a_model)
    return res
