from flask import render_template, redirect, request, url_for, flash, session
from . import auth
from .forms import LoginForm
from flask_login import login_user,logout_user, login_required, current_user
from ..models import User
from flask_sqlalchemy import SQLAlchemy
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print "Checking User!!!"
   
    if request.method == 'POST':
        
        # Check if user email exists
        user = User.query.filter_by(email=request.form['email']).first()
        print "I am %s " %  request.form.get('checkRemember')

        if request.form.get('checkRemember') is None:
            rem = False
        else:
            rem = True
        # Start authentication steps
        if user is not None:
            login_user(user, rem)
            flash('logged in successfully')
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password')
        # if user is None:
        #     return "User Not Found!!!"
        # else:
        #     return render_template('success.html')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print "Entering Form Registration"
        user = User(email=request.form.get('email'),
            username=request.form.get('username'),
            password = request.form.get('password')
            )
        
        db.session.add(user)
        db.session.commit()
 
        flash('You have successfully registered, you can now login')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')



