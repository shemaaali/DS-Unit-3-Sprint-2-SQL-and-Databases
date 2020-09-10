import pandas as pd
import numpy as np
import psycopg2

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

cur.execute('''DROP TABLE IF EXISTS titanic_table; CREATE TABLE IF NOT EXISTS titanic_table(
  Survived bytea,
  Pclass smallint,
  Name varchar(200),
  Sex sex_binary	
  Age decimal,
  Siblings_Spouses_Aboard smallint,
  Parent_Children_Aboard smallint,
  Fare decimal);''')

#cur.execute('''INSERT INTO titanic_table(Survived, Pclass ,Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
#VALUES 
#(2, 3, 'C8556', 'C85', 23,  53.1000, 67, 'good', 12, 'btyu', 'auto'),
#(9, 7, 'C7867', 'C67', 125,  55.1000, 5, 'goodness', 13, 'niceo', 'beyoon');''')

cur.execute("SELECT * from titanic_table;")

result_query = cur.fetchall()
print("result_query:",result_query)

#cur.close()
#conn.commit()
#conn.close()

# for loop to insert the whole table
for index, row in df.iterrows():
     cur.execute(f'''INSERT INTO titanic_table(Survived, Pclass ,Name, Sex, Age, Siblings_Spouses_Aboard, Parent_Children_Aboard,	Fare)
VALUES 
( 
  {row[0]}, {row[1]}, '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}, {row[6]}, {row[7]}
)
    ''')