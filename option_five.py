import psycopg2
from cryption import *
from user import user

def handle_option_five(): 
    hint = input('Type new hint: ')
    if not hint:
        print('Error: hint was empty.')
    else: 
        print(insert_new_pw(hint))

    



def insert_new_pw(hint):
    try: 
        connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
        )
        cursor = connection.cursor()
        query = "update vault set hint = (%s) where masterpass = (%s)"
        arguments = ((AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').encrypt(hint), user.password, ))
        cursor.execute(query, arguments)
        return('Success!')
    except: 
        return('An error occured.')
    finally: 
        connection.commit()
        cursor.close()
        connection.close()

    