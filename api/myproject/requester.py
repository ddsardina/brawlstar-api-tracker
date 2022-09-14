import requests
from myproject import db
from myproject.models import Player
from myproject.config import key


url = 'https://api.brawlstars.com/v1/players/%23'
auth_headers = {'Authorization': key}

#test Request
#r = requests.get('https://api.brawlstars.com/v1/players/%23PCURU80V',headers={'Authorization': key}).json()
#Test User: PCURU80V

#All Brawlstar Playertags begin with '#' the hashtag is represented by the unicode %23


# Validates That the Player Exist By Checking the BrawlStars API
# After Validating Player, It Will Check if Player is in DB
def responsecode(playertag):
    player_url = url + playertag
    response_code = requests.get(player_url,headers=auth_headers).status_code
    if response_code == 200:
        if Player.query.get(playertag):
            print("player found in Db")
            return 200
        else:
            print("No Player found")
            return 201
    else:
        print("Invalid Key")
    

# Will Pull Player from DB if Already There
# Will Pull Stats from BrawlStars API if not
def pull_player(playertag):
    internalResponse = responsecode(playertag)
    if internalResponse == 200:
        player = Player.query.get(playertag)
        print("player in Db")
        return player.json(), 200
    elif internalResponse == 201:
        print("player does not exist in Db")
        stats = player_stats(playertag)
        playername = stats['name']
        trophies = stats['trophies']
        level = stats['level']
        victories3v3 = stats['victories3v3']
        victoriesSolo = stats['victoriesSolo']
        victoriesDuo = stats['victoriesDuo']
        club = stats['club']
        new_player = Player(playertag,playername,trophies,level,victories3v3,victoriesSolo,victoriesDuo,club)
        db.session.add(new_player)
        db.session.commit()
        print(new_player)
        return new_player.json(), 201
    else:
        return {'Info':'Player Tag Invalid'}, 404

#Repulls Player Info
def update_player(playertag):
    stats = player_stats(playertag)
    player = Player.query.get(playertag)
    player.trophies = stats['trophies']
    player.level = stats['level']
    player.victories3v3 = stats['victories3v3']
    player.victoriesSolo = stats['victoriesSolo']
    player.victoriesDuo = stats['victoriesDuo']
    player.club = stats['club']
    print("Stats Repulled")
    db.session.commit()
    return player.json(), 200

# Function used by pull_player & update_player
# Makes request and formats
def player_stats(playertag):
    player_url = url + playertag
    response = requests.get(player_url,headers=auth_headers).json()
    name = response['name']
    trophies = int(response['trophies'])
    level = int(response['expLevel'])
    victories3v3 = int(response['3vs3Victories'])
    victoriesSolo = int(response['soloVictories'])
    victoriesDuo = int(response['duoVictories'])
    try:
        club = response['club']['name']
    except(KeyError):
        club = None
    stats = {
        'name': name,
        'trophies': trophies,
        'level': level,
        'victories3v3': victories3v3,
        'victoriesSolo': victoriesSolo,
        'victoriesDuo': victoriesDuo,
        'club': club
    }
    return stats
