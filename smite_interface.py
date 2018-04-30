from db import Db
db = Db('db.sqlite3')

def main():
    input_var = 'temp'
    while(input_var != 'exit'):
        input_var = input("smite_friends> ")
        inList = input_var.split(' -')
        print()
        valid = parseList(inList)
        if(valid == 1):
            print('Wrong number of parameters.\nDo "help" for more information')
        if(valid == 2):
            print('Invalid command.\nDo "help" for more information')
        if(input_var != 'exit'):
            print()

def parseList(inList):
    if(len(inList) == 0):
        return 1

    if(inList[0] == 'exit'):
        return 0

    if(inList[0] == 'help'):
        printHelp()
        return 0

    if(inList[0].lower() == 'getgods'):
        if(len(inList) != 1):
            return 1
        response = db.getGods()
        pprintResponse(response)
        return 0

    if(inList[0].lower() == 'getfriends'):
        if(len(inList) != 1):
            return 1
        response = db.getFriends()
        pprintResponse(response)
        return 0

    if(inList[0].lower() == 'averagedamage'):
        if(len(inList) != 1):
            return 1
        response = db.averageDamage()
        pprintResponse(response)
        return 0

    if(inList[0].lower() == 'getmatches'):
        if(len(inList) != 2):
            return 1
        response = db.getMatches(inList[1])
        pprintResponse(response)
        return 0

    if(inList[0].lower() == 'newplayer'):
        if(len(inList) == 2):
            db.newSinglePlayer(inList[1])
            return 0
        elif(len(inList) == 3):
            if(inList[2] == 'b'):
                db.newPlayer(inList[1])
            return 0  
        return 1

    if(inList[0].lower() == 'rolestats'):
        if(len(inList) != 2):
            return 1
        response = db.getBestRole(inList[1])
        pprintResponse(response)
        return 0

    if(inList[0].lower() == 'betterwith'):
        if(len(inList) != 3):
            return 1
        response = db.whoWonMore(inList[1], inList[2])
        pprintResponse(response)
        return 0

    return 2

def printHelp():
    print('exit                                  : Terminates execution of smite_friends')
    print('help                                  : Prints to console how to utilize commands')
    print('getfriends                            : Shows all players currently in database')
    print('getgods                               : Shows all gods currenlty playable in SMITE')
    print('averagedamage                         : Shows the average damage for all gods who have been played')
    print('newplayer  -<Player_Name>             : Adds a single player into the database')
    print('newplayer  -<Player_Name> -b          : Resets database and pulls down for all data for Player_Name and all friends')
    print('getmatches -<Player_Name>             : Shows all recent matches for a specific player (Includes AI matches)')
    print('rolestats  -<Player_Name>             : Shows all classes and associated worshipper totals')
    print('betterwith -<Player_Name> -<God_Name> : Shows all friends who have more worshippers with the designated god')
    print('\nNote that all commands are case-insensitive, but all tags are case-sensitive.')

def pprintResponse(response):
    maxList = []
    names = response['names']
    rows = response['rows']
    sum = 0
    for name in names:
        maxList.append(len(str(name)))
    
    for tuple in rows:
        i = 0
        for elem in tuple:
            if(maxList[i] < len(str(elem))):
                maxList[i] = len(str(elem))
            i+=1
    
    i = 0
    while(i < len(maxList)):
        maxList[i] += 2
        sum += maxList[i]
        i+=1
    
    i = 0

    for name in names:
        offset = maxList[i]
        print('{var:{offset}}'.format(var = str(name), offset = offset), end='', flush=True)
        i+=1
    print()

    i = 0
    while(i < (sum - 2)):
        print('_', end='', flush=True)
        i+=1
    print()

    for tuple in rows:
        i = 0
        for elem in tuple:
            offset = maxList[i]
            print('{var:{offset}}'.format(var = str(elem), offset = offset), end='', flush=True)
            i+=1
        print()



    




main()