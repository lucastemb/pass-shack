import psycopg2
import getpass 
import pyperclip
from cryption import * 

def handle_option_two():
    app = input('Enter platform or app: ')
    print(checker(app))

def checker(platform):
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
    cursor = connection.cursor()
    try:
        query = ("select  * from accounts")
        cursor.execute(query)
        for table in cursor.fetchall():
            decryptedTuple = (AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').decrypt(table[0]), AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').decrypt(table[1]),)
            if decryptedTuple[0] == platform.lower():
                return(AESCipher('+MbQeThVmYq3t6w9z$C&F)J@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5v8y/B?').decrypt(table[1])) 
        return('Platform does not exist.')
    except: 
        return('Error')
    finally: 
        connection.commit()
        cursor.close()
        connection.close()

