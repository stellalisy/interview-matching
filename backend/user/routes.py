from flask import Flask
from app import app
from user.models import User

@app.route('/api/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/api/user/signout')
def signout():
  return User().signout()

@app.route('/api/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/api/user/check', methods=['POST'])
def check():
  return User().check()

@app.route('/api/user/signout-schedule')
def signoutSchedule():
  return User().signoutSchedule()

@app.route('/api/interviewer/update', methods=['POST'])
def update_interviewer():
  return User().update_interviewer()

@app.route('/api/interviewee/update', methods=['POST'])
def update_interviewee():
  return User().update_interviewee()

@app.route('/api/admin/update', methods=['POST'])
def update_admin():
  return User().update_admin()

@app.route('/api/get-time', methods=['GET'])
def get_time():
  return User().get_time()

@app.route('/api/get-interviewee', methods=['GET'])
def get_interviewee():
  return User().get_interviewee()

@app.route('/api/get-role', methods=['GET'])
def get_role():
  return User().get_role()