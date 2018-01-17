from flask_script import Manager
from flaskblog import create_app
from flask_migrate import Migrate, MigrateCommand
from flaskblog.models import db

app = create_app()
manager = Manager(app)

# db migrate
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run() # direct call to run so we can run and debug from PyCharm