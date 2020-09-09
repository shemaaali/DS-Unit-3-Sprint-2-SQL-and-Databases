import sqlite3

connection = sqlite3.connect("rpg_db.sqlite3")
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = 'SELECT COUNT (*) FROM charactercreater_character'
result = cursor.execute(query).fetchall()

#cursor.execute('''SELECT COUNT(item_id) FROM charactercreator_character_inventory, GROUP BY character_id''')

#print(cursor.fetchall())
#result = cursor.execute(query).fetchall()
#print("RESULT ", result)

cursor.execute('''SELECT AVG(count) FROM
               (SELECT COUNT(item_id) FROM charactercreator_character_inventory,
               GROUP BY character_id)''')
print(cursor.fetchall())

for row in result:
    print(type(row), row)

cursor.close()
connection.commit()

