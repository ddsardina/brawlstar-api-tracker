import requests
import os
from myproject.models import Player
from myproject.config import key


url = 'https://api.brawlstars.com/v1/players/%23'
auth_headers = {'Authorization': key}

#test Request
#r = requests.get('https://api.brawlstars.com/v1/players/%23PCURU80V',headers={'Authorization': key}).json()
#Test User: PCURU80V

#All Brawlstar Playertags begin with '#' the hashtag is represented by the unicode %23


#Function Gets Status Code from Brawlstar API and then checks if playertag is in DB
def responsecode(playertag):
    player_url = url + playertag
    response_code = requests.get(player_url,headers=auth_headers).status_code
    if response_code == 200:
        if Player.query.get(playertag):
            #print("player found in Db")
            return 200
        else:
            #print("No Player found")
            return 201
    else:
        print("Invalid Key")
    

#Returns the name of the Player
def player_name(playertag):
    player_url = url + playertag
    response = requests.get(player_url,headers=auth_headers).json()
    name = response['name']
    return name


#Returns the Trophy count of the brawler
def player_trophies(id):
    player_url = url + id
    response = requests.get(player_url,headers=auth_headers).json()
    trophies = response['trophies']
    return int(trophies)



