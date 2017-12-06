WTF_CSRF_ENABLED = True
SECRET_KEY = 'osiris55'

races = {
    'squid': {
        'name' : 'Squid',
        'attack' : 'squirt paint',
        'landspeed': 1,
        'waterspeed': 5,
        'airspeed': 0,
    },
    'penguin': {
        'name' : 'Penguin',
        'attack' : 'launch a nuclear warhead',
        'landspeed': 2,
        'waterspeed': 4,
        'airspeed': 0,
    },
    'ditto': {
        'name' : 'Ditto',
        'attack' : 'mimick',
        'landspeed': 3,
        'waterspeed': 2,
        'airspeed': 1,
    },
    'slothmare': {
        'name' : 'Slothmare',
        'attack' : 'slaughthmrrrgle',
        'landspeed': 1,
        'waterspeed': 1,
        'airspeed': 4,
    },
}

classes = {
    'fancypants': {
        'name' : 'Fancy Pants',
        'attack' : 'flashy-triple-reverse-hurricane-kick',
    },
    'manahands': {
        'name' : 'Manahands',
        'attack' : 'magicalize a spell'
    },
    'whippersnapper': {
        'name' : 'Whippersnapper',
        'attack' : 'whine about homework'
    },
    'gifspammer': {
        'name' : 'Gif-Spammer',
        'attack' : 'spam really bad memes'
    },
}

rooms = {
    'void': {
        'name': 'The Void',
        'description': 'You are surrounded by whiteness. Some would find this disorienting, considering there is no floor, no walls, and no ceiling.',
        'exits': [('farm','wake up')],
        'image': None,
    },
    'farm': {
        'name': 'The Farm',
        'description': 'The smell of cow manure drifts into your nostrils.  You look around, finding yourself in the middle of a field filled with spherical cows.\nBeyond the green grassy meadows of the farm, you can see majestic purple mountains to the north, a city to the east, a thick forest to the south, and sand dunes to the west.',
        'exits': [('country road','north'),('cobbled path','east'),('dirt path','south'),('sand dune 1', 'west')],
        'image': 'spherical-cows.jpg',
    },
    'country road': {
        'name': 'Country Road',
        'description': 'It\'s a lovely road, some would say.  Aged oaks line the sides of this road, almost ripe with oakfruit. The breeze rustles through their leaves.  Somewhere to the north are mountains, and the perfume of spherical cow dung wafts in from the south.',
        'exits': [('farm','south'),('country road 2','north')],
        'image': 'country-road.jpg',
    },
    'country road 2': {
        'name': 'Country Road',
        'description': 'It\'s a lovely road, some would say.  Aged oaks line the sides of this road, almost ripe with oakfruit. The breeze rustles through their leaves.  Somewhere to the north are mountains, to the south are fields.',
        'exits': [('country road','south'),('mountain foothills','north')],
        'image': 'country-road.jpg',
    },
    'mountain foothills': {
        'name': 'Mountain Foothills',
        'description': 'The paths are a bit more overgrown here and the way becomes a bit more difficult to climb.  All before you are monstrous peaks covered in snow.  You spot a narrow canyon not too far from here to the northwest.  There is a well-traveled road to the south.',
        'exits': [('country road 2','south'),('mountain side','north'), ('canyon', 'northwest')],
        'image': None,
    },
}

encounters = {
    'booger': {
        'name': 'Booger',
        'description': 'This is a tiny booger.',
        'image': None,
        'hp': 1,
        'speed': 0,
        'attack': ['It flicks itself at you.',],
        'death': 'It gets lost somewhere in the dust...oh well.'
    },
    'spooder': {
        'name': 'Spooder',
        'description': 'This is a tiny spooder.  It is pretty spoopy.',
        'image': None,
        'hp': 2,
        'speed': 4,
        'attack': ['It bites you with its widdle fangs.',],
        'death': 'It got squooshed.'
    },
    'mongoose': {
        'name': 'Mongoose',
        'description': 'Mongeese are pretty feisty, especially if you steal their oatmeal.  This one thinks you stole his.',
        'image': None,
        'hp': 5,
        'speed': 3,
        'attack': ['After hissing, it chomps down on your toes.',],
        'death': 'Poor mongoose.  It died without its oatmeal.  You monster.'
    },
    'cadenbot': {
    },
    'dangerfloof': {
    },
    'dangernoodle': {
    },
    'ghost': {
    },
    'catfish': {
    },
    'ghost': {
    },
    'jelobot': {
    },
    'pig': {
    },
    'frog': {
    },
}

bosses = {
    'buttermelon': {
        'name': 'Buttermelon',
        'description': 'Yellow, curved, and fruity, just like your nightmares.  Beware the buttermelon!',
        'image': None,
        'hp': 100,
        'speed': 5,
        'damage': 50,
        'attack': ['It starts peeling itself, exposing the mushy fruit to your eyes!', 
                   'It reveals buttermelon-shuriken, and throws several in your direction',
                   'In a poof of smoke, it vanishes before your eyes!  Before you can react, it appears behind you with a sharp dagger at your back.',
                   'It does a jump-spinning-reverse-crescent-kick to your head with its stem!',
                  ],
        'death': 'After a fierce battle, the buttermelon flops over on its side.  Its insides are mushy, and its peel starts turning brown.'
    },
    'handicorn': {
        'name': 'Handicorn',
        'description': 'A giant disembodied hand wearing the parts of a handicorn costume stands majestically before you, wielding a large kitchen knife.',
        'image': None,
        'hp': 80,
        'speed': 4,
        'damage': 25,
        'attack': ['It rams you with its pretty purple plastic horn!', 
                   'It chops you with its kitchen knife!',
                   'It tramples you with its pretty purple hooves!',
                   'It farts glitter in your general direction.',
                  ],
        'death': 'Beat to the point of exhaustion, the handicorn sways a bit before biting the dust.  It lives no more.'
    },
    'icarus': {
        'name': 'Icarus',
        'description': 'A rather clever stupid bot, some kind of cross between a giant robot bird and a phoenix.',
        'image': None,
        'hp': 120,
        'speed': 2,
        'damage': 80,
        'attack': ['It bans you from the chat!', 
                   'It gives you a bad !react gif!',
                   'It confuses you with a random !acronym!',
                   'It reveals a !spoiler for you that you didn\'t want to see!',
                  ],
        'death': 'It encounters some bad javascript code and crashes.  No more Icarus.'
    },
}

items = {
    'cornmuffin': {
        'name': 'Cornmuffin',
        'type': 'consumable',
        'value': 5,
        'action': 'You stuff the cornmuffin in yo\' face!',
    },
    'fry sauce': {
        'name': 'Fry Sauce',
        'type': 'consumable',
        'value': 10,
        'action': 'You drink down your favorite non-Newtonian substance.',
    },
    'tasty ink': {
        'name': 'Tasty Ink',
        'type': 'consumable',
        'value': 15,
        'action': 'You aren\'t sure whether it is edible, but you try anyway.',
    },
    'potato': {
        'name': 'Cornmuffin',
        'type': 'consumable',
        'value': 20,
        'action': 'Boil \'em, mash \'em, stick \'em in a stew.',
    },
    'propeller hat': {
        'name': 'Propeller Hat',
        'type': 'armor',
        'value': 1,
        'action': 'Doesn\'t do much, but it looks cool.',
    },
}