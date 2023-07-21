import psycopg2
from passlib.hash import pbkdf2_sha256

con = psycopg2.connect(dbname = "passwords", host = "localhost", user = "lucastemb")
cur = con.cursor()
cur.execute("select masterpass from managee;")
print(type(cur.fetchone()[0]))
password = input()

if (pbkdf2_sha256.verify(password, f"{cur.fetchone()}")):
    print("Welcome!")
else:
    print("Error.") 

cur.close()
con.close()
