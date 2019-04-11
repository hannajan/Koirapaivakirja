from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectMultipleField, validators


msgInt = "Käytä pistettä erottimena. Pituus oltava vähintään 0.01 km"
msgPlace = "Paikan nimi voi olla korkeintaan 120 merkkiä pitkä"
class WalkForm(FlaskForm):
    day = IntegerField("Päivämäärä") 
    month = IntegerField("Kuukausi")
    year = IntegerField("Vuosi")
    startHour = IntegerField("Alkoi")
    startMinute = IntegerField("Minuutti")
    endHour = IntegerField("Loppui", validators=(validators.Optional(),))
    endMinute = IntegerField("Minuutti", validators=(validators.Optional(),))
    place = StringField("Paikka", [validators.Length(max=120, message = msgPlace)])
    length = FloatField("Pituus (km)", [validators.NumberRange(min=0.01, message = msgInt)])
    handlers = SelectMultipleField("Hoitajat", choices=[])

    class Meta:
        csrf = False
