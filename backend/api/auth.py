import os
from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException, status
import secrets
from dotenv import load_dotenv,find_dotenv



class SecurityService:

    def __init__(self):
        load_dotenv('/home/terrington/projects/sandbox/backend/api/auth.env')
        self.username = os.getenv('BASIC_AUTH_USERNAME')
        self.password = os.getenv('BASIC_AUTH_PASSWORD')


    def verify(self, credentials: HTTPBasicCredentials) -> None:
        correct_credentials = secrets.compare_digest(credentials.username + credentials.password, self.username + self.password)
        if not correct_credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )