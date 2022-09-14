from datetime import datetime
from pymongo import MongoClient
import certifi
import requests
from bson.objectid import ObjectId
from myproject.config import key
from myproject import db
from myproject.models import BattleLog
from myproject.config import mongodburi


cert = certifi.where()
client = MongoClient(mongodburi, tlsCAFile=cert)
MDB = client.brawlstar

#battleCollection = MDB.battles
#playertag = "PCURU80V"


#r = requests.get(f'https://api.brawlstars.com/v1/players/%23{playertag}/battlelog',headers={'Authorization': key}).json()


def battlelogpull(playertag):
    collName = f'battles{playertag}'
    battleCollection = MDB[collName]
    newBattles = 0
    r = requests.get(f'https://api.brawlstars.com/v1/players/%23{playertag}/battlelog',headers={'Authorization': key}).json()
    for num in reversed(range(0,25)):
        try:
            if r["items"][num]['battle']['type'] == 'soloRanked':
                battletime = r["items"][num]['battleTime']
                timeQuery = {"battleTime": battletime}
                battleExist = battleCollection.find(timeQuery)
                exist = len(list(battleExist))
                if exist == 0:
                    gamemode = r["items"][num]['battle']['mode']
                    map = r["items"][num]['event']['map']
                    result = r["items"][num]['battle']['result']
                    duration = r["items"][num]['battle']['duration']
                    initteams = r["items"][num]['battle']['teams']
                    teams = []
                    for team in initteams:
                        teamList = []
                        for player in team:
                            teamList.append(player['brawler']['name'])
                            if player['tag'] == f'#{playertag}':
                                brawler = (player['brawler']['name'])
                        teams.append(teamList)
                    battle = {
                        "battleTime": battletime,
                        "status": "New",
                        "mode": gamemode,
                        "map": map,
                        "result": result,
                        "duration": duration,
                        "playerBrawler": brawler,
                        "teams": teams,
                        "fullTeam": initteams
                    } 
                    battleCollection.insert_one(battle)
                    newBattles += 1
        except (KeyError, NameError, IndexError):
            continue
    return {'New Battles': newBattles}

def battlesToDB(playertag):
    commitedBattles = 0
    collName = f'battles{playertag}'
    battleCollection = MDB[collName]
    battlequery = {"status": "New"}
    newBattles = battleCollection.find(battlequery)
    battles = []
    for battle in newBattles:
        battles.append(battle)
    for num in range(len(battles)):
        print(battles[num]["battleTime"])
        try:
            if (
                battles[num]["result"] == battles[num+1]["result"] and 
                battles[num]["fullTeam"] == battles[num+1]["fullTeam"] and
                battles[num]["status"] == "New"
            ):
                battletime = battles[num]["battleTime"]
                print(battletime)
                match1 = battles[num]["result"]
                print(f'Two Game M1: {match1}')
                match2 = battles[num+1]["result"]
                print(f'Two Game M2: {match2}')
                result = match1
                match1id = str(battles[num].get('_id'))
                match2id = str(battles[num+1].get('_id'))
                brawler = battles[num]["playerBrawler"]
                map = battles[num]["map"]
                mode = battles[num]["mode"]
                newBattle = BattleLog(
                    battletime=battletime,
                    match1=match1,
                    match2=match2,
                    match3=None,
                    match1id=match1id,
                    match2id=match2id,
                    match3id=None,
                    result=result,
                    brawler=brawler,
                    map=map,
                    gamemode=mode,
                    player_id=playertag
                )
                db.session.add(newBattle)
                db.session.commit()
                _id1 = ObjectId(match1id)
                _id2 = ObjectId(match2id)
                updates = {"$set": {'status': "Reviewed"}}
                battleCollection.update_one({"_id":_id1}, updates)
                battleCollection.update_one({"_id":_id2}, updates)
                battles[num]['status'] = "Reviewed"
                battles[num+1]['status'] = "Reviewed"
                print(f'GameMode: {mode}, Map: {map}, Brawler: {brawler}, Result: {result}')
                commitedBattles += 1
            elif battles[num]["fullTeam"] == battles[num+2]["fullTeam"]:
                battletime = battles[num]["battleTime"]
                match1 = battles[num]["result"]
                print(f'Three Game M1: {match1}')
                match2 = battles[num+1]["result"]
                print(f'Three Game M2: {match2}')
                match3 = battles[num+2]["result"]
                print(f'Three Game M3: {match3}')
                result = match3
                match1id = str(battles[num].get('_id'))
                match2id = str(battles[num+1].get('_id'))
                match3id = str(battles[num+2].get('_id'))
                brawler = battles[num]["playerBrawler"]
                map = battles[num]["map"]
                mode = battles[num]["mode"]
                newBattle = BattleLog(
                    battletime=battletime,
                    match1=match1,
                    match2=match2,
                    match3=match3,
                    match1id=match1id,
                    match2id=match2id,
                    match3id=match3id,
                    result=result,
                    brawler=brawler,
                    map=map,
                    gamemode=mode,
                    player_id=playertag
                )
                db.session.add(newBattle)
                db.session.commit()
                _id1 = ObjectId(match1id)
                _id2 = ObjectId(match2id)
                _id3 = ObjectId(match3id)
                updates = {"$set": {'status': "Reviewed"}}
                battleCollection.update_one({"_id":_id1}, updates)
                battleCollection.update_one({"_id":_id2}, updates)
                battleCollection.update_one({"_id":_id3}, updates)
                battles[num]["status"] = "Reviewed"
                battles[num+1]["status"] = "Reviewed"
                battles[num+2]["status"] = "Reviewed"
                print(f'GameMode: {mode}, Map: {map}, Brawler: {brawler}, Result: {result}, Three match game')
                commitedBattles += 1
        except (KeyError, IndexError):
            continue
    return {'Commited Battles': commitedBattles}
