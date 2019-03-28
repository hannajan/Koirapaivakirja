from datetime import datetime, date

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

today = str(datetime.today())
year = int(today[:4])


messageName = "Nimen on oltava vähintään 2 ja enintään 120 merkkiä pitkä."
messageBreed = "Rodun nimen on oltava vähintään 3 ja enintään 120 merkkiä pitkä"
messageDay = "Päivän on oltava välillä 1-31"
messageMonth = "Kuukauden on oltava välillä 1-12"
messageYear = "Vuoden on oltava välillä 1980-" + str(year)

class DogForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=120, message=messageName)])
    breed = StringField("Rotu", [validators.Length(min=3, max=120, message=messageBreed)])
    birthday = IntegerField("Syntymäpäivä", [validators.NumberRange(min=1, max=31, message=messageDay)])
    birthmonth = IntegerField("Kuukausi", [validators.NumberRange(min=1, max=12, message=messageMonth)])
    birthyear = IntegerField("Vuosi", [validators.NumberRange(min=1980, max=year, message=messageYear)])

    class Meta:
        csrf = False

