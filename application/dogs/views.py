from datetime import datetime
from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.dogs.models import Dog
from application.dogs.forms import DogForm

@app.route("/dogs", methods=["GET"])
@login_required
def dogs_index():
    return render_template("dogs/list.html")

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
    dog.account_id = current_user.id
    try:
        dog.birthday = datetime(form.birthyear.data, form.birthmonth.data, form.birthday.data)
    except:
        errorMessage = ["Päivämäärää ei ole olemassa"]
        return render_template("dogs/new.html", form=form, errorMessage = errorMessage)   
    
    db.session().add(dog)
    db.session().commit()
    
    return redirect(url_for("dogs_index"))

@app.route("/dogs/<dog_id>")
@login_required
def dogs_show(dog_id):
    dog = Dog.query.get(dog_id)
    day = dog.birthday.strftime("%d")
    month = dog.birthday.strftime("%m")
    year = dog.birthday.strftime("%Y")

    return render_template("dogs/show.html", dog=dog, day=day, month=month, year=year, form=DogForm())

@app.route("/dogs/<dog_id>/modify", methods=["GET", "POST"])
@login_required
def dogs_modify(dog_id):
    form = DogForm(request.form)
    dog = Dog.query.get(dog_id)
    day = dog.birthday.strftime("%d")
    month = dog.birthday.strftime("%m")
    year = dog.birthday.strftime("%Y")

    if not form.validate():
        return render_template("dogs/show.html", form = form, dog=dog, day=day, month=month, year=year)



    dog.name = form.name.data
    dog.breed = form.breed.data
    
    try:
        dog.birthday = datetime(form.birthyear.data, form.birthmonth.data, form.birthday.data)
    except:
        errorMessage = ["Päivämäärää ei ole olemassa"]
        return render_template("dogs/show.html", form=form, errorMessage = errorMessage, dog=dog, day=day, month=month, year=year) 

    db.session.commit()

    return redirect(url_for("dogs_index"))

@app.route("/dogs/<dog_id>/remove", methods=["POST"])
@login_required
def dogs_delete(dog_id):
    dog = Dog.query.get(dog_id)
    db.session().delete(dog)
    db.session().commit()

    return redirect(url_for("dogs_index"))