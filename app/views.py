from flask import render_template, abort
from app import app

navbarItems = [
    {
        'route': 'login',
        'show': 'inicio sesion'
    },
    {
        'route': 'signup',
        'show': 'registro'
    },
    {
        'route': 'bulletin_board',
        'show': 'tablon'
    }
]

logged = False

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
    	                   current='index',
    	                   navbarItems=navbarItems)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',
                           title='inicio sesion',
                           current='login',
                           navbarItems=navbarItems)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
    return render_template('signup.html',
    	                   title='registro',
    	                   current='signup',
    	                   navbarItems=navbarItems,
    	                   userTypes=userTypes)

@app.route('/bulletin_board')
def bulletin_board():
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'title': 'Busco guitarra',
            'body': 'Busco guitarra en Escocia!'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'He perdido un contrabajo.'
        }
    ]
    return render_template('bulletin_board.html',
    	                   title='tablon',
    	                   current='bulletin_board',
    	                   navbarItems=navbarItems,
                           posts=posts)


@app.errorhandler(404)
def not_found(error):
	return render_template('routing/404.html',
		                   title='error'), 404

@app.errorhandler(401)
def not_found(error):
	return render_template('routing/401.html',
		                   title='error'), 401