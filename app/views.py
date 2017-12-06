from flask import render_template, flash, redirect, request, session
from app import app
from .forms import Character
from config import races, classes, rooms

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
                  'class':    clss
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
                if len(form.race.data) > 1:
                    race = ''
                    for x in form.race.data:
                        race += x[:2]
                else:
                    race = form.race.data[0]
                if len(form.clss.data) > 1:
                    clss = ''
                    for x in form.clss.data:
                        clss += x[:2]
                else:
                    clss = form.clss.data[0]
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
        if len(form.race.data) > 1:
            race = ''
            for x in form.race.data:
                race += x[:2]
        else:
            race = form.race.data[0]
        if len(form.clss.data) > 1:
            clss = ''
            for x in form.clss.data:
                clss += x[:2]
        else:
            clss = form.clss.data[0]
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
    # flashmsg = 
    room = rooms[roomname]
    return render_template('adventure.html',
                            roomname=room['name'],
                            roomdesc=room['description'],
                            exits=room['exits'],
                            image=room['image'])