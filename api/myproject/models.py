from sqlalchemy import ForeignKey
from myproject import db
from myproject import app

class Player(db.Model):

    __tablename__ = 'players'

    playertag = db.Column(db.String(50), primary_key=True)
    playername = db.Column(db.String(25))
    trophies = db.Column(db.Integer)
    level = db.Column(db.Integer)
    victories3v3 = db.Column(db.Integer)
    victoriesSolo = db.Column(db.Integer)
    victoriesDuo = db.Column(db.Integer)
    club = db.Column(db.String(25))
    battles = db.relationship("BattleLog")

    def __init__(self,playertag,playername,trophies,level,victories3v3,victoriesSolo,victoriesDuo,club):
        self.playertag = playertag
        self.playername = playername
        self.trophies = trophies
        self.level = level
        self.victories3v3 = victories3v3
        self.victoriesSolo = victoriesSolo
        self.victoriesDuo = victoriesDuo
        self.club = club


    def json(self):
        return {
            "name": self.playername,
            "playertag": self.playertag,
            "trophies": self.trophies,
            "level": self.level,
            "victories3v3": self.victories3v3,
            "victoriesSolo": self.victoriesSolo,
            "victoriesDuo": self.victoriesDuo,
            "club": self.club
            }
    
    def jsonblog(self):
        battles = ""
        for battle in self.battles:
            battles += {
            "brawler": battle.brawler,
            "result": battle.result
            },
        return battles
    
    def __repr__(self):
        return f"Tag is {self.playertag}, Name is {self.playername} and trophy count is {self.trophies}"


class BattleLog(db.Model):

    __tablename__ = 'battlelogs'

    id = db.Column(db.Integer,primary_key=True)
    battletime = db.Column(db.String(25))
    match1 = db.Column(db.String(10))
    match2 = db.Column(db.String(10))
    match3 = db.Column(db.String(10))
    result = db.Column(db.String(10))
    brawler = db.Column(db.String(25))
    map = db.Column(db.String(50))
    gamemode = db.Column(db.String(25))
    player_id = db.Column(db.String,ForeignKey("players.playertag"))

    def __init__(self,battletime,match1,match2,match3,result,brawler,map,gamemode,player_id):
        self.battletime = battletime
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.result = result
        self.brawler = brawler
        self.map = map
        self.gamemode = gamemode
        self.player_id = player_id


with app.app_context():
    db.create_all()