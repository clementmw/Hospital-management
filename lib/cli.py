import click
from model import Admin, Patient, Doctor
from seed import session

@click.group
def cli():
    welcome_message = click.style('Welcome to Hospital Management System\n', fg = 'blue')
    click.echo(welcome_message)
    

@cli.command()

def admin():
   admin =  click.style('ADMIN PANEL', fg = 'blue')
   click.echo(admin)
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

       admin = session.query(Admin).filter_by(username = username, password = password)
       if admin:
           click.echo(click.style('Login Successful', fg = 'green'))
       else:
           click.echo(click.style('Login Failed', fg = 'red'))  

   elif choice == 3:
       doctors = session.query(Doctor).all()
       for doctor in doctors:
           click.echo(doctor)

   elif choice == 4:
       patients = session.query(Patient).all()
       for patient in patients:
           click.echo(patient)
     
   elif choice == 5:
       name = click.prompt('Enter Doctor name')
       email = click.prompt('Enter EmailAddress')
       id_no = click.prompt('Enter Doctor ID_NO')
       fees = click.prompt('Enter doctor charges')

       doctor = Doctor(name = name, email = email, id_no = id_no, app_fees = fees)
       session.add(doctor)
       session.commit()
       click.echo(click.style('Doctor created successfully', fg = 'green'))

   elif choice == 6:
       delete_doctor = click.prompt('Enter Doctor ID_NO')

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
       
       

       










@cli.command()
def patient():
    pass

    

    
   

if __name__ == '__main__':
    cli.add_command(admin)
  
    cli()
