from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)
login = LoginManager(app)
login.login_view = "auth.login"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.routes.index import index
from app.routes.auth import auth

app.register_blueprint(index, url_prefix="/")
app.register_blueprint(auth, url_prefix="/auth")