import psycopg2
from database import curr_master_pass
class user(): 
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "lucastemb"
    )
        
    cursor = connection.cursor()
    cursor.execute("select masterpass from vault;")
    if curr_master_pass():
        password = cursor.fetchone()[0] 
    else:
        pass
    cursor.close()
    connection.close()
