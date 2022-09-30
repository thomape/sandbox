from sqlalchemy.orm import sessionmaker
from database.database import DBConnection
from models.test_model import ContactModel


class TestCrud():

    def __init__(self):
        dbconn = DBConnection()
        self.engine = dbconn.get_engine(
            dbconn.creds['pguser'],
            dbconn.creds['pgpasswd'],
            dbconn.creds['pghost'],
            dbconn.creds['pgport'],
            dbconn.creds['pgdb']
        )
        
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

    def delete_contact(self, contact_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.delete(contact_id)
        session.commit()
        return('Successfully deleted from DB')
        

    
    