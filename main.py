from flask import Flask, request, render_template, render_response
from tinydb import TinyDB, where, Query

app = Flask(__name__)

from wtforms import FlaskForm, BooleanField, StringField, validators
from wtforms.widgets import TextInput, PasswordInput

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

@app.route('/', methods=['GET','POST'])
def login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.save()
        redirect('register')
    return render_template('register', form=form)
