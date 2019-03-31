from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = StringField("Salasana")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi")
    username = StringField("Käyttäjätunnus")
    password = StringField("Salasana")

    class Meta:
        csrf = False