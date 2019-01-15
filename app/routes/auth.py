from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import LoginForm

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index.base"))
    return render_template("login.html", title="Sign In", form=form)