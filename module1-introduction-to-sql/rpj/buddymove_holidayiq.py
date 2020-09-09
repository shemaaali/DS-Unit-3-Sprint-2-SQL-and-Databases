import sqlite3

connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#breakpoint()


query = 'SELECT COUNT(*) FROM Nature;'

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row), row)

