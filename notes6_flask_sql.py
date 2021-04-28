#
# Python and flask can connect to variety of SQL database engines, including PostgreSQL, MySQL , SQLite etc.
# SQLite is a simple SQL database engine that comes with Flask and can handle all our needs.
#

# To connect Python, Flask and SQL together we will need an ORM ( Object Relational Mapper )
# ORM allows to directly use Python instead of SQL syntax to create, edit, update and delete from our database.
# The most common ORM for python is SQL alchemy.
#
# Flask-SQLAlchemy is an extension that allows for an easy connection of Flask with SQLAlchemy.
#   pip install Flask-SQLAlchemy

# To begin working with Databases, we'll do the following:
# - Setup SQLite database in a Flask app
# - Create a model in Flask app
# - Perform basic CRUD on our model
#

# Initializing the SQLite Databases.
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')      # This sets the path of the SQLite database file that will be saved on system.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # This is so that not every change is tracked by the OS.

db = SQLAlchemy(app)                # This initiates the database

#############################################

class Puppy(db.Model):

    # Manual table name choice. Python Creates a default database with the name of the class. To override that, we can use below:
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)         # These are the ways of creating column in the table.
    name = db.Column(db.Text)                           # This is a text column which allows text
    age = db.Column(db.Integer)                        # This is a integer column 

    def __init__(self,name,age):        # the initialization method. **NOTE the id will be auto-created for us later, so we don't add it here!
        self.name = name                # the name attribute for the object
        self.age = age                  # the age attribute.

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."        # This is the string representation of a puppy in the model
    

'''
#
# Creating tables:
'''

from basic import db,Puppy

db.create_all()         # Creates all the TABLES model, i.e DB TAble.

'''

#
# Now below talks about the ways of interacting with the DB objects. 
# Below are the methods provided by SQLAlchemy which are used to interact with the tables. 
#

'''
from BasicModelApp import db,Puppy

###########################
###### CREATE ############
#########################
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)            # db.session is the SQLAlchemy function. Since the Puppy class inherits the SQLAlchemy Model class, it has all its functions as well.
# db.session.add_all([my_puppy,other_puppy])    # This add_all function allows a list of puppy instances to be added at the same time.
db.session.commit()                 # This commits the changes done.

###########################
###### READ ##############
#########################
# Note lots of ORM filter options here.
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options
# all(), first(), get(), count(), paginate()

all_puppies = Puppy.query.all()         # list of all puppies in table
print(all_puppies)
print('\n')
# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print('\n')
# Filters
puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam)
print('\n')
###########################
###### UPDATE ############
#########################

# Grab your data, then modify it, then save the changes.
first_puppy = Puppy.query.get(1)            # This returns the query with id=1
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


###########################
###### DELETE ############
#########################
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)

'''

#
# :::: M I G R A T I O N S ::::
#
# Sometimes we would want to make adjustments to the Database model. 
# Upon making these changes, you will need to migrate these changes in order to update the database table.
# We can do this with --> FLASK MIGRATE
# pip install Flask-Migrate

# 4 main commands:

# 1. Set the FLASK_APP environment variable.
# linux -> export FLASK_APP=myapp.py
# Windows -> set FLASK_APP=myapp.py
#

# 2. flask db init
# this sets up the migration directory.

# 3. flask db migrate -m "some message"
# Sets up the migration file.

# 4. flask db upgrade
# Updates the database with the migration


# for all the instructions you can check -> migrations_instructions.txt

# Now before we go ahead, we also need to import the Migrate class in our main flask python file:

'''
from flask_migrate import Migrate  

app = Flask(__name__)

db = SQLAlchemy(app)  

Migrate (app,db)        # This links the Flask application (app) and the database we created db. WE need to add these lines in the main flask application file so that \
                        # the database file which is already created can be migrated easily if there are new columns added/removed.

'''
# Once the above changes are made in the main flask file and then we can migrate as below:
# Run below commands on the command prompt:

'''
set FLASK_APP=basic.py

flask db init       # This is required the first time. Susequent times this command is not required. This creates a directory.

flask db migrate -m "some message about the migration"

flask db upgrade

'''

# # # # # # # # # # # # # # # # # # # #
# :::: R E L A T I O N S H I P S :::: #
# # # # # # # # # # # # # # # # # # # #

# For larger projects there can be multiple models.
# These models may have a relationsip to each other, for example a Model for Puppies and another Model for their Owners.
#

# Primary Key : Unique Identifier Column

# Foreign Key : Primary Key in another table

# To Create a foreign ID we need to refer to a primary key of the other table.
# Example: 
'''
puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))    # Where puppies is the other table for which "id" is the primary key.

    # This is a one-to-many relationship
    # A puppy can have many toys

    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')
    
    
    # This is a one-to-one relationship
    # A puppy only has one owner, thus uselist is False.
    # Strong assumption of 1 dog per 1 owner and vice versa.
    
    owner = db.relationship('Owner',backref='puppy',uselist=False)
'''

# # # # # # # # # # # # # # # # # # # #
# # # # # :::: V I E W S :::: # # # # #
# # # # # # # # # # # # # # # # # # # #

# We've gone through enough to learn to make a real website !!
# Key Features:
# - Display Templates
# - Accept User information through forms
# - Save supplied infomration in Databases
# - Report back saved information
