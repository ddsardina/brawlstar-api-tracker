from myproject import app,db,api
from flask import render_template, url_for, redirect
from flask_restful import Resource
from myproject.forms import PlayerIdForm, RefreshForm
from myproject.models import Player
from myproject.requester import responsecode, player_name, player_trophies

#API endpoint to get all users
class AllUsers(Resource):
    def get(self):
        users = Player.query.all()
        return [user.json() for user in users]

#API endpoint to delete a user
class UserResource(Resource):
    def delete(self,playertag):

        user = Player.query.get(playertag)
        db.session.delete(user)
        db.session.commit()

        return {'note':'delete successful'}

api.add_resource(AllUsers,'/all/users')
api.add_resource(UserResource, '/user/<string:playertag>')


#Checks if the player tag matches a user in brawstars
#Then checks if the user is in the DB, or adds the user if not in the DB
@app.route('/',methods=['GET','POST'])
def home():
    form = PlayerIdForm()
    if form.validate_on_submit():
        playertag = form.player_id.data.upper()
        if responsecode(playertag) == 200:
            print("player in Db")
            return redirect(url_for('player_stats', playertag=playertag))
        elif responsecode(playertag) == 201:
            print("player does not exist")
            name = player_name(playertag)
            trophies = player_trophies(playertag)
            new_player = Player(playertag,name,trophies)
            db.session.add(new_player)
            db.session.commit()
            print(new_player)
            return redirect(url_for('player_stats', playertag=playertag))
        else:
            render_template('error.html')
    return render_template('home.html',form=form)

#Displays the user's stats and will repull stats upon refresh
@app.route('/user/<playertag>',methods=['GET','POST'])
def player_stats(playertag):
    player = Player.query.get(playertag)
    print(player)
    tag = player.playertag
    name = player.playername
    trophies = player.trophies
    db.session.commit()
    form = RefreshForm()
    if form.validate_on_submit():
        player.name = player_name(playertag)
        player.trophies = player_trophies(playertag)
        print(player)
        print("Stats Repulled")
        db.session.commit()
        return redirect(url_for('player_stats', playertag=playertag))

    return render_template('stats.html',tag=tag,name=name,trophies=trophies,form=form)



if __name__ == '__main__':
    app.run(debug=True)
