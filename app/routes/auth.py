from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from app import db
from app.forms import LoginForm, RegistrationForm
from app.models.user import User
from app.routes import is_safe_url

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.base'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or not is_safe_url(next_page):
            return redirect(url_for("index.base"))
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.base'))

@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index.base"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, 
            last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congrats, you are now a registered user")
        return redirect(url_for("auth.login"))
    return render_template("register.html", title="Register", form=form)