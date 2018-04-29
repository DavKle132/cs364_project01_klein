from db import Db

db = Db('db.sqlite3')

rows = db.whoWonMore('MrDramaQueen', 'Nox')
for row in rows:
    print(row)