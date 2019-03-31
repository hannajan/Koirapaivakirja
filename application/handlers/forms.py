from flask_wtf import FlaskForm
from wtforms import StringField, validators

message = "Nimen on oltava vähintään 2 ja enintään 120 merkkiä pitkä"

class HandlerForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=120, message=message)])

    class Meta:
        csrf = False