from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/user/update', methods=['POST'])
def update_interviewer():
  return User().update()

@app.route('/user/update', methods=['POST'])
def update_interviewee():
  return User().update()