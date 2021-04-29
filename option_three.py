import psycopg2
from cryption import *

def handle_option_three():
    platform = input('Platform: ')
    password = input('New Password: ')
    print(change_existing_password(password, platform))

def change_existing_password(password, platform):
    connection = psycopg2.connect(
        dbname = 'passwords',
        host = 'localhost',
        user = 'jesustembras'
    )
    cursor = connection.cursor()

    try:
        true_platform = None
        query_one = ("select platform from accounts")
        cursor.execute(query_one)
        for enc_platform in cursor.fetchall(): 
            if AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').decrypt(enc_platform[0]) == platform.lower():
                true_platform = enc_platform[0]
        if true_platform == None:
            return('Platform not found.')
        query_two = 'update accounts set password = (%s) where platform = (%s)'
        argument = (AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').encrypt(password), true_platform, )
        cursor.execute(query_two, argument)
        return('Success!')
    except: 
        return('Something went wrong. Try again.')
    finally:
        connection.commit()
        cursor.close()
        connection.close()