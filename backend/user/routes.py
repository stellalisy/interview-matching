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

@app.route('/user/check', methods=['POST'])
def check():
  return User().check()

@app.route('/user/signout-schedule')
def signoutSchedule():
  return User().signoutSchedule()

@app.route('/interviewer/update', methods=['POST'])
def update_interviewer():
  return User().update_interviewer()

@app.route('/interviewee/update', methods=['POST'])
def update_interviewee():
  return User().update_interviewee()

@app.route('/admin/update', methods=['POST'])
def update_admin():
  return User().update_admin()

@app.route('/get-time', methods=['GET'])
def get_time():
  return User().get_time()

@app.route('/get-interviewee', methods=['GET'])
def get_interviewee():
  return User().get_interviewee()

@app.route('/get-role', methods=['GET'])
def get_role():
  return User().get_role()