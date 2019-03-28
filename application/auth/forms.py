from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = StringField("Salasana")

    class Meta:
        csrf = False