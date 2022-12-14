from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary

Base = declarative_base()

class ContactModel(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, index=True, unique=True, autoincrement=True, primary_key=True)
    first_name = Column(String, primary_key=True)
    last_name = Column(String)
    email = Column(String)

    def __repr__(self) -> str:
        return f'<User(first_name="{self.first_name}", last_name="{self.last_name}", email="{self.email}")>'



class AccountModel(Base):
    __tablename__='accounts'

    user_id = Column(Integer, index=True, unique=True, autoincrement=True, primary_key=True)
    email = Column(String, primary_key=True, unique=True)
    user_pwd = Column(LargeBinary)
    salt = Column(LargeBinary)
    created_on = Column(String)
    last_login = Column(String)
    login_attempts = Column(Integer)