from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)
SQLAlchemy(app)

from app import views, models

if __name__ == '__main__':
    app.run()
