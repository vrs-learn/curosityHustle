#
# Flask App Basics
#

'''
from flask import Flask             # from flask package importing the Flask Class.
app = Flask(__name__)               # This is the object of the Flask App that is created. The __name__ is the basically the name of the module where the file remains.

@app.route('/')                     # THis is defining in the web application, with route '/' return the index function.
def index():                         # this is a function thats returning an html code that says, Hello Puppy.
    return '<h1> Hello Puppy !</h1>'

if __name__ == '__main__':          # This is just verifying if the script is being triggered directly.
    app.run()                        # This is running the application

'''

#
# Adding multiple routes:
#
# By adding additonal @app.route('/target_page') -> we can add more functions that will be called when the webpage with the same URL is hit.

#
# Dyamic Routing.
# There can be use cases when the route has to be dyanmic, like user profile page etc.
#
# This can be done as follows:

'''
@app.route('/some_page/<name>')
def other_page(name):
    # Later we will see how to use this parameter with templates !!
    return 'User: {}'.format(name)

'''

'''
from flask import Flask            
app = Flask(__name__)               

@app.route('/')                     
def index():                        
    return '<h1> Hello Puppy !</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1> This is a page for {} </h1>".format(name.upper())

if __name__ == '__main__':          
    app.run()                       

'''

#
# Enabling Debug.
# debug=True in the app.run() 
# So it becomes : app.run(debug=True)
#
# On the webpage, when running in debug, if there is an error, there is a shell icon which allows you to open up the shell and allow you to run the commands to check what the error was.
# To open the shell, you need a pin which is displayed while running the application itself.
#
# ** NOTE : Make sure to remove the debug when deplying to production.
#
