import sqlite3


class ItemDescription:
    def __init__(self, json, ItemId):
        # print(json)
        self.attributes = (
            json['Description'],
            json['Value'],
            ItemId
        )

    def toDB(self, dbPath, json):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO ItemDescription (\
            Description,                    \
            Value,                          \
            ItemId                          \
            ) VALUES (?,?,?)', self.attributes)

        conn.commit()
        conn.close()