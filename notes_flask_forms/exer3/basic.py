from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class simpleForm(FlaskForm):

    breed = StringField('What breed are you ?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form = simpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash("You just changed the breed to : " + session['breed'])
        return redirect(url_for('index'))
    
    return render_template('index.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)



