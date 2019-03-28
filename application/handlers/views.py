from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.handlers.models import Handler

@app.route("/handlers", methods=["GET"])
@login_required
def handlers_index():
    return render_template("handlers/list.html", handlers= Handler.query.filter_by(account_id=current_user.id) )

@app.route("/handlers/new/")
@login_required
def handlers_form():
    return render_template("handlers/new.html")

@app.route("/handlers/modify_<handler_id>/", methods=["GET"])
@login_required
def handlers_modify_form(handler_id):
    return render_template("handlers/modify.html", handler_id=handler_id)

@app.route("/handlers/<handler_id>/", methods=["POST"])
@login_required
def handlers_set_name(handler_id):
    h = Handler.query.get(handler_id)
    h.name = request.form.get("newname")
    db.session().commit()

    return redirect(url_for("handlers_index"))


@app.route("/handlers/", methods=["POST"])
@login_required
def handlers_create():
    t = Handler(request.form.get("name"))
    t.account_id = current_user.id

    db.session.add(t)
    db.session.commit()

    return redirect(url_for("handlers_index"))