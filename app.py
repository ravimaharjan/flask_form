import sys
from app_factory import create_app
sys.path.append("/Users/ravi/workspace/Python/flask_form")

if __name__ == '__main__':
    app = create_app("")
    app.debug = True
    app.run("127.0.0.1", 5001)

