from myproject import app,db,api
from flask_restful import Resource
from myproject.models import Player
from myproject.requester import battlelogpull, pull_player, update_player

#API endpoint to get all users
class AllUsers(Resource):
    def get(self):
        users = Player.query.all()
        return [user.json() for user in users]

#API endpoint for single user
class UserResource(Resource):
    def delete(self,playertag):
        user = Player.query.get(playertag)
        db.session.delete(user)
        db.session.commit()
        return {'note':'delete successful'}

    def get(self,playertag):
        playertag = playertag.upper()
        response = pull_player(playertag)
        return response
    
    def put(self,playertag):
        response = update_player(playertag)
        return response

#API endpoint for battlelog
class PlayerBattleLog(Resource):
    def put(self,playertag):
        log = battlelogpull(playertag)
        return log, 201


api.add_resource(AllUsers,'/api/all/users')
api.add_resource(UserResource, '/api/user/<string:playertag>')
api.add_resource(PlayerBattleLog, '/api/battles/<string:playertag>')


if __name__ == '__main__':
    app.run(debug=True)
