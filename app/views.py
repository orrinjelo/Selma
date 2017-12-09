from flask import render_template, flash, redirect, request, session
from app import app
from .forms import Character
from config import races, classes, rooms, encounters
import random

# index view function suppressed for brevity

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    username = request.args.get('name', 'Lonk')
    race     = request.args.get('race', 'Nobody')
    clss     = request.args.get('clss', 'Nothing')

    if username != 'Lonk':
        player = {'username': username,
                  'race':     race,
                  'class':    clss,
                  'strength': 5,
                  'def':      0,
                  }

        session['playerinfo'] = player
    else:
        try:
            player   = session['playerinfo']
            username = player['username']
            race     = player['race']
            clss     = player['class']
        except:
            form = Character()
            if form.validate_on_submit():
                race = form.race.data
                clss = form.clss.data
                return redirect('/index?name={0}&race={1}&clss={2}'.format(str(form.name.data), race, clss))
            return render_template('login.html', 
                       title='Create Player',
                       form=form)        

    return render_template('index.html',
                           title='Home',
                           user=username,
                           race=race,
                           clss=clss)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Character()
    if form.validate_on_submit():
        race = form.race.data
        clss = form.clss.data
        return redirect('/index?name={0}&race={1}&clss={2}'.format(str(form.name.data), race, clss))
    return render_template('login.html', 
                           title='Create Player',
                           form=form)

@app.route('/adventure', methods=['GET', 'POST'])
def adventure():
    try:
        pi = session['playerinfo']
    except:
        return redirect('/index')
    roomname = request.args.get('room', 'void')
    pi['room'] = roomname

    session['playerinfo'] = pi
    r = random.randint(0,4) 
    if r == 2:
        return redirect('/encounter')

    room = rooms[roomname]
    return render_template('adventure.html',
                            roomname=room['name'],
                            roomdesc=room['description'],
                            exits=room['exits'],
                            image=room['image'])

@app.route('/encounter', methods=['GET', 'POST'])
def encounter():
    def they_attack():
        r = random.randint(0,len(session['encounterinfo']['enemy']['attack'])-1)
        flash(session['encounterinfo']['enemy']['attack'][r])
        r = random.randint(0,session['encounterinfo']['enemy']['strength'])
        flash('It does {0} damage to you!'.format(r))

    try:
        pi = session['playerinfo']
    except:
        return redirect('/index')

    room = rooms[pi['room']]

    action = request.args.get('action', 'none')
    print(action)
    if action == 'none':
        r = random.randint(0,len(encounters)-1)
        print(r)
        creature = encounters[list(encounters.keys())[r]]

        flash('You encounter a {0}!'.format(creature['name']) )
        flash('{0}'.format(creature['description']) )

        session['encounterinfo'] = { 'enemy': creature,
                                     'health': creature['hp']
                                   }
    elif action == 'attack':
        attack_val = random.randint(0,pi['strength'])
        flash('You {0}!'.format(classes[pi['class']]['attack']))
        flash('You do {0} points of damage!'.format(attack_val))
        session['encounterinfo']['health'] -= attack_val
        if session['encounterinfo']['health'] <= 0:
            flash(session['encounterinfo']['enemy']['death'])
            return redirect('/adventure?room={0}'.format(pi['room']))
        else:
            they_attack()
    elif action == 'run':
        a, b = random.randint(0,races[pi['race']]['landspeed']), random.randint(0,session['encounterinfo']['enemy']['speed'])
        if a > b:
            flash('You manage to run away!')
            return redirect('/adventure?room={0}'.format(pi['room']))
        else:
            flash('You fail to escape!')
            they_attack()

    return render_template('adventure.html',
                            roomname=room['name'],
                            roomdesc=room['description'],
                            thisroom=pi['room'],
                            thispage='encounter',
                            actions=[('attack','attack!'),('run','run away!'),('useinv','use inventory item'),],
                            # exits=room['exits'],
                            image=room['image'])