import click
from model import Admin, Patient, Doctor
from seed import session

@click.group
def cli():
    welcome_message = click.style('Welcome to Hospital Management System\n', fg = 'red')
    click.echo(welcome_message)
    

@click.command
@click.option('--register', is_flag=True, help='Register Admin')
@click.option('--add-doctor', is_flag=True, help='Add Doctor')
def admin(register, add_doctor):
    if register:
        admin_name = click.prompt("Enter Admin Name: ")
        click.echo(f"Admin '{admin_name}' registered successfully!")
    elif add_doctor:
        doctor_name = click.prompt("Enter Doctor Name: ")
        click.echo(f"Doctor '{doctor_name}' added successfully!")

if __name__ == '__main__':
    cli.add_command(admin)
  
    cli()
