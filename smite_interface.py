from db import Db
db = Db('db.sqlite3')

def main():
    input_var = 'temp'
    while(input_var != 'exit'):
        input_var = input("smite_friends> ")
        inList = input_var.split(' -')
        valid = parseList(inList)
        if(valid == 1):
            print('Wrong number of parameters.\nDo "help" for more information')
        if(valid == 2):
            print('Invalid command.\nDo "help" for more information')
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
        printResponse(response)
        return 0

    if(inList[0].lower() == 'getfriends'):
        if(len(inList) != 1):
            return 1
        response = db.getFriends()
        printResponse(response)
        return 0

    if(inList[0].lower() == 'newplayer'):
        if(len(inList) != 2):
            return 1
        db.newPlayer(inList[1])
        return 0

    if(inList[0].lower() == 'rolestats'):
        if(len(inList) != 2):
            return 1
        response = db.getBestRole(inList[1])
        printResponse(response)
        return 0

    if(inList[0].lower() == 'betterwith'):
        if(len(inList) != 3):
            return 1
        response = db.whoWonMore(inList[1], inList[2])
        printResponse(response)
        return 0

    return 2

def printHelp():
    print('exit                                  : Terminates execution of smite_friends')
    print('help                                  : Prints to console how to utilize commands')
    print('getfriends                            : Shows all players currently in database')
    print('getgods                               : Shows all gods currenlty playable in SMITE')
    print('newplayer  -<Player_Name>             : Updates database to use new player and their friends')
    print('rolestats  -<Player_Name>             : Shows all classes and associated worshipper totals')
    print('betterwith -<Player_Name> -<God_Name> : Shows all friends who have more worshippers with the designated god')
    print('\nNote that all commands are case-insensitive, but all tags are case-sensitive.')

def printResponse(response):
    names = response['names']
    rows = response['rows']
    for name in names:
        print('{:22}'.format(str(name)), end='', flush=True)
    print()
    for tuple in rows:
        for elem in tuple:
            print('{:22}'.format(str(elem)), end='', flush=True)
        print()
    print()




main()