from app_factory import create_app
from db_provider import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 


app = create_app("")

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ =="__main__":
	manager.run()