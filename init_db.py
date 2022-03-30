import sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cur = connection.cursor()

connection.close()
