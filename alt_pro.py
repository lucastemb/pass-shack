import psycopg2
import getpass
from database import curr_master_pass, has_hint
from functionality import *
from passlib.hash import pbkdf2_sha256
from user import user
from option_one import *
from option_four import *
from option_two import * 
from option_three import *
from option_five import *
from cryption import * 
from option_six import * 

def masterpass(): 
    tries = 0
    if curr_master_pass():
        try:
            print("\nYour vault is locked. Verify your master password to continue.")
            masterpw = getpass.getpass("Master Password: ")
            while not (pbkdf2_sha256.verify(masterpw, user.password)):
                tries += 1
                if(tries >= 3 and has_hint()):
                    print("\nHint: %s" % (AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').decrypt(user.hint)))
                print("\nYour vault is locked. Verify your master password to continue.")
                masterpw = getpass.getpass("Master Password: ")
            startup()    
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
            handle_option_one()
            startup()
        elif(option == '2'):
            handle_option_two()
            startup()
        elif(option == '3'):
            handle_option_three()
            startup()
        elif(option == '4'):
            handle_option_four()
            startup()
        elif(option == '5'):
            handle_option_five()
            startup()
        elif(option == '6'):
            handle_option_six()
            startup()
        elif(option.lower() == 'q'):
            pass
        else: 
            print("Please enter one of the specified options.")
            startup()
    except (ValueError, SyntaxError, NameError) as e:
        print("Please enter one of the specfied options.")
        startup()


def menu():
    print(('-'*25) + 'Menu'+ ('-' *25))
    print('1. Create new password')
    print('2. Find a password for a site or app')
    print('3. Change existing password')
    print('4. Delete existing account information')
    print('5. Change master password hint')
    print('6. Change master password')
    print('Q. Exit')
    print('-'*54)


masterpass()
    
