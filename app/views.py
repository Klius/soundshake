from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    userTypes = [  # fake array of posts
        { 
            'name': 'Carpintero',
            'description': 'Beautiful day in Portland!',
            'id_tipo_usuario': 1
        },
        { 
            'name': 'Fontanero', 
            'description': 'To be or not to be!',
            'id_tipo_usuario': 2
        },
        { 
            'name': 'Malabarista', 
            'description': 'Lore ipsum',
            'id_tipo_usuario': 3
        }
    ]
    return render_template('login.html',
    	                   userTypes=userTypes)

@app.route('/bulletin_board')
def bulletin_board():
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'},
            'body': 'Busco guitarra en Escocia!'
        },
        { 
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('bulletin_board.html',
                           posts=posts)
