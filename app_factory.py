from flask import Flask
from db_provider import db
from config import Config
from webapp.applications.home import home_app
from webapp.applications.auth import auth_app
from extensions import migrate

def create_app(config_file):
    app = Flask(__name__)
    from webapp import models
    
    app.config.from_object(Config)
    register_blueprint(app)
    register_extensions(app)

    return app

def register_blueprint(app):
    app.register_blueprint(home_app)
    app.register_blueprint(auth_app)

def register_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db)