from flask import Flask

from app.routes.index import index

app = Flask(__name__)
app.register_blueprint(index, url_prefix="/")