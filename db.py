from client import Client
import sqlite3
devId = '2378'
autKey = '16884716A7714D918BF411C9822E9989'
baseUrl = 'http://api.smitegame.com/smiteapi.svc/'

class Db:
    def __init__(self, dbAddr):
        self.dbAddr = dbAddr
        self.c = Client(devId, autKey, self.dbAddr)

    def newPlayer(self, pName):
        print('Updating Script...', end='', flush=True)
        self.c.resetDB('smiteScriptDB.sql')
        print('Complete')
        self.pName = pName
        print('Adding Players and their stats...', end='', flush=True)
        self.c.playerRankMatchDB(self.pName)
        print('Complete')
        self.c = Client(devId, autKey, self.dbAddr)
        print('Adding Items...', end='', flush=True)
        self.c.itemDB()
        print('Complete')
        print('Adding Gods and Abilities...', end='', flush=True)
        self.c.godAbilityDB()
        print('Complete')


    def getFriends(self):
        conn = sqlite3.connect(self.dbAddr)
        c = conn.cursor()
        c.execute('SELECT Name, Level, Wins, Losses, MasteryLevel, Total_Worshippers, Last_Login_Datetime  FROM Player')
        rows = c.fetchall()
        names = [description[0] for description in c.description]
        conn.close()
        return {'rows':rows, 'names':names}

    def getGods(self):
        conn = sqlite3.connect(self.dbAddr)
        c = conn.cursor()
        c.execute('SELECT Name, Roles AS Role, Pantheon, Type, Title FROM God ORDER BY Name')
        rows = c.fetchall()
        names = [description[0] for description in c.description]
        conn.close()
        return {'rows':rows, 'names':names}

    def getBestRole(self, pName):
        conn = sqlite3.connect(self.dbAddr)
        c = conn.cursor()
        c.execute("SELECT God.Roles, sum(PlayerGod.Worshippers) AS Worshippers \
                    FROM Player JOIN PlayerGod JOIN God \
                    ON Player.PlayerID = PlayerGod.PlayerID AND PlayerGod.GodID = God.GodID \
                    WHERE Player.Name LIKE '%' || ? \
                    GROUP BY God.Roles \
                    ORDER BY sum(PlayerGod.Worshippers) DESC", (pName,))
        rows = c.fetchall()
        names = [description[0] for description in c.description]
        conn.close()
        return {'rows':rows, 'names':names}

    def whoWonMore(self, player, god):
        conn = sqlite3.connect(self.dbAddr)
        c = conn.cursor()
        c.execute("SELECT Player.Name, PlayerGod.Wins, PlayerGod.Losses, PlayerGod.Worshippers \
                    FROM Player JOIN PlayerGod JOIN God \
                    ON Player.PlayerId = PlayerGod.PlayerId AND PlayerGod.GodID = God.GodID \
                    WHERE God.Name = ? AND PlayerGod.Wins > (SELECT PlayerGod.Wins \
                                                                    FROM Player JOIN PlayerGod JOIN God \
                                                                    ON Player.PlayerID = PlayerGod.PlayerID AND PlayerGod.GodID = God.GodID \
                                                                    WHERE Player.Name LIKE '%' || ? AND God.Name = ?)\
                    ORDER BY PlayerGod.Worshippers DESC", (god, player, god,))
        rows = c.fetchall()
        names = [description[0] for description in c.description]
        conn.close()
        return {'rows':rows, 'names':names}




