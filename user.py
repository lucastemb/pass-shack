import psycopg2
from database import curr_master_pass, has_hint
class user(): 
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
        
    cursor = connection.cursor()
    cursor.execute("select * from vault;")
    fetch = cursor.fetchone()
    if curr_master_pass():
        password = ((fetch)[0])
    else:
        pass
    if has_hint():
        hint = ((fetch)[1])
    else:
        pass
    cursor.close()
    connection.close()

