import sqlite3
from itemdesc import ItemDescription

class Item:
    def __init__(self, json):
        # print(json)
        if json['ItemDescription']['Description'] != None and json['ItemDescription']['SecondaryDescription'] != None:
            self.attributes = (
                json['ChildItemId'],
                json['DeviceName'],
                json['IconId'],
                json['ItemId'],
                json['ItemTier'],
                json['Price'],
                json['RootItemId'],
                json['ShortDesc'],
                json['Type'],
                json['itemIcon_URL'],
                json['ItemDescription']['Description'],
                json['ItemDescription']['SecondaryDescription']
            )
        elif json['ItemDescription']['Description'] == None and json['ItemDescription']['SecondaryDescription'] != None:
            self.attributes = (
                json['ChildItemId'],
                json['DeviceName'],
                json['IconId'],
                json['ItemId'],
                json['ItemTier'],
                json['Price'],
                json['RootItemId'],
                json['ShortDesc'],
                json['Type'],
                json['itemIcon_URL'],
                None,
                json['ItemDescription']['SecondaryDescription']
            )
        elif json['ItemDescription']['Description'] != None and json['ItemDescription']['SecondaryDescription'] == None:
            self.attributes = (
                json['ChildItemId'],
                json['DeviceName'],
                json['IconId'],
                json['ItemId'],
                json['ItemTier'],
                json['Price'],
                json['RootItemId'],
                json['ShortDesc'],
                json['Type'],
                json['itemIcon_URL'],
                json['ItemDescription']['Description'],
                None
            )
        else:
            self.attributes = (
                json['ChildItemId'],
                json['DeviceName'],
                json['IconId'],
                json['ItemId'],
                json['ItemTier'],
                json['Price'],
                json['RootItemId'],
                json['ShortDesc'],
                json['Type'],
                json['itemIcon_URL'],
                json['ItemDescription']['Description'],
                json['ItemDescription']['SecondaryDescription']
            )


    def toDB(self, dbPath, json):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('INSERT INTO Item (       \
            ChildItemId,                    \
            DeviceName,                     \
            IconId,                         \
            ItemId,                         \
            ItemTier,                       \
            Price,                          \
            RootItemId,                     \
            ShortDesc,                      \
            Type,                           \
            itemIcon_URL,                   \
            Description,                    \
            SecondaryDescription            \
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', self.attributes)
        
        conn.commit()
        conn.close()

        menuItems = json['ItemDescription']['Menuitems']
        for x in menuItems:
            itemDesc = ItemDescription(x, json['ItemId'])
            itemDesc.toDB(dbPath, json)