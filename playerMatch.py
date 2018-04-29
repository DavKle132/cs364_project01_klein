import sqlite3


class PlayerMatch:
    def __init__(self, json):
        # print(json)
        self.attributes = (
            json['ActiveId1'],
            json['ActiveId2'],
            json['Active_1'],
            json['Active_2'],
            json['Assists'],
            json['Creeps'],
            json['Damage'],
            json['Damage_Bot'],
            json['Damage_Done_In_Hand'],
            json['Damage_Mitigated'],
            json['Damage_Structure'],
            json['Damage_Taken'],
            json['Damage_Taken_Magical'],
            json['Damage_Taken_Physical'],
            json['Deaths'],
            json['Distance_Traveled'],
            json['God'],
            json['GodId'],
            json['Gold'],
            json['Healing'],
            json['Healing_Bot'],
            json['Healing_Player_Self'],
            json['ItemId1'],
            json['ItemId2'],
            json['ItemId3'],
            json['ItemId4'],
            json['ItemId5'],
            json['ItemId6'],
            json['Item_1'],
            json['Item_2'],
            json['Item_3'],
            json['Item_4'],
            json['Item_5'],
            json['Item_6'],
            json['Killing_Spree'],
            json['Kills'],
            json['Level'],
            json['Map_Game'],
            json['Match'],
            json['Match_Time'],
            json['Minutes'],
            json['Multi_kill_Max'],
            json['Objective_Assists'],
            json['Queue'],
            json['Region'],
            json['Skin'],
            json['SkinId'],
            json['Surrendered'],
            json['TaskForce'],
            json['Team1Score'],
            json['Team2Score'],
            json['Time_In_Match_Seconds'],
            json['Wards_Placed'],
            json['Win_Status'],
            json['Winning_TaskForce'],
            json['playerName']
        )

    def toDB(self, dbPath):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO PlayerMatch (\
            ActiveId1,                      \
            ActiveId2,                      \
            Active_1,                       \
            Active_2,                       \
            Assists,                        \
            Creeps,                         \
            Damage,                         \
            Damage_Bot,                     \
            Damage_Done_In_Hand,            \
            Damage_Mitigated,               \
            Damage_Structure,               \
            Damage_Taken,                   \
            Damage_Taken_Magical,           \
            Damage_Taken_Physical,          \
            Deaths,                         \
            Distance_Traveled,              \
            God,                            \
            GodId,                          \
            Gold,                           \
            Healing,                        \
            Healing_Bot,                    \
            Healing_Player_Self,            \
            ItemId1,                        \
            ItemId2,                        \
            ItemId3,                        \
            ItemId4,                        \
            ItemId5,                        \
            ItemId6,                        \
            Item_1,                         \
            Item_2,                         \
            Item_3,                         \
            Item_4,                         \
            Item_5,                         \
            Item_6,                         \
            Killing_Spree,                  \
            Kills,                          \
            Level,                          \
            Map_Game,                       \
            Match,                          \
            Match_Time,                     \
            Minutes,                        \
            Multi_kill_Max,                 \
            Objective_Assists,              \
            Queue,                          \
            Region,                         \
            Skin,                           \
            SkinId,                         \
            Surrendered,                    \
            TaskForce,                      \
            Team1Score,                     \
            Team2Score,                     \
            Time_In_Match_Seconds,          \
            Wards_Placed,                   \
            Win_Status,                     \
            Winning_TaskForce,              \
            playerName                      \
            ) VALUES (                      \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?,                \
            ?,?,?,?,?,?,?,?)', self.attributes)
        conn.commit()
        conn.close()