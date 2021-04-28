# forms.py
#

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to Remove:")
    submit = SubmitField('Remove Puppy')

class AddOwner(FlaskForm):
    name = StringField("Name of Owner: ")
    puppy_id = StringField("Id of Puppy: ")
    submit = SubmitField("Add Owner")

