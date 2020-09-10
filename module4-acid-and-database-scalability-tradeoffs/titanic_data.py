import psycopg2
import sqlite3
import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.shape)
print(df.head())

DB_NAME = 'obgeebcm'
DB_USER = 'obgeebcm'
DB_PASSWORD = 'V8UxJY7QEPU20Tbojx_2fkSFq1KdLT7O'
DB_HOST = 'lallah.db.elephantsql.com'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host = DB_HOST)
                   
print("connection:", conn)
cur = conn.cursor()
print("cursor:", cur)


cur.execute('SELECT * FROM titanic_table WHERE survived = 1')
survived = len(cur.fetchall())
print("survived:", survived)

cur.execute('SELECT * FROM titanic_table WHERE survived = 0')
died = len(cur.fetchall())
print("died:", died)

cur.execute('SELECT AVG(age) FROM titanic_table WHERE survived = 1')
Avg_Age_Live = cur.fetchall()[0][0]
print("Avg_Age_Live:", Avg_Age_Live)

cur.execute('SELECT AVG(age) FROM titanic_table WHERE survived = 0')
Avg_Age_Die = cur.fetchall()[0][0]
print("Avg_Age_Die:", Avg_Age_Die)

cur.execute('SELECT AVG(age) FROM titanic_table WHERE pclass = 1')
Avg_Age_Class1 = cur.fetchall()[0][0]
print("Avg_Age_Class1:", Avg_Age_Class1)

cur.execute('SELECT AVG(age) FROM titanic_table WHERE pclass = 2')
Avg_Age_Class2 = cur.fetchall()[0][0]
print("Avg_Age_Class2:", Avg_Age_Class2)

cur.execute('SELECT AVG(age) FROM titanic_table WHERE pclass = 3')
Avg_Age_Class3 = cur.fetchall()[0][0]
print("Avg_Age_Class3:", Avg_Age_Class3)

cur.execute('SELECT AVG(fare) FROM titanic_table WHERE pclass = 1')
Avg_Fare_Pclass1 = cur.fetchall()[0][0]
print("Avg_Fare_Pclass1:", Avg_Fare_Pclass1)

cur.execute('SELECT AVG(fare) FROM titanic_table WHERE pclass = 2')
Avg_Fare_Pclass2 = cur.fetchall()[0][0]
print("Avg_Fare_Pclass1:", Avg_Fare_Pclass1)

cur.execute('SELECT AVG(fare) FROM titanic_table WHERE pclass = 3')
Avg_Fare_Pclass3 = cur.fetchall()[0][0]
print("Avg_Fare_Pclass3:", Avg_Fare_Pclass3)