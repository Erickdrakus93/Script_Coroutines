from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__) #This is the instance of the main app as we can note
    app.config['SECRET_KEY'] = 'some_chains_as_the_main'
    app.config['SQLALCHEMY_DATABASE'] = 'some chain of the main form'
    db.init_app(app)
    return app