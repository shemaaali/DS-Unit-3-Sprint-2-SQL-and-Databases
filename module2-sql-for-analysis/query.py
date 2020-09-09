import psycopg2

DB_NAME = 'ulhkihqg'
DB_USER = 'ulhkihqg'
DB_PASSWORD = 'OFhPOgi-dYtXICf9i5n5Kl9XWWbfgKZt'
DB_HOST = 'hansken.db.elephantsql.com'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host = DB_HOST)
print("connection:", conn)
cur = conn.cursor()
print("cursor:", cur)
cur.execute("SELECT * from test_table;")

result_query = cur.fetchall()
print(result_query)