from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///hospital.db')

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    gender=Column(String())
    id_no = Column(Integer())
    age = Column(Integer())
    phone_number = Column(Integer())

    def __repr__ (self):
        return f'name: {self.name}'\
        f'id_no: {self.id_no}'\
        f'gender: {self.gender}'\
        f'age: {self.age}'\
        

        
  

