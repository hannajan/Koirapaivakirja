from datetime import datetime
from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.dogs.models import Dog
from application.dogs.forms import DogForm

@app.route("/dogs", methods=["GET"])
def dogs_index():
    return render_template("dogs/list.html", dogs = Dog.query.all())

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
    
    return redirect(url_for("index"))

@app.route("/dogs/<dog_id>")
def dogs_show(dog_id):
    dogs = Dog.query.filter_by(id=dog_id)
    day = dogs[0].birthday.strftime("%d")
    month = dogs[0].birthday.strftime("%m")
    year = dogs[0].birthday.strftime("%Y")
    return render_template("dogs/show.html", dogs=dogs, day=day, month=month, year=year, form=DogForm())
