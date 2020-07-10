from flask import Flask, jsonify, request, session, redirect, json
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

  def start_session(self, user):
    del user['password']
    #del user['password2']
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
    user['password'] = pbkdf2_sha256.encrypt(user['password'])
    #user['password2'] = pbkdf2_sha256.encrypt(user['password2'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
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

    query = {"_id" : user['_id']}
    newvalues = {"$set": {
                    'event': request.form.get('event'),
                    'start_date': request.form.get('start_date'),
                    'end_date': request.form.get('end_date'),
                    'start_time': request.form.get('start_time'),
                    'end_time': request.form.get('end_time')
                } }
    
    db.users.update_one(query, newvalues)

    return jsonify(user), 200


