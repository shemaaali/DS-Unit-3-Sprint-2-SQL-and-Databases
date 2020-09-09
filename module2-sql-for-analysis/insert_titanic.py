import pandas as pd
import numpy as np
import psycopg2

DATA_PATH  = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Linear-Models/master/data/'
df = pd.read_csv(DATA_PATH+'titanic/train.csv')
print(df.shape)
print(df.head())


DB_NAME = 'obgeebcm'
DB_USER = 'obgeebcm'
DB_PASSWORD = 'V8UxJY7QEPU20Tbojx_2fkSFq1KdLT7O'
DB_HOST = 'lallah.db.elephantsql'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host = DB_HOST)

create_titanic = """
CREATE TABLE titanic_table (
  PassengerId       SERIAL PRIMARY KEY,
  Survived          int,
  Pclass            int,
  Name	            varchar(40) NOT NULL,
  Sex               varchar(40) NOT NULL,	
  Age               int,
  SibSp             int,
  Parch	            int,
  Ticket            varchar(40) NOT NULL,
  Fare              int,
  Cabin             varchar(40) NOT NULL,
  Embarked          varchar(40) NOT NULL,
  data    JSONB
);
"""

insert_titanic = """
INSERT INTO titanic_table(PassengerId, Survived, Pclass ,Name, Sex, Age, SibSp, Parch, Ticket data) VALUES
(
  'A row Name',
  null
),
(
  'Another row, with JSON',
  '{ "S": 3, "NaN": ["C85", "C123",  53.1000], "C": true }'::JSONB
);
"""

print("connection:", conn)
cur = conn.cursor()
print("cursor:", cur)

cur.execute(create_titanic)
cur.execute(insert_titanic)

cur.execute("SELECT * from create_titanic;")

result_query = cur.fetchall()
print(result_query)