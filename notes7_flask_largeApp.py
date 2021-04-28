# For large applications, it makes more sense to separate portions of the application into their own files
# - models.py       - forms.py      - views.py

# For even larger applications it begins to make sense to refactor the files into separate components
# like - Forms, Views, Templates for each major component.

# We will split the app.py into separate components for each major aspect:
# Create two folders - Puppies and Owners
# Each of the directory will have forms.py, views.py and templates

# We will also be able to use the "blueprints" library to connect these separate modular components to our main app.py file.
# Keep in mind, we're still keeping app.py, it will just be referencing these sub-components.
'''
It will look something like below:

├───app.py # main app.py file to be called to start server for web app
├───requirements.txt # File of pip install statements for your app
├───migrations # folder created for migrations by calling
├───myproject # main project folder, sub-components will be in separate folders
│   │   data.sqlite
│   │   models.py
│   │   __init__.py
│   │
│   ├───owners
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───templates
│   │      └───owners
│   │             add_owner.html
│   │   
│   │
│   ├───puppies
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───templates
│   │   │   └───puppies
│   │   │           add.html
│   │   │           delete.html
│   │   │           list.html
│   │
│   ├───static # Where you store your CSS, JS, Images, Fonts, etc...
│   ├───templates
│          base.html
│          home.html

'''
#######################################################################
#######################################################################
## <<<  For DETAILS CHECK THE 06-Larger-Flask-Applications Folder >>> ##
#######################################################################
#######################################################################
#
# Now since both puppies and owners are going to have same views , we will be using blueprint to handle it.
#
# Blueprints register a url_prefix for each of the views
# /owners/add
# /puppies/add

# For this restructuring project, we are going to do:
# - Restructuring the project folders
# - Adding in Blueprints
# - Registering Blueprints in __init__.py
#

# Inside owners and puppies folder we create views.py which have below blueprints :
'''
from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners',                              
                              __name__,
                              template_folder='templates/owners')   # This is required to create the blueprint. First argument is the name of the blueprint
                                                                    # This is 

@owners_blueprint.route('/add', methods=['GET', 'POST'])            # Now when we have to create a decorator, we use the Blueprint variable 
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html',form=form)

'''
#
# Once the blueprints is created for all the sections, we need to register it in main project's __init__.py file.
#
'''
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint,url_prefix="/owners")
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
'''