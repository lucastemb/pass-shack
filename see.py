import psycopg2

conn = psycopg2.connect( host = "localhost", dbname = "lucastemb", user = "lucastemb")

cur = conn.cursor()

cur.execute("select first_name, last_name from students")
row = cur.fetchone()
while row != None: 
    print(row[0], row[1])
    row = cur.fetchone() 
cur.close()
conn.close()