from faker import Faker
from sqlalchemy.orm import sessionmaker
from model import engine, Base, Patient, Doctor, Admin

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# to delete after instance

session.query(Doctor).delete()
session.query(Patient).delete()
session.query(Admin).delete()

# Create Faker instance
fake = Faker()

# Function to seed patients
def seed_patients():
    for _ in range(10):
        patient = Patient(
            name=fake.name(),
            gender=fake.random_element(elements=('Male', 'Female')),
            id_no=fake.random_int(min=100000, max=999999),
            age=fake.random_int(min=18, max=80),
            phone_number=fake.phone_number(),
            app_date=fake.date_time_this_decade(),
        )
        session.add(patient)

# Function to seed doctors
def seed_doctors():
    for _ in range(5):
        doctor = Doctor(
            name=fake.name(),
            email=fake.email(),
            app_fees=fake.random_int(min=50, max=200),
        )
        session.add(doctor)

# Function to seed admins
def seed_admins():
    for _ in range(2):
        admin = Admin(
            username=fake.name(),
            password = fake.password()
        )
        session.add(admin)

# Seed data
seed_patients()
seed_doctors()
seed_admins()

print("seeded data succesfully")

# Commit the changes
session.commit()
