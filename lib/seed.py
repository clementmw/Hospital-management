from faker import Faker
from sqlalchemy.orm import sessionmaker
from model import engine, Base, Patient,Doctor, Admin

Session = sessionmaker(bind = engine)
session = Session()

session.commit()