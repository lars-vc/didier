from enum import Enum

myId = "171671190631481345"
didierId = "680510935164911730"
botIDs = [
    "155149108183695360",
    "234395307759108106",
    "239631525350604801",
    "408785106942164992",
    "679679176466235399",
    "680510935164911730",
    "706148003949314069",
    "728361496874057812"
]
BugReports = "762668401960812554"
CallOfCode = "626699611192688641"
CoCGeneral = "626699611813314561"
DeZandbak = "728361030404538488"
ErrorLogs = "762668505455132722"
FeatureRequests = "762668473313787964"

mods = {
    626699611192688641: [384457911377854467, 171671190631481345],
    728361030404538488: [171671190631481345],
    689200072268841106: [332948151226990614, 171671190631481345, 280025474485321729, 237239312385703951],
    710515840566427721: [171671190631481345, 140186024075722752, 296197359539585024]
}

allowedChannels = {
    "bot-games": 634327239361691658,
    "bot-commands": 629034637955694602,
    "bot-testing": 679701786189103106,
    "shitposting": 676713433567199232,
    "didier-testings": 689202224437395573,
    "freegames": 705745297908826113,
    "bot-commandsCOCGI": 714170653124722738,
    "generalZandbak": 728361031008780422,
    "freegamesZandbak": 728545397127118898,
    "spelenZandbak": 769248992957038612
}

creationDate = 1582243200

holidayAPIKey = "af4e1ebe-465d-4b93-a828-b95df18e6424"


class Live(Enum):
    CallOfCode = "626699611192688641"
    DidierPosting = "728361031008780422"
    General = "626699611813314561"


class Zandbak(Enum):
    CallOfCode = "728361030404538488"
    DidierPosting = "728361031008780422"
    General = "728361031008780422"
