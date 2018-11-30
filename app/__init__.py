# app/__init__.py

# third-party imports
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# local imports
from config import app_config
from flask_bootstrap import Bootstrap
# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    print("pass")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Bootstrap(app)
    migrate=Migrate(app,db)
    from app import models
   
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app