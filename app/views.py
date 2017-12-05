from flask import render_template, flash, redirect, request
from app import app
from .forms import Character
from config import races

# index view function suppressed for brevity

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    username = request.args.get('name', 'Lonk')
    race     = request.args.get('race', 'Nobody')
    if not race in races.keys():
        racestr = ' ( = '
        for i in range(len(race)//2):
            for k in races.keys():
                if k[:2] == race[i*2:i*2+2]:
                    racestr += races[k]['name'] + '-'
        racestr += 'hybrid)'
    return render_template('index.html',
                           title='Home',
                           user=username,
                           race=race.capitalize() + racestr)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Character()
    if form.validate_on_submit():
        if len(form.race.data) > 1:
            race = ''
            for x in form.race.data:
                race += x[:2]
        else:
            race = form.race.data[0]
        return redirect('/index?name={0}&race={1}'.format(str(form.name.data), race))
    return render_template('login.html', 
                           title='Create Player',
                           form=form)