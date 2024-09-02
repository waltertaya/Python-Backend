from flask import Flask
from flask_pymongo import PyMongo
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    with app.app_context():
        mongo = PyMongo(app)
        app.config['mongo'] = mongo
    return app
