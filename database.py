import psycopg2 
from passlib.hash import pbkdf2_sha256


def curr_master_pass(): 
    has_pass = True
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
        
    cursor = connection.cursor()
    cursor.execute("select masterpass from vault;")
    try: 
        cursor.fetchone()[0]
    except: 
        has_pass = False
    cursor.close()
    connection.close()
    return has_pass

def has_hint():
    hint = True
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
        
    cursor = connection.cursor()
    cursor.execute("select hint from vault;")
    try: 
        cursor.fetchone()[0]
    except: 
        hint = False
    cursor.close()
    connection.close()
    return hint
    

def insert_hashed_masterpass(masterpass, hint): 
    hashedpass = pbkdf2_sha256.hash(masterpass)
    connection = psycopg2.connect(
        dbname = "passwords",
        host = "localhost",
        user = "jesustembras"
    )
    cursor = connection.cursor()
    query = "INSERT INTO vault(masterpass, hint) VALUES(%s, %s);"
    hashedpw = (hashedpass, hint,  )
    cursor.execute(query, hashedpw)
    connection.commit()
    cursor.close()
    connection.close()
    
    