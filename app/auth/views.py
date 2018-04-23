from flask import render_template, redirect, request, url_for, flash, session
from . import auth
from .forms import LoginForm
from flask_login import login_user
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print "Checking User!!!"
   
    if request.method == 'POST':
        
        # Check if user email exists
        user = User.query.filter_by(email=request.form['email']).first()
        print "I am %s " %  request.form.get('checkRemember')

        # if request.form.get('checkRemember') is None:
        #     rem = False
        # else:
        #     rem = True
        if user is not None:
            login_user(user)
            flask.flask('logged in successfully')
            next = flask.request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        # Start authentication steps
        flash('Invalid username or password')
        # if user is None:
        #     return "User Not Found!!!"
        # else:
        #     return render_template('success.html')
    return render_template('auth/login.html', form=form)



