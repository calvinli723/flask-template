from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes.index import index_blueprint
from app.routes.login import login_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint, url_prefix="/")
app.register_blueprint(login_blueprint, url_prefix="/login")
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)