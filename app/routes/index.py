from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/index')
def hello():
    return 'Hello, World!'
