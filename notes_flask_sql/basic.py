import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')      # This sets the path of the SQLite database file that will be saved on system.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # This is so that not every change is tracked by the OS.

db = SQLAlchemy(app)                # This initiates the database

Migrate (app,db)
#############################################

class Puppy(db.Model):

    # Manual table name choice. Python Creates a default database with the name of the class. To override that, we can use below:
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)         
    name = db.Column(db.Text)                           
    age = db.Column(db.Integer)                         

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."