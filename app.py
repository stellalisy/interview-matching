# import the Flask class from the flask module
from functools import wraps
from flask import Flask, Markup, render_template, make_response
from flask import redirect, request, url_for, session, flash, json

import os
import datetime
import random, string

import math

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'key'


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    return render_template('index.html')  # render a template


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin') or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))


@app.route('/availability_e')
@login_required
def availability_interviewee():
    if request.method == 'POST':
        flash('Saved')
    return render_template('availability_e.html')


@app.route('/check_e')
@login_required
def check_interviewee():
    return render_template('check_e.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
