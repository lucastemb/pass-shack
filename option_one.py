import psycopg2
import getpass
from cryption import *

def handle_option_one(): 
    platform = input('Platform: ')
    password = input('Password: ')
    # try:
    insert_new_pw(platform.lower(), password)
    # except: 
    #     print('Something went wrong. Please try again.')


def insert_new_pw(platform, password):
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
    cursor = connection.cursor()
    query = "INSERT INTO accounts(platform, password) VALUES(%s, %s);"
    arguments = ((AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').encrypt(platform.lower())), (AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').encrypt(password)), )
    cursor.execute(query, arguments)
    connection.commit()
    cursor.close()
    connection.close()
