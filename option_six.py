import psycopg2
from cryption import *
from user import user

def handle_option_six(): 
    masterpass = input('Type new master password: ')
    if not masterpass:
        print('Error: hint was empty.')
    else: 
        print(insert_new_masterpass(masterpass))

    



def insert_new_masterpass(masterpass):
    try: 
        connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
        )
        cursor = connection.cursor()
        query = "update vault set masterpass = (%s) where masterpass = (%s)"
        hashedpass = pbkdf2_sha256.hash(masterpass)
        arguments = (hashedpass, user.password, )
        cursor.execute(query, arguments)
        return('Success!')
    except: 
        return('An error occured.')
    finally: 
        connection.commit()
        cursor.close()
        connection.close()