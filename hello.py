import os
from flask import Flask, render_template, session, redirect, url_for
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Secret key for wtforms

app.config['SECRET_KEY'] = 'hard to guess string'
# Start DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# End DB Config

# Time wrapper
moment = Moment(app)

### Form Class ##
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')
## End Form Class ##

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    # create relationshp with table roles, 'roles.id' argument specifies is the id from roles column.
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username


#### END Database ORM ####


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

# User Form
@app.route('/user', methods=['GET', 'POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('user.html', form=form, name=session.get('name'))



# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# Form class


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)