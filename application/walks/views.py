from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.walks.models import Walk
from application.walks.forms import WalkForm
from datetime import datetime
from application.handlers.models import Handler


@app.route("/walks/new/")
@login_required
def walks_form():
    return render_template("walks/new.html", form = WalkForm(), handlers=Handler.query.filter_by(account_id=current_user.id))

@app.route("/walks/", methods=["GET", "POST"])
@login_required
def walks_create():
    
    form = WalkForm(request.form)
    
    if not form.validate():
        return render_template("walks/new.html", form = form)

    walk = Walk() 
    year = form.year.data
    month = form.month.data
    day = form.day.data 
    errorMessage = ["Anna kelvollinen päivämäärä ja aika"]

    try:
        walk.start = datetime(year, month, day, form.startHour.data, form.startMinute.data, 00, 00)
    except:

        return render_template("walks/new.html", form=form, errorStart = errorMessage)

    try:
        walk.end = datetime(year, month, day, form.endHour.data, form.endMinute.data, 00, 00)
    except:
        return render_template("walks/new.html", form=form, errorEnd = errorMessage)

    walk.place = form.place.data
    walk.length = form.length.data

    db.session().add(walk)
    db.session().flush()
    db.session().refresh(walk)
    db.session().commit()
    

    return render_template("walks/newhandler.html", walk_id=walk.id, handlers= Handler.query.filter_by(account_id=current_user.id))

@app.route("/walks/sethandler")
@login_required
def walks_set_handler(walk_id):
    
    return url_for("index")