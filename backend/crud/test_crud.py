from sqlalchemy.orm import sessionmaker
from database.database import DBConnection


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
        
    def insert_contact(self,c_model):    
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(c_model)
        session.commit()
        session.close()
        return('Successfully added to DB')

    def delete_contact(self, contact_name):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        c_model = ContactModel()
        session.query(c_model).filter(c_model['first_name']==contact_name).delete()
        session.commit()
        

    
    