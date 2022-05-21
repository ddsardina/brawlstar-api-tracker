from myproject import db
from myproject import app

class Player(db.Model):

    __tablename__ = 'players'

    playertag = db.Column(db.String(50), primary_key=True)
    playername = db.Column(db.String(25))
    trophies = db.Column(db.Integer)

    def __init__(self,playertag,playername,trophies):
        self.playertag = playertag
        self.playername = playername
        self.trophies = trophies

    def json(self):
        return {
            "name": self.playername,
            "playertag": self.playertag,
            "trophies": self.trophies
            }
    
    def __repr__(self):
        return f"Tag is {self.playertag}, Name is {self.playername} and trophy count is {self.trophies}"

with app.app_context():
    db.create_all()