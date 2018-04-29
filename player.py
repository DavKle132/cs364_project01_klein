import sqlite3
from playerGod import PlayerGod
from playerMatch import PlayerMatch

class Player:
    def __init__(self, json, jsonPG, jsonM):
        self.attributes = (
            json[0]['Avatar_URL'],
            json[0]['Created_Datetime'],
            json[0]['Id'],
            json[0]['Last_Login_Datetime'],
            json[0]['Leaves'],
            json[0]['Level'],
            json[0]['Losses'],
            json[0]['MasteryLevel'],
            json[0]['Name'],
            json[0]['Personal_Status_Message'],
            json[0]['Region'],
            json[0]['TeamId'],
            json[0]['Team_Name'],
            json[0]['Total_Achievements'],
            json[0]['Total_Worshippers'],
            json[0]['Wins'],
        )

    def toDB(self, dbPath, json, jsonPG, jsonM):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO Player ( \
            Avatar_URL,                 \
            Created_Datetime,           \
            PlayerID,                   \
            Last_Login_Datetime,        \
            Leaves,                     \
            Level,                      \
            Losses,                     \
            MasteryLevel,               \
            Name,                       \
            Personal_Status_Message,    \
            Region,                     \
            TeamId,                     \
            Team_Name,                  \
            Total_Achievements,         \
            Total_Worshippers,          \
            Wins                        \
            ) VALUES (                  \
            ?,?,?,?,?,?,                \
            ?,?,?,?,?,?,                \
            ?,?,?,?)', self.attributes)

        conn.commit()
        conn.close()

        for x in jsonM:
            m = PlayerMatch( x )
            m.toDB('db.sqlite3')

        for x in jsonPG:
            pg = PlayerGod( x )
            pg.toDB('db.sqlite3')

        
        
