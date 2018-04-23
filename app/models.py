from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager

#### Start Database ORM ####
class Role(db.Model):
    # define name of the table
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # create 1 to many relationship between table roles and table users.  backref defines the reverse direction, 
    # can be used on any instance of User instead of role_id to access the Role model as an object
    users = db.relationship('User', backref='role')

# Optional method to give readable string representation
    def __repr__(self):
        return '<ROLE %r>' % self.name

#Function to be invoked when user needs to be loaded from database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # create relationshp with table roles, 'roles.id' argument specifies is the id from roles column.
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username


#### END Database ORM ####

