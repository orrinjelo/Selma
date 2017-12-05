from flask_wtf import Form
from wtforms import SelectMultipleField, BooleanField, StringField, widgets
from wtforms.validators import DataRequired
from config import races

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Character(Form):
    name  = StringField('name', validators=[DataRequired()])
    race  = MultiCheckboxField('race', validators=[DataRequired()], choices=[(k, races[k]['name']) for k in races.keys()])
