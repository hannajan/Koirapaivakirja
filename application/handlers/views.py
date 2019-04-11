from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.handlers.models import Handler
from application.handlers.forms import HandlerForm

@app.route("/handlers", methods=["GET"])
@login_required
def handlers_index():
    return render_template("handlers/list.html", handlers= Handler.query.filter_by(account_id=current_user.id) )

@app.route("/handlers/new/")
@login_required
def handlers_form():
    return render_template("handlers/new.html", form = HandlerForm())

@app.route("/handlers/modify_<handler_id>/", methods=["GET"])
@login_required
def handlers_modify_form(handler_id):
    handler = Handler.query.get(handler_id)
    return render_template("handlers/modify.html", handler=handler, form = HandlerForm())

@app.route("/handlers/<handler_id>/", methods=["POST"])
@login_required
def handlers_set_name(handler_id):

    form = HandlerForm(request.form)

    if not form.validate():
        return render_template("/handlers/modify.html", form = form, handler_id=handler_id)

    h = Handler.query.get(handler_id)
    h.name = form.name.data
    db.session().commit()

    return redirect(url_for("handlers_index"))


@app.route("/handlers/", methods=["POST"])
@login_required
def handlers_create():

    form = HandlerForm(request.form)

    if not form.validate():
        return render_template("handlers/new.html", form = form)

    h = Handler(form.name.data)
    h.account_id = current_user.id

    db.session.add(h)
    db.session.commit()

    return redirect(url_for("handlers_index"))