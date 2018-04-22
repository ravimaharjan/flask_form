import sys
# print sys.path

sys.path.append("/Users/ravi/workspace/Python/flask_form")
from flask import Flask
from config import Config
from webapp.applications.home import home_app
from webapp.applications.auth import auth_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home_app)
app.register_blueprint(auth_app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.debug = True

# from app import routes, models

if __name__ == '__main__':
    app.run("127.0.0.1", 5001)

