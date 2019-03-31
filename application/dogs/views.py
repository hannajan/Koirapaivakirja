from datetime import datetime
from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.dogs.models import Dog
from application.dogs.forms import DogForm

@app.route("/dogs/new/")
@login_required
def dogs_form():
    return render_template("dogs/new.html", form = DogForm())

@app.route("/dogs/", methods=["POST"])
@login_required
def dogs_create():
    form = DogForm(request.form)

    if not form.validate():
        return render_template("dogs/new.html", form = form)

    dog = Dog()
    dog.name = form.name.data
    dog.breed = form.breed.data
    try:
        dog.birthday = datetime(form.birthyear.data, form.birthmonth.data, form.birthday.data)
    except:
        errorMessage = ["Päivämäärää ei ole olemassa"]
        return render_template("dogs/new.html", form=form, errorMessage = errorMessage)   
    
    db.session().add(dog)
    db.session().commit()
    
    return "Koira lisätty!"