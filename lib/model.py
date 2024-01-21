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
        return f'Patient name: {self.name}'\
        f'  id_no: {self.id_no}'\
        f'  Gender: {self.gender}'\
        f'  Age: {self.age}'\
        f'  Appointment: {self.app_date}'\
        f'  Doctor id: {self.doctor_id}'
    
                  
 # doctors class
     
class Doctor(Base):
    __tablename__ = 'doctors'

    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    email = Column(String())
    id_no = Column(Integer())
    app_fees = Column(Integer())

    # establish connection to patients
    patient  = relationship('Patient', backref= 'doctors')

   
    # establish connection to admin
    admin_id = Column(Integer(), ForeignKey('admins.id'))


    def __repr__ (self):
        return f'name: {self.name}'\
        f'  Email: {self.email}'\
        f'  Consoltation fees: KSH{self.app_fees} /='\


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())

    # establish connection to both patient and doctors
    patient = relationship('Patient', backref='admins')
    doctor = relationship('Doctor', backref='admins')


    def __repr__ (self):
        return f'name: {self.name}'\
     
        
  

