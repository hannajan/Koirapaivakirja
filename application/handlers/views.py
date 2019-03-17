from application import app, db
from flask import redirect, render_template, request, url_for
from application.handlers.models import Handler

@app.route("/handlers", methods=["GET"])
def handlers_index():
    return render_template("handlers/list.html", handlers = Handler.query.all() )

@app.route("/handlers/new/")
def handlers_form():
    return render_template("handlers/new.html")

@app.route("/handlers/", methods=["POST"])
def handlers_create():
    t = Handler(request.form.get("name"))

    db.session.add(t)
    db.session.commit()

    return redirect(url_for("handlers_index"))