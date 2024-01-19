from sqlalchemy import create_engine,Column,Integer,String,func,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime


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
    app_date = Column(DateTime, default=func.current_timestamp())

    # establish connection to doctors
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))

    # establish connection to admin
    admin_id = Column(Integer(), ForeignKey('admins.id'))

    def __repr__ (self):
        return f'name: {self.name}'\
        f'id_no: {self.id_no}'\
        f'gender: {self.gender}'\
        f'age: {self.age}'\
                  
 # doctors class
     
class Doctor(Base):
    __tablename__ = 'doctors'

    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    email = Column(String())
    app_fees = Column(Integer())

    # establish connection to patients
    patient  = relationship('Patient', backref= 'doctors')

   
    # establish connection to admin
    admin_id = Column(Integer(), ForeignKey('admins.id'))


    def __repr__ (self):
        return f'name: {self.name}'\
        f'email: {self.email}'\
        f'consoltation fees: {self.app_fees}'\


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # establish connection to both patient and doctors
    patient = relationship('Patient', backref='admins')
    doctor = relationship('Doctor', backref='admins')


    def __repr__ (self):
        return f'name: {self.name}'\
     
        
  
