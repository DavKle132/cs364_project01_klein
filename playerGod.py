import sqlite3


class PlayerGod:
    def __init__(self, json):
        # print(json)
        self.attributes = (
            json['Assists'],
            json['Deaths'],
            json['Kills'],
            json['Losses'],
            json['MinionKills'],
            json['Rank'],
            json['Wins'],
            json['Worshippers'],
            json['god_id'],
            json['player_id']
        )

    def toDB(self, dbPath):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO PlayerGod (  \
            Assists,                        \
            Deaths,                         \
            Kills,                          \
            Losses,                         \
            MinionKills,                    \
            Rank,                           \
            Wins,                           \
            Worshippers,                    \
            GodID,                          \
            PlayerID                        \
            ) VALUES (?,?,?,?,?,?,?,?,?,?)', self.attributes)
        conn.commit()
        conn.close()