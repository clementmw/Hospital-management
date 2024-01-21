import click
from model import Admin, Patient, Doctor
from seed import session

@click.group
def cli():
    welcome_message = click.style('WELCOME TO HOSPITAL MANAGEMENT SYSTEM \n', fg = 'green')
    click.echo(welcome_message)
    

@cli.command()

def admin():
   click.echo(click.style('ADMIN PANEL', fg = 'blue'))
   click.echo(click.style('1. Register', fg = 'red'))
   click.echo(click.style('2. Login', fg = 'red'))
   click.echo(click.style('3. Get all doctors', fg = 'red'))
   click.echo(click.style('4. Get all patients', fg = 'red'))
   click.echo(click.style('5. Add doctor', fg = 'red'))
   click.echo(click.style('6. Delete doctor', fg = 'red'))

   choice = click.prompt('Enter your choice(1-6)', type=int)

   if choice == 1:
       username = click.prompt('Enter Username')
       password = click.prompt('Enter Password', hide_input=True)

       existing_admin = session.query(Admin).filter_by (username = username).first()
       if existing_admin:
           click.echo(click.style('Admin already exists', fg = 'red'))
       else:
         new_admin = Admin(username = username, password = password)
         session.add(new_admin)
         session.commit()
         click.echo(click.style('Admin created successfully', fg = 'green'))

   elif choice == 2:
       username = click.prompt('Enter Username')
       password = click.prompt('Enter Password', hide_input=True)

       admin = session.query(Admin).filter_by(username = username, password = password).first()
       if admin:
           click.echo(click.style('Login Successful', fg = 'green'))
       else:
           click.echo(click.style('Login Failed', fg = 'red'))  

   elif choice == 3:
       doctors = session.query(Doctor).all()
       for doctor in doctors:
           click.echo(f'{doctor.id}, DR {doctor.name} ')
          

   elif choice == 4:
       patients = session.query(Patient).all()
       for patient in patients:
           click.echo(patient)
     
   elif choice == 5:
       name = click.prompt('Enter Doctor name')
       email = click.prompt('Enter EmailAddress')
       uid_no = click.prompt('Enter Doctor UID_NO')
       fees = click.prompt('Enter doctor charges')

       existing_id = session.query(Doctor).filter_by(id_no = uid_no).first()
       if existing_id:
           click.echo(click.style('Doctor already exists', fg = 'red'))
       else:
            doctor = Doctor(name = name, email = email, id_no = uid_no, app_fees = fees)
            session.add(doctor)
            session.commit()
            click.echo(click.style('Doctor created successfully', fg = 'green'))   

   elif choice == 6:
       delete_doctor = click.prompt('Enter Doctor UID_NO')

       doctor_to_delete = session.query(Doctor).filter_by(id_no=delete_doctor).first()

       if doctor_to_delete:
            confirmation  = click.confirm(f'Do you want to delete doctor {doctor_to_delete}', default=False)
       
            if confirmation:
                session.delete(doctor_to_delete)
                session.commit()
                click.echo(click.style('Doctor deleted successfully', fg = 'green'))
            else:
                click.echo(click.style('delete aborted', fg = 'red'))
       else:
           click.echo(click.style('Doctor does not exist', fg = 'red'))

 # patient side 
               
@cli.command()
def patient():
   click.echo(click.style('PATIENT PANEL', fg = 'blue'))
   click.echo(click.style('1. Register', fg = 'red'))
   click.echo(click.style('2. Login', fg = 'red'))

   patient_choice = click.prompt('Enter your choice(1-2)', type=int)

   if patient_choice == 1:
       name = click.prompt('Enter Patient name')
       gender = click.prompt('Enter Gender male/female')
       id_no = click.prompt('Enter Patient ID_NO', type=int)
       age = click.prompt('Enter patient age')
       phone_number = click.prompt('Enter patient phone number')
       doctor_name = click.prompt('Enter doctor name')

       existing_id = session.query(Patient).filter_by(id_no = id_no).first()
       existing_doctor = session.query(Doctor).filter_by(name = doctor_name).first()
       if existing_id:
           click.echo(click.style('Patient already exists {name}', fg = 'red'))
       elif not existing_doctor:
           click.echo(click.style('Please confirm Doctor Name', fg = 'red'))
       else:
            patient = Patient(name = name, gender = gender, id_no = id_no, age = age,phone_number=phone_number, doctor_id = existing_doctor.id)
            session.add(patient)
            session.commit()
            click.echo(click.style('Patient created successfully', fg = 'green'))

   elif patient_choice == 2:
       patient_id = click.prompt('Enter Patient ID_NO', type=int)
       exists = session.query(Patient).filter_by(id_no = patient_id).first()

       if exists:
           click.echo(click.style(f'Login succesfull: {exists}', fg = 'green'))
       else:
           click.echo(click.style('Patient not found please Register', fg = 'red'))

# doctor side
           
@cli.command()
def doctor():
    authenticated = False

    while not authenticated:
        click.echo(click.style('DOCTOR PANEL', fg='blue'))
        click.echo(click.style('1. Register', fg='red'))
        click.echo(click.style('2. Login', fg='red'))

        doctor_choice = click.prompt('Enter your choice (1-2)', type=int)

        if doctor_choice == 1:
            name = click.prompt('Enter Doctor name')
            email = click.prompt('Enter EmailAddress')
            uid_no = click.prompt('Enter Doctor UID_NO')
            fees = click.prompt('Enter doctor charges')

            existing_id = session.query(Doctor).filter_by(id_no=uid_no).first()
            if existing_id:
                click.echo(click.style('Doctor already exists', fg='red'))
            else:
                doctor = Doctor(name=name, email=email, id_no=uid_no, app_fees=fees)
                session.add(doctor)
                session.commit()
                click.echo(click.style('Doctor Registered successfully', fg='green'))

        elif doctor_choice == 2:
            doctor_id = click.prompt('Enter Doctor UID_NO', type=int)
            exists = session.query(Doctor).filter_by(id_no=doctor_id).first()

            if exists:
                click.echo(click.style(f'Login successful: {exists.name}', fg='green'))
                authenticated = True
            else:
                click.echo(click.style('Doctor not found. Please register.', fg='red'))

    while authenticated:
        click.echo(click.style("You are authenticated as a doctor. Perform actions here.", fg = 'blue'))

        click.echo(click.style('1. Get your patients', fg = 'red'))

        doc_choice = click.prompt('Enter your choice (1)', type=int)

        if doc_choice == 1:
            patients = session.query(Patient).filter_by(doctor_id=exists.id)
            for patient in patients:
                click.echo(patient)
        else:
            click.echo(click.style('Cannot find scheduled appointment', fg = 'red'))
        break
        


   

if __name__ == '__main__':
    cli.add_command(admin)
    cli.add_command(patient)
    cli.add_command(doctor)
  
    cli()
