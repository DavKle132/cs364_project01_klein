import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('SELECT * FROM God Where GodID = 3492')
rows = c.fetchall()
print(len(rows))