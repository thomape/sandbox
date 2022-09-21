from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

class DBConnection:
    def __init__(self) -> None:
        self.creds = {
            'pguser':'sandbox',
            'pgpasswd':'sandbox',
            'pghost':'localhost',
            'pgport':'5432',
            'pgdb':'sandbox'
        }

    def get_engine(self,user, password, host, port, db):
        url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    
        if not database_exists(url):
            create_database(url)
    
        engine = create_engine(url, pool_size=50, echo=False)
    
        return engine