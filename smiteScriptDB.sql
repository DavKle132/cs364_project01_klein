DROP TABLE IF EXISTS [PlayerGod];

DROP TABLE IF EXISTS [Player];

DROP TABLE IF EXISTS [God];

DROP TABLE IF EXISTS [Ability];

DROP TABLE IF EXISTS [PlayerMatch];

DROP TABLE IF EXISTS [Item];

DROP TABLE IF EXISTS [ItemDescription];


CREATE TABLE [God]
(
    [AbilityId1] INTEGER NOT NULL,
    [AbilityId2] INTEGER NOT NULL,
    [AbilityId3] INTEGER NOT NULL,
    [AbilityId4] INTEGER NOT NULL,
    [AbilityId5] INTEGER NOT NULL,
    [AttackSpeed] REAL,
    [AttackSpeedPerLevel] REAL,
    [Cons] TEXT,
    [HP5PerLevel] REAL NOT NULL,
    [Health] INTEGER NOT NULL,
    [HealthPerFive] INTEGER NOT NULL,
    [HealthPerLevel] INTEGER NOT NULL,
    [Lore] TEXT,
    [MP5PerLevel] REAL,
    [MagicProtection] REAL NOT NULL,
    [MagicProtectionPerLevel] REAL NOT NULL,
    [MagicalPower] INTEGER NOT NULL,
    [MagicalPowerPerLevel] INTEGER NOT NULL,
    [Mana] INTEGER NOT NULL,
    [ManaPerFive] INTEGER NOT NULL,
    [ManaPerLevel] INTEGER NOT NULL,
    [Name] NVARCHAR(25) NOT NULL,
    [OnFreeRotation] NVARCHAR(10),
    [Pantheon] NVARCHAR(20),
    [PhysicalPower] REAL NOT NULL,
    [PhysicalPowerPerLevel] REAL NOT NULL,
    [PhysicalProtection] REAL NOT NULL,
    [PhysicalProtectionPerLevel] REAL NOT NULL,
    [Pros] TEXT,
    [Roles] NVARCHAR(15),
    [Speed] INTEGER NOT NULL,
    [Title] TEXT,
    [Type] NVARCHAR(30),
    [GodCard_URL] TEXT,
    [GodIcon_URL] TEXT,
    [GodID] INTEGER PRIMARY KEY NOT NULL,
    [LatestGod] NVARCHAR(2),
    [BasicAttackDamage] NVARCHAR(35) NOT NULL,
    [BasicAttackProgression] TEXT NOT NULL
);

CREATE TABLE [Ability]
(
    [AbilityID] INTEGER NOT NULL PRIMARY KEY,
    [Summary] NVARCHAR(30),
    [Cooldown] NVARCHAR(20),
    [Cost] NVARCHAR(20),
    [Description] TEXT,
    [URL] TEXT
);

CREATE TABLE [Player]
(
    [PlayerID] INTEGER PRIMARY KEY NOT NULL,
    [Name] NVARCHAR(25),
    [Avatar_URL] TEXT,
    [Created_Datetime] NVARCHAR(30),
    [Leaves] INTEGER,
    [Level] INTEGER NOT NULL,
    [Losses] INTEGER NOT NULL,
    [MasteryLevel] INTEGER NOT NULL,
    [Last_Login_Datetime] NVARCHAR(30),
    [Personal_Status_Message] TEXT,
    [Region] NVARCHAR(25),
    [TeamId] INTEGER,
    [Team_Name] NVARCHAR(30),
    [Total_Achievements] INTEGER NOT NULL,
    [Total_Worshippers] INTEGER NOT NULL,
    [Wins] INTEGER NOT NULL
);

