from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes.index import index
from app.routes.auth import auth

app = Flask(__name__)
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(auth, url_prefix="/auth")
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)