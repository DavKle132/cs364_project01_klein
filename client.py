from datetime import datetime, date, time
import requests
import json
import hashlib
from pprint import pprint
from god import God
from player import Player
from item import Item
import sqlite3
from sqlite3 import OperationalError

# This class parses endpoint URLs based on devId, autKey, and Timestamp
# @author = DavidKlein
# @date   = 5/3/2018

class Client:
    devId = None
    autKey = None
    session = None
    db = None
    baseUrl = 'http://api.smitegame.com/smiteapi.svc/'

    def __init__(self, dID, aKey, db):
        self.devId = dID
        self.autKey = aKey
        self.db = db
        url = self.baseUrl + 'createsessionjson/' + self.devId + '/' + self.generateSignature('createsession') + '/' + generateTs()

        r = requests.get( url )
        text = r.text
        parsed_json = json.loads(text)
        self.session = parsed_json['session_id']

    

    def getFriends(self, player):
        url = self.baseUrl + 'getfriendsjson/' + self.devId + '/' + self.generateSignature('getfriends') + '/' + self.session + '/' + generateTs() + '/' + player
        r = requests.get( url )
        text = json.loads( r.text )
       # print(text)
        return text

    def getGods(self):
        url = self.baseUrl + 'getgodsjson/' + self.devId + '/' + self.generateSignature('getgods') + '/' + self.session + '/' + generateTs() + '/1'
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def getPlayer(self, player):
        url = self.baseUrl + 'getplayerjson/' + self.devId + '/' + self.generateSignature('getplayer') + '/' + self.session + '/' + generateTs() + '/' + player
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def getGodRanks(self, player):
        url = self.baseUrl + 'getgodranksjson/' + self.devId + '/' + self.generateSignature('getgodranks') + '/' + self.session + '/' + generateTs() + '/' + player
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def getMatchHistory(self, player):
        url = self.baseUrl + 'getmatchhistoryjson/' + self.devId + '/' + self.generateSignature('getmatchhistory') + '/' + self.session + '/' + generateTs() + '/' + player
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def getMatchDetails(self, mID):
        url = self.baseUrl + 'getmatchdetailsjson/' + self.devId + '/' + self.generateSignature('getmatchdetails') + '/' + self.session + '/' + generateTs() + '/' + str(mID)
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def getItems(self):
        url = self.baseUrl + 'getitemsjson/' + self.devId + '/' + self.generateSignature('getitems') + '/' + self.session + '/' + generateTs() + '/1'
        r = requests.get( url )
        text = json.loads( r.text )
       # print( text )
        return text

    def generateSignature(self, methodname):
        """Generates a new MD5 hashed signature

        Parameters
        ----------
        methodname : str
            The method that will be called.

        """
        now = generateTs()
        sig = hashlib.md5(self.devId.encode('utf-8') + methodname.encode('utf-8') + self.autKey.encode('utf-8') + now.encode('utf-8')).hexdigest()
        return sig

    def godAbilityDB(self):
        gods = self.getGods()
        for x in gods:
            god = God(x)
            god.toDB(self.db, x)

    def playerRankMatchDB(self, player):
        p = self.getPlayer(player)
        pg = self.getGodRanks(player)
        m = self.getMatchHistory(player)
        p1 = Player(p, pg, m)
        p1.toDB(self.db, p, pg, m)
        friends = self.getFriends(player)
        for f in friends:
            # print(f['name'])
            if f['name'] != '':
                pJson = self.getPlayer(f['name'])
                jsonPG = self.getGodRanks(f['name'])
                jsonM = self.getMatchHistory(f['name'])
                player = Player(pJson, jsonPG, jsonM)
                player.toDB(self.db, pJson, jsonPG, jsonM)
    
    def singlePlayer(self, player):
        p = self.getPlayer(player)
        pg = self.getGodRanks(player)
        m = self.getMatchHistory(player)
        try:
            p1 = Player(p, pg, m)
            p1.toDB(self.db, p, pg, m)
        except IndexError:
            print(player, ' has their profile hidden')
        except sqlite3.IntegrityError:
            print(player, ' has their profile hidden')

    def itemDB(self):
        items = self.getItems()
        for x in items:
            item = Item( x )
            item.toDB( self.db, x )

    def resetDB(self, file):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        
        fd = open(file, 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                c.execute(command)
                conn.commit()
            except OperationalError:
                print( 'Command skipped: ')

        conn.close()


def generateTs():
    def padInt( i ):
        s = str( i )
        l = len( s )
        if l == 1:
            s = '0' + s
        return s

    now = datetime.utcnow()

    nYear = padInt( now.year )
    nMonth = padInt( now.month )
    nDay = padInt( now.day )
    nHour = padInt( now.hour )
    nMin = padInt( now.minute )
    nSec = padInt( now.second )

    ts = nYear + nMonth + nDay + nHour + nMin + nSec

    return ts


