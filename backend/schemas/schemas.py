from pydantic import BaseModel
from typing import Optional


class ContactSchema(BaseModel):
    # id: Optional[int] = None
    first_name: str
    last_name: str
    email: str

class AccountSchema(BaseModel):
    #user_id: Optional[int] = None
    email: str
    password: str
    #created_on: Optional[str] = None
    #last_login: Optional[str] = None