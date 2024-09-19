from flask import Flask

def create_app():

    # app = Flask(__name__)
    app = Flask(__name__, static_folder='../public', template_folder='../templates')
    return app
