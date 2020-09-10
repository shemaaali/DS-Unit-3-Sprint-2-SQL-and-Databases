import sqlite3
import json
import pymongo

# How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?
"""
I believe working with MongoDB is a little bit different than SQL. The SQL table structures
are included pandas libraries and its' querying syntaxes are more intuitive to me. I can insert the information.
So Mongo seems to be much more flexable than postgreSQL
The most important distinction between the two SQL is vertically scalable,
noSQL is horizontally calable as adding more things. For SQL, performance is increased by adding
(CPU/RAM). I think MongoDB traffic capcacity is increased by sharing or
adding more servers.
"""

# Instantiate client
client = pymongo.MongoClient("mongodb+srv://sdshima:3b8m9oBEEAYUuzaY@cluster0.j3bqi.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# check to see if the test working
result = db.test.insert_one({'Hello Python':[4, 'Python', 5]})
print('The MongoDB Test is Working Fine\n The Inserted Id:', result.inserted_id)

# Create a new database for rpg
db = client.rpgdb
with open('rpg_data.json') as f:
    file_data = json.load(f)
db.rpgdb.insert_many(file_data)
print("The DB RPG Client:", db)



# working with the rpg database
path = '../module1-introduction-to-sql/rpg_db.sqlite3'
conn = sqlite3.connect(path)

cur1 = conn.cursor()
cur1.execute('Select * FROM charactercreator_character')
character = cur1.fetchall()
print("Cursor character:", character)

cur2 = conn.cursor()
cur2.execute('Select * FROM armory_item')
result = cur2.fetchall()
print("Cursor Result:", result)


db = client.RPG

for i in range(len(character)):
    db.characters.insert_one({
        'sql_id': character[i][0],
        'name': character[i][1],
        'level': character[i][2],
        'exp': character[i][3],
        'hp': character[i][4],
        'str': character[i][5],
        'int': character[i][6],
        'dex': character[i][7],
        'wis': character[i][8],
    })

for i in range(len(result)):
    db.result.insert_one({
        'sql_id': character[i][0],
        'name':character[i][1],
        'cost': character[i][2],
        'weight': character[i][3],
    })
    