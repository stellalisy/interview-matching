from flask import Flask, url_for, request, render_template, redirect, abort
from markupsafe import escape, Markup
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

#@app.route("/me")
#def me_api():
#    user = get_current_user()
#    return {
#        "username": user.username,
#        "theme": user.theme,
#        "image": url_for("user_image", filename=user.image),
#    }

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return projects()
    else:
        return hello_world()

with app.test_request_context('/login', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    print(request.path == '/hello')
    print(request.method == 'POST')


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
