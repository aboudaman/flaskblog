Installing VENV for flask
virtualenv venv
. venv/bin/activate

#download for pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

#Install flask
pip install flask

#install sqlalchemy
pip install sqlalchemy

#start glask server
export FLASK_APP=hello.py
flask run

#specify the host
flask run --host 0.0.0.0

#Data and time - UTC is used
handled with Flask-Moment
pip install flask-moment
used with jquery

#Create a database based on the model classes
export FLASK_APP=directory.py #directory.py = name of application
flask shell
from directory import db    # directory= name of app
db.create_all() #creates the database
db.drop_all()   # deletes the database

# Inserting Rows
from appname import Role, User
admin_role = Role(name='Admin')
user_joe = User(username='joe', role=admin_role)    #role attribute from backref can be used as a high level representation
db.session.add(admin_role)
or
db.session.add_all([user_joe, admin_role])
db.session.commit()

#Rolling back database changes
db.session.rollback()

#Updating rows
admin_role.name = Administrator
db.session.add(admin_role)
db.session.commit()

#Deleting rows
db.session.delete(mod_role)
db.session.commit()

#Querying ROWS
Role.query.all()   #returns all rows in a database
Role.qyery.filter_by(name='name').first()   # Return the first occurence or none

#Querying SPECIFIC rows
use filters
User.query.filter_by(role=user_role).all()

#CHECK SQL code
str(User.query.filter_by(role=user)

# Add changes to the database
Manged via flask alchemy database session
db.session.add(admin_role)
db.session.add(user_joe)
#update tables in database
Use database migration framework
pip install flask-migrate
migrate = Migrate(app, db)
    add support: flask db init (entered from command line, to create a migration)
    flask db migrate -m "initial migration"
    flask upgrade() -> applies changes to the database
    flask downgrade() -> removes the last migration from the database

# Not having to import the database instance and models each time in the shell
add 
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

#Before using shell
export FLASK_APP=hello.py

# Adding Migration - Used to make changes and update your database efficiently
pip install flask-migrate

import in your project: from flask_migrate import Migrate
flask db init
flask db migrate    # Perform the migration
flask db upgrade    # Apply the migration

#### Organizing the Folders ####
|- Project
    |- app/
        |- templates/
        |- static/
        |- main/
            |-__init__.py
            |- errors.py
            |- forms.py
            |- views.py
        |- __init__.py
        |- email.py
        |- models.py
    |- migrations
    |- tests/
        |- __init__.py
        |- test*.py
    |- venv/
    |- requirements.txt
    |- config.py
    |- flasky.py

# REQUIREMENTS FILE
It is good practice to include a requirements.txt file.  This records all the package dependencies with exact version 
numbers.  This is important in case the virtual environment needs to be regenerated on a different machine.
This file can be generated automatically by pip: pip freeze > requirements.txt

When you need to build a perfect replica of the virtual environment.  You can create a new virtual environment
by: pip install -r requirements.txt

# Unit Tests

