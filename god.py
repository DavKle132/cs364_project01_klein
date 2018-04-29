import sqlite3
from ability import Ability


class God:
    def __init__(self, json):
        # print(json)
        self.attributes = (
            json['AbilityId1'],
            json['AbilityId2'],
            json['AbilityId3'],
            json['AbilityId4'],
            json['AbilityId5'],
            json['AttackSpeed'],
            json['AttackSpeedPerLevel'],
            json['Cons'],
            json['HP5PerLevel'],
            json['Health'],
            json['HealthPerFive'],
            json['HealthPerLevel'],
            json['Lore'],
            json['MP5PerLevel'],
            json['MagicProtection'],
            json['MagicProtectionPerLevel'],
            json['MagicalPower'],
            json['MagicalPowerPerLevel'],
            json['Mana'],
            json['ManaPerFive'],
            json['ManaPerLevel'],
            json['Name'],
            json['OnFreeRotation'],
            json['Pantheon'],
            json['PhysicalPower'],
            json['PhysicalPowerPerLevel'],
            json['PhysicalProtection'],
            json['PhysicalProtectionPerLevel'],
            json['Pros'],
            json['Roles'],
            json['Speed'],
            json['Title'],
            json['Type'],
            json['godCard_URL'],
            json['godIcon_URL'],
            json['id'],
            json['latestGod'],
            json['basicAttack']['itemDescription']['menuitems'][0]['value'],
            json['basicAttack']['itemDescription']['menuitems'][1]['value'],
        )

    def toDB(self, dbPath, json):
        conn = sqlite3.connect(dbPath)
        c = conn.cursor()
        c.execute('SELECT * FROM God WHERE GodID = ?', (json['id'],))
        rows = c.fetchall()
        if(len(rows) == 0):
            c.execute('INSERT INTO God (    \
                AbilityId1,                 \
                AbilityId2,                 \
                AbilityId3,                 \
                AbilityId4,                 \
                AbilityId5,                 \
                AttackSpeed,                \
                AttackSpeedPerLevel,        \
                Cons,                       \
                HP5PerLevel,                \
                Health,                     \
                HealthPerFive,              \
                HealthPerLevel,             \
                Lore,                       \
                MP5PerLevel,                \
                MagicProtection,            \
                MagicProtectionPerLevel,    \
                MagicalPower,               \
                MagicalPowerPerLevel,       \
                Mana,                       \
                ManaPerFive,                \
                ManaPerLevel,               \
                Name,                       \
                OnFreeRotation,             \
                Pantheon,                   \
                PhysicalPower,              \
                PhysicalPowerPerLevel,      \
                PhysicalProtection,         \
                PhysicalProtectionPerLevel, \
                Pros,                       \
                Roles,                      \
                Speed,                      \
                Title,                      \
                Type,                       \
                GodCard_URL,                \
                GodIcon_URL,                \
                GodID,                      \
                LatestGod,                  \
                BasicAttackDamage,          \
                BasicAttackProgression      \
                ) VALUES (                  \
                ?,?,?,?,?,?,                \
                ?,?,?,?,?,?,                \
                ?,?,?,?,?,?,                \
                ?,?,?,?,?,?,                \
                ?,?,?,?,?,?,                \
                ?,?,?,?,?,?,?,?,?)', self.attributes)

            conn.commit()
            conn.close()

            Ability1 = Ability(json['Ability_1'])
            Ability2 = Ability(json['Ability_2'])
            Ability3 = Ability(json['Ability_3'])
            Ability4 = Ability(json['Ability_4'])
            Ability5 = Ability(json['Ability_5'])

            Ability1.toDB('db.sqlite3')
            Ability2.toDB('db.sqlite3')
            Ability3.toDB('db.sqlite3')
            Ability4.toDB('db.sqlite3')
            Ability5.toDB('db.sqlite3')
        
        