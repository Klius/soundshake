from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class SearchForm(FlaskForm):
    queryString = StringField('queryString', validators=[InputRequired()])


class LoginForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])
    submit = SubmitField('Validar')
