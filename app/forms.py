from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class SearchForm(FlaskForm):
    queryString = StringField('queryString', validators=[InputRequired()])


class LoginForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=7, max=200)])
    submit = SubmitField('Validar')
