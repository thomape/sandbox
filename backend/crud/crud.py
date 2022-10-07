import datetime as dt
from typing import Tuple
import os
import hashlib
import hmac
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from models.models import AccountModel, Base, ContactModel
from database.database import DBConnection


class BaseOperations:
    def __init__(self):
        dbconn = DBConnection()
        self.engine = dbconn.get_engine(
            dbconn.creds['pguser'],
            dbconn.creds['pgpasswd'],
            dbconn.creds['pghost'],
            dbconn.creds['pgport'],
            dbconn.creds['pgdb']
        )
        

class ContactOperations(BaseOperations):

    def create_contact(self,c_model):    
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(c_model)
        session.commit()
        session.close()
        return('Successfully added to DB')

    def get_all_contacts(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.get()
        session.close()
        return session

    def delete_contact(self, c_model):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(ContactModel).filter(ContactModel.email == c_model.email).delete()
        session.commit()
        return('Successfully deleted from DB')



class AccountOperations(BaseOperations):

    def sign_in(self,a_model):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        check_pwd = PasswordEncryption()
        target_user = session.query(AccountModel).filter(AccountModel.email == a_model.email)

        if target_user.count() != 1:
            return "Invalid username/password"
        else:
            attempt_count = 0
            for user in target_user:
                is_valid = check_pwd.check_password(user.salt,user.user_pwd,a_model.user_pwd)
                attempt_count = user.login_attempts
        
            if is_valid and attempt_count <= 5:
                target_user.update({AccountModel.login_attempts: 0})
                target_user.update({AccountModel.last_login: dt.datetime.now()})
                session.commit()
                session.close()
                return "Success"
            elif not is_valid and attempt_count > 5:
                return "Account locked. Too many unsuccessful attempts."
            else:
                attempt_count += 1
                target_user.update({AccountModel.login_attempts: attempt_count})
                session.commit()
                session.close()
                return "Invalid username/password"

    def sign_up(self, a_model):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        target_user = session.query(AccountModel).filter(AccountModel.email == a_model.email)

        if target_user.count() == 1:
            return "Account already exists."
        else:
            encrypt_pwd = PasswordEncryption()
            salt, pwd_hash = encrypt_pwd.new_password(a_model.user_pwd)
            a_model.user_pwd = pwd_hash
            a_model.salt = salt
            session.add(a_model)
            session.commit()
            session.close()
            return {"message":"New account created."}



class PasswordEncryption:

    def new_password(self, password: str) -> Tuple[bytes,bytes]:
        salt = os.urandom(16)
        pwd_hash = hashlib.pbkdf2_hmac('sha256',password.encode(), salt, 100000)
        return salt, pwd_hash

    def check_password(self, salt: bytes, pwd_hash: bytes, password: str) -> bool:
        return hmac.compare_digest(
            pwd_hash,
            hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        )
