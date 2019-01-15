from flask import Blueprint, render_template

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/index")
def base():
    user = {"username": "Calvin"}
    return render_template("index.html", title="Home", user=user)
