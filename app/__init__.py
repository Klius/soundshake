from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')

SQLAlchemy(app)

from app import views, models

if __name__ == '__main__':
    app.run()
