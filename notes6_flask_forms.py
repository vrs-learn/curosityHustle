#
# Forms with Flask
#
# We can use flask_wtf and wtforms packages to quickly create forms from our flask python scripts.
#
# First lets discuss the main components to creating a form.
#
# Below steps are required:
# Configure a secret key for security
# Createa a WTForm Class
#   Create fields for each part of the form
# Setup a view function
#   Add methods=['GET','POST']
#   Create an instance of Form Class
#   Handle form submission
#

# First -> WE need to import FlaskForm from flask_wtf modulle.
# Second -> WE need to import fields which we need to use in the form by using as below:
'''
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
'''

# This line is required for setting a secret key. 
'''
app.config['SECRET_KEY'] = 'mysecretkey'
'''
# Then we create our own class that extends the FlaskForm class as below.
# In this we create two attributes of the class that utilize the Stringfield and Submitfield types of field for the form.
'''
class InfoForm(FlaskForm):
    #This general class gets a lot of form about puppies.
    #Mainly a way to go through many of the WTForms Fields.

    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')

'''
#
# Now for this example, we create a new route which allows 'GET' and 'POST' methods.
# Then we initiate a form variable of InfoForm Class, that we created before.
# Now for this example we use the same page which is displayed again and again with the information that we get from the user.
# So we check the values 
#
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    # Set the breed to a boolean False.
    # So we can use it in an if statement in the html.
    breed = False
    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        breed = form.breed.data
        # Reset the form's breed data to be False
        form.breed.data = ''
    return render_template('00-home.html', form=form, breed=breed)
'''
#
# Inside the html code, we have checks that perform check for the first time that the values are available or not.
# then the form tag is used and then the python code is used to create the fields and submit buttons.
# 
'''
<p>
{% if breed %}
  The breed you entered is {{breed}}.
  You can update it in the form below:
{% else %}
  Please enter your breed in the form below:
{% endif %}
</p>

<form method="POST">
    {# This hidden_tag is a CSRF security feature. #}
    {{ form.hidden_tag() }}
    {{ form.breed.label }} {{ form.breed(class='some-css-class') }}
    {{ form.submit() }}
</form>
'''

############################################################
################## :::: Form Fields :::: ###################
############################################################
# 
# Every possible HTML form field has a corresponding wtforms class you can import
#
# wtforms also has validators you can easily insert
# Validators can perform checks on the form data, such as requiring a field to be filled.
#
# Flasks's Session object is used to grab the information provided in the form and pass it to another template.
#
# Benefit of using a session is , you don't need to pass on each of the variables to the render_template when calling the html page.
# 
# For below example, we imported following from flask:
# 
'''
from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    # This general class gets a lot of form about puppies.
    # Mainly a way to go through many of the WTForms Fields.

    breed = StringField('What breed are you?',validators=[DataRequired()])
    neutered  = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick Your Favorite Food:',
                          choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                   ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))      # Notice how we donot use render_template. Instead we  use redirect with url_for. Its similar how we use url_for in 
                                                  # html templates. We provide the function name which we 


    return render_template('01-home.html', form=form) # This is first time the URL is hit when the form is not filled. At this time the page home.html is called.
                                                      #  And form is also passed.  This form object is then called in the html page.


@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')
'''
#
# The form when passed to the html page, is rendered and used to present the fields as below:
#
'''
<form  method="POST">
    {# This hidden_tag is a CSRF security feature. #}
    {{ form.hidden_tag() }}
    {{ form.breed.label }} {{form.breed}}
    <br>
    {{ form.neutered.label}} {{form.neutered}}
    <br>
    {{form.food_choice.label}}{{form.food_choice}}
    <br>
    {{form.mood.label}}{{form.mood}}
    <br>
    Any other feedback?
    <br>
    {{form.feedback}}
   <br>
    {{ form.submit() }}
</form>
'''

