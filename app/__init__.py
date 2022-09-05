from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(Config)
        login = LoginManager(app)
        login.login_view = "auth.login"
        app.login = login
        db.init_app(app)
        migrate.init_app(app, db)

        from app.routes.index import index
        from app.routes.auth import auth

        app.register_blueprint(index, url_prefix="/")
        app.register_blueprint(auth, url_prefix="/auth")

        return app