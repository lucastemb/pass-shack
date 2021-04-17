import psycopg2
import getpass
from database import curr_master_pass
from functionality import *
from passlib.hash import pbkdf2_sha256
from user import user
def masterpass(): 
    if curr_master_pass():
        try:
            print("\nYour vault is locked. Verify your master password to continue.")
            masterpw = getpass.getpass("Master Password: ")
            if pbkdf2_sha256.verify(masterpw, user.password):
                startup()
            else: 
                masterpass()
        except (ValueError, SyntaxError, NameError) as e:
            print("Incorrect password. Try again.")
    else: 
        add_master_pass_wrapper()


def startup():
    try:
        print("\n")
        menu()
        option = getpass.getpass("")
        if(option == '1'):
            print("New Password")
        elif(option == '2'):
            print("Want it back?")
        elif(option.lower() == 'q'):
            pass
        else: 
            print("Please enter one of the specified options.")
    except (ValueError, SyntaxError, NameError) as e:
        print("Please enter one of the specfied options.")


def menu():
    print(('-'*25) + 'Menu'+ ('-' *25))
    print('1. Create new password')
    print('2. Find a password for a site or app')
    print('Q. Exit')
    print('-'*54)


masterpass()
    
