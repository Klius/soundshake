from flask import render_template
from app import app
from app.forms import LoginForm

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
    nick_name = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        nick_name = form.nick_name.data
        form.nick_name.data = ''
        password = form.password.data
        form.password = ''
    return render_template('login.html',
                           current='login',
                           navbarItems=navbarItems,
                           form=form,
                           nickName=nick_name,
                           password=password)


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
                           navbarItems=navbarItems,
                           userTypes=user_types)


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
                           navbarItems=navbarItems,
                           posts=posts)


@app.errorhandler(401)
def not_found(error):
    return render_template('routing/401.html',
                           error=error), 401


@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html',
                           error=error), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('routing/500.html',
                           error=error), 500
