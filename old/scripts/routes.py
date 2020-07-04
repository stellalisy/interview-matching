from flask import url_for, render_template, redirect, make_response, request, jsonify, json, session
from flask import current_app as app
from .forms import ContactForm, SignupForm
#from .models import db, User


@app.route('/data', methods=['GET'])
def get_data():
    with open('/Users/bytedance/interview-matching/algorithm/data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('home.html',
                           template='home-template')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    #form = ContactForm(meta={'csrf': False})
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('contact.html',
                           form=form,
                           template='form-template')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    #form = SignupForm(meta={'csrf': False})
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('signup.html',
                           form=form,
                           template='form-template')


@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')

@app.route("/api/v2/test_response")
def users():
    head = {"Content-Type": "application/json"}
    response = make_response('Test worked!', 200)
    #response.headres['Content-Type'] = 'application/json'
    return response



"""
@app.route('/create', methods=['GET'])
def user_records():
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
            on the playground is where I spent most of my days",
            admin=False
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for('user_records'))
    return render_template(
        'users.html',
        users=User.query.all(),
        title="Show Users"
    )"""

"""

@app.errorhandler(404)
def not_found():
    #Page not found.
    return make_response(render_template("404.html"), 404)


@app.errorhandler(400)
def bad_request():
    #Bad request.
    return make_response(render_template("400.html"), 400)


@app.errorhandler(500)
def server_error():
    #Internal server error.
    return make_response(render_template("500.html"), 500)"""