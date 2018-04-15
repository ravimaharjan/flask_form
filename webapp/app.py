from flask import Flask
from config import Config
from applications.home import home_app
from applications.auth import auth_app
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home_app)
app.register_blueprint(auth_app)

app.debug = True


if __name__ == '__main__':
    app.run("127.0.0.1", 5001)

