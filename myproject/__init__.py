import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
#cfrom myproject.config import dbpass

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
###Configuration for sqlite DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


###Configuration for Postgresql DB
#Create a Database called brawlstars, User: application, password stored in dbpass variable in config.py
#app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://application:{dbpass}@localhost:5432/brawlstars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
api = Api(app)