CREATE TABLE [PlayerGod]
(
    [PlayerID] INTEGER NOT NULL,
    [GodID] INTEGER NOT NULL,
    [Assists] INTEGER NOT NULL,
    [Deaths] INTEGER NOT NULL,
    [Kills] INTEGER NOT NULL,
    [Losses] INTEGER NOT NULL,
    [MinionKills] INTEGER NOT NULL,
    [Rank] INTEGER NOT NULL,
    [Wins] INTEGER NOT NULL,
    [Worshippers] INTEGER NOT NULL,
    FOREIGN KEY([PlayerID]) REFERENCES [Player]([PlayerID])
        ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY([GodID]) REFERENCES [God]([GodID])
        ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE [PlayerMatch]
(
    [ActiveId1] INTEGER NOT NULL,
    [ActiveId2] INTEGER NOT NULL,
    [Active_1] NVARCHAR(20),
    [Active_2] NVARCHAR(20),
    [Assists] INTEGER NOT NULL,
    [Creeps] INTEGER NOT NULL,
    [Damage] INTEGER NOT NULL,
    [Damage_Bot] INTEGER NOT NULL,
    [Damage_Done_In_Hand] INTEGER NOT NULL,
    [Damage_Mitigated] INTEGER NOT NULL,
    [Damage_Structure] INTEGER NOT NULL,
    [Damage_Taken] INTEGER NOT NULL,
    [Damage_Taken_Magical] INTEGER NOT NULL,
    [Damage_Taken_Physical] INTEGER NOT NULL,
    [Deaths] INTEGER NOT NULL,
    [Distance_Traveled] INTEGER NOT NULL,
    [God] NVARCHAR(20),
    [GodId] INTEGER NOT NULL,
    [Gold] INTEGER NOT NULL,
    [Healing] INTEGER NOT NULL,
    [Healing_Bot] INTEGER NOT NULL,
    [Healing_Player_Self] INTEGER NOT NULL,
    [ItemId1] INTEGER NOT NULL,
    [ItemId2] INTEGER NOT NULL,
    [ItemId3] INTEGER NOT NULL,
    [ItemId4] INTEGER NOT NULL,
    [ItemId5] INTEGER NOT NULL,
    [ItemId6] INTEGER NOT NULL,
    [Item_1] NVARCHAR(30),
    [Item_2] NVARCHAR(30),
    [Item_3] NVARCHAR(30),
    [Item_4] NVARCHAR(30),
    [Item_5] NVARCHAR(30),
    [Item_6] NVARCHAR(30),
    [Killing_Spree] INTEGER NOT NULL,
    [Kills] INTEGER NOT NULL,
    [Level] INTEGER NOT NULL,
    [Map_Game] NVARCHAR(30),
    [Match] INTEGER NOT NULL,
    [Match_Time] NVARCHAR(30),
    [Minutes] INTEGER NOT NULL,
    [Multi_kill_Max] INTEGER NOT NULL,
    [Objective_Assists] INTEGER NOT NULL,
    [Queue] NVARCHAR(30),
    [Region] NVARCHAR(25),
    [Skin] NVARCHAR(30),
    [SkinId] INTEGER NOT NULL,
    [Surrendered] INTEGER NOT NULL,
    [TaskForce] INTEGER NOT NULL,
    [Team1Score] INTEGER NOT NULL,
    [Team2Score] INTEGER NOT NULL,
    [Time_In_Match_Seconds] INTEGER NOT NULL,
    [Wards_Placed] INTEGER NOT NULL,
    [Win_Status] NVARCHAR(10),
    [Winning_TaskForce]INTEGER NOT NULL,
    [playerName] NVARCHAR(25)
);

CREATE TABLE [Item]
(
    [ID] INTEGER PRIMARY KEY AUTOINCREMENT,
    [ChildItemId] INTEGER NOT NULL,
    [DeviceName] NVARCHAR(30) NOT NULL,  
    [IconId] INTEGER NOT NULL,
    [ItemId] INTEGER NOT NULL,
    [ItemTier] INTEGER NOT NULL,
    [Price] INTEGER NOT NULL,     
    [RootItemId] INTEGER NOT NULL,
    [ShortDesc] TEXT NOT NULL,
    [Type] NVARCHAR(15),
    [itemIcon_URL] TEXT NOT NULL,
    [Description] TEXT,
    [SecondaryDescription] TEXT
);

CREATE TABLE [ItemDescription]
(
    [ID] INTEGER PRIMARY KEY AUTOINCREMENT,
    [Description] TEXT NOT NULL,
    [Value] TEXT NOT NULL,
    [ItemId] INTEGER  NOT NULL  
);