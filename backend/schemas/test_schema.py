from pydantic import BaseModel
from typing import Optional


class ContactSchema(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: Optional[str] = None