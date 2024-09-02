from flask import Flask
from pymongo import MongoClient

def connect_db():
    uri = 'mongodb+srv://ochiengwalter02:walter8236@waltertayadb.y2nbk2w.mongodb.net/'
    try:
        client = MongoClient(uri)
        # db = client['movies-db']
        db = client.movies_db
        print('Databases connected successfully')
        return db
    except Exception as e:
        raise e


def create_app():
    app = Flask(__name__)
    with app.app_context():
        db = connect_db()
        app.config['db'] = db
    return app