from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.walks.models import Walk, WalkHandler
from application.walks.forms import WalkForm
from datetime import datetime
from application.handlers.models import Handler


@app.route("/walks/new/")
@login_required
def walks_form():
    form = WalkForm()
    form.handlers.choices = [(handler.id, handler.name) for handler in Handler.query.filter_by(account_id=current_user.id).all()]

    return render_template("walks/new.html", form=form)

@app.route("/walks/", methods=["GET", "POST"])
@login_required
def walks_create():
    
    form = WalkForm(request.form)
    
    if not form.validate():
        return render_template("walks/new.html", form = form)

    year = form.year.data
    month = form.month.data
    day = form.day.data 
    errorMessage = ["Anna kelvollinen päivämäärä ja aika"]

    try:
        start = datetime(year, month, day, form.startHour.data, form.startMinute.data, 00, 00)
    except:

        return render_template("walks/new.html", form=form, errorStart = errorMessage)

    try:
        end = datetime(year, month, day, form.endHour.data, form.endMinute.data, 00, 00)
    except:
        return render_template("walks/new.html", form=form, errorEnd = errorMessage)

    walk = Walk(start, end, form.place.data, form.length.data) 

    db.session().add(walk)
    db.session().flush()
    db.session().refresh(walk)

    for handler_id in form.handlers.data:
        walkhandler = WalkHandler(walk.id, handler_id)
        db.session().add(walkhandler)

    db.session().commit()
    

    return render_template("index.html")

@app.route("/walks/sethandler")
@login_required
def walks_set_handler(walk_id):
    
    return url_for("index")