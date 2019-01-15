from flask import Blueprint, render_template
from flask_login import login_required

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/index")
@login_required
def base():
    return render_template("index.html", title="Home")
