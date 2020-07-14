from flask import Flask, jsonify, request, session, redirect, json, flash
from passlib.hash import sha256_crypt
from app import db
import uuid
from datetime import date

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    if request.form.get('password') != request.form.get('password2'):
      return jsonify({ "error": "Passwords don't match" }), 402

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "role": request.form.get('role')
    }

    # Encrypt the password
    user['password'] = sha256_crypt.hash(user['password'])
    #user['password2'] = pbkdf2_sha256.encrypt(user['password2'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.find_one({ "role": "Admin"}) and user['role'] == "Admin":
      return jsonify({ "error": "Admin account already signed up" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')

  def signoutSchedule(self):
    session.clear()
    return redirect('/check-schedule/')
  
  def login(self):
    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and sha256_crypt.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401

  def check(self):
    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and sha256_crypt.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
      
    return jsonify({ "error": "Invalid login credentials" }), 401

  def update_interviewer(self):
    user = session['user']
    print("update interviewer")

    data = json.loads(request.get_data(as_text=True))

    query = {"_id" : user['_id']}
    newvalues = {"$set": {
                    'max_int': data['max_int'],
                    'team': data['team'],
                    'time': data['grid']
                } }
    
    db.users.update_one(query, newvalues)

    return jsonify(user), 200

  def update_interviewee(self):
    user = session['user']
    print("update interviewee")

    data = json.loads(request.get_data(as_text=True))
    print(data)

    query = {"_id" : user['_id']}
    newvalues = {"$set": {
                    'year': data['year'],
                    'interest1': data['interest1'],
                    'interest2': data['interest2'],
                    'time': data['grid']
                } }
    
    db.users.update_one(query, newvalues)

    return jsonify(user), 200

  def update_admin(self):
    user = session['user']
    print("update admin")

    # Check for existing event name
    if db.users.find_one({ "event": request.form.get('event') }):
      if (db.users.find_one({ "event": request.form.get('event') })['_id'] != session['user']['_id']):
        return jsonify({ "error": "Event name already in use" }), 400

    start_time = int(request.form.get('start_time'))
    end_time = int(request.form.get('end_time'))
    #start_time = int(request.form.get('start_time').split(':')[0])
    #end_time = int(request.form.get('end_time').split(':')[0])
    print(start_time)
    print(end_time)
    hours = end_time - start_time
    if hours <= 0:
      return jsonify({ "error": "End time has to be later than start time" }), 400

    start_date = request.form.get('start_date').split('-')
    end_date = request.form.get('end_date').split('-')
    print(start_date)
    print(end_date)
    date0 = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    date1 = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    delta = date1 - date0
    days = delta.days + 1
    print(days)
    if days <= 0:
      return jsonify({ "error": "End date can't be earlier than start date" }), 400
    
    query = {"_id" : user['_id']}
    newvalues = {"$set": {
                    'event': request.form.get('event'),
                    'start_date': request.form.get('start_date'),
                    'end_date': request.form.get('end_date'),
                    'start_time': request.form.get('start_time'),
                    'end_time': request.form.get('end_time'),
                    'hours': hours,
                    'days': days
                } }

    
    db.users.update_one(query, newvalues)

    return jsonify(user), 200
  
  def get_time(self):
    adminAccount = db.users.find_one({"role": "Admin"})
    user = session['user']
    result = {
      'start_time': adminAccount['start_time'],
      'start_date': adminAccount['start_date'],
      'days': adminAccount['days'],
      'hours': adminAccount['hours']
    }
    if 'interviews' in user:
      result['interviews'] = user['interviews']
      result['num_int'] = user['num_int']
    if 'final_time' in user:
      result['final_time'] = user['final_time']
    return jsonify(result), 200
