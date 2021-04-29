import psycopg2
from cryption import *
def handle_option_four(): 
    platform = input('Platform: ')
    print(delete_account(platform))

def delete_account(platform):
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
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
        query_two = ("delete from accounts where platform = (%s)")
        argument = (true_platform,)
        cursor.execute(query_two, argument)
        return('Success!')
    except: 
        return ('Platform does not exist.')
    finally: 
        connection.commit()
        cursor.close()
        connection.close()
