from flask import render_template, request, abort
from app import app
from app.forms import LoginForm

navbarItemsUnlogged = [
    {
        'route': 'login',
        'show': 'inicio sesion'
    },
    {
        'route': 'signup',
        'show': 'registro'
    }
]

navbarItemsLogged = [
    {
        'route': 'profiles',
        'show': 'perfil'
    },
    {
        'route': 'bulletin_board',
        'show': 'tablon'
    },
    {
        'route': 'events',
        'show': 'eventos'
    }
]

logged = False


@app.route('/')
@app.route('/index')
def index():
    html_address = 'index.html'
    navbar_items = navbarItemsUnlogged
    # Para cuando tengamos usuarios y esas cosas, de momento a piñon...
    if logged:
        html_address = 'index.html'
        navbar_items = navbarItemsLogged

    return render_template(html_address,
                           current='index',
                           navbarItems=navbar_items)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    return render_template('login.html',
                           current='login',
                           navbarItems=navbarItemsUnlogged,
                           form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    user_types = [  # fake array of posts
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
                           current='signup',
                           navbarItems=navbarItemsUnlogged,
                           userTypes=user_types)


# cambiar route para que sea /user/<nombre usuario>/<num> para el usuario/perfil seleccionado, o algo por el estilo
@app.route('/user')
def profiles():
    return render_template('profiles.html',
                           current='profiles',
                           navbarItems=navbarItemsLogged)


@app.route('/bulletin_board')
def bulletin_board():
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'title': 'Busco guitarra',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Lost bass',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        }
    ]
    return render_template('bulletin_board.html',
                           current='bulletin_board',
                           navbarItems=navbarItemsLogged,
                           posts=posts)


@app.route('/events')
def events():
    return render_template('events.html',
                           current='events',
                           navbarItems=navbarItemsLogged)


@app.errorhandler(401)
def not_found(error):
    return render_template('401.html',
                           error=error), 401


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',
                           error=error), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html',
                           error=error), 500
