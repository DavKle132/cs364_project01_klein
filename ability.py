import sqlite3


class Ability:
    def __init__(self, json):
        # print(json)
        jsonDesc = json['Description']['itemDescription']
        self.attributes = (
            jsonDesc['cooldown'],
            jsonDesc['cost'],
            jsonDesc['description'],
            json['Id'],
            json['Summary'],
            json['URL']
        )

    def toDB(self, dbPath):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO Ability (\
            Cooldown,                   \
            Cost,                       \
            Description,                \
            AbilityID,                  \
            Summary,                    \
            URL                         \
            ) VALUES (?,?,?,?,?,?)', self.attributes)
        conn.commit()
        conn.close()
