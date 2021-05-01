#
# REST API
# 
# Representational State Transfer
#
# Process to learn :
# - Learn about POSTMAN Testing Tool
# - Send a json object with REST
# - Learn basic REST commands
# - Implement Authentication
# - Implement simple example of a Restful Flask Web application
#
'''
Create  POST    Create a new object
Read    GET     Read information about object (or multiple objects)
Update  PUT     Update information about existing object
Delete  DELETE  Delete an object
'''

# To use rest api, we install a new library
# pip install Flask-Restful
'''
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):     # we inherit Resource into the class. and then we create get, post etc methods.
    
    def get(self):                  # This is for the GET request. We can call the application when running and call the GET request and will get the response from this function.
        return {'hello':'world'}


api.add_resource(HelloWorld,'/')
    
if __name__ == '__main__':
    app.run(debug=True)
'''

######################
## CRUD with API
######################


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

puppies = []

class Puppy(Resource):

    def get(self,name):
        for pup in puppies:
            if pup['name'] == name:
                return {'name': puppies[name]}
        
        return {'name': None}, 404

    def post(self,name):
        pup = {'name': name}
        puppies.append(pup)
        return pup
    
    def delete(self,name):
        for no,pup in enumerate(puppies):
            if pup['name'] == name:
                puppies.pop(no)
                return {'note':"successfully deleted"}
        
        return {'note':'No such puppy found.'}, 404


class allpuppies(Resource):

    def get(self):
        return {'puppies': puppies}


api.add_resource(Puppy,'/puppy/<string:name>')
api.add_resource(allpuppies,'/allpuppies')


if __name__ == '__main__':
    app.run(debug=True)

#####################
#### Flask JWT (JSON Web Token) Library
#####################
#
# We can use the Flask - JWT library to require authorization before being able to create a REST API all.
# Users will need to provide a username and password to an authentication page, then they will receive a key they can attach to their calls.
#
# For using the JWT,we import it as below and create a new variable for JWT as below:
# 
'''
from flask_jwt import JWT ,jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)


class AllNames(Resource):

    @jwt_required()             # This needs to be added in the funtions where the authentication is requried.
    def get(self):
        # return all the puppies :)
        return {'puppies': puppies}

'''