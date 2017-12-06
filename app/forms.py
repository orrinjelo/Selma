from flask_wtf import Form
from wtforms import SelectMultipleField, BooleanField, StringField, widgets, RadioField
from wtforms.validators import DataRequired
from config import races, classes

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Character(Form):
    name    = StringField('name', validators=[DataRequired()])
    race    = RadioField('race',  validators=[DataRequired()], choices=[(k, races[k]['name'])   for k in races.keys()])
    clss    = RadioField('class', validators=[DataRequired()], choices=[(k, classes[k]['name']) for k in classes.keys()])
