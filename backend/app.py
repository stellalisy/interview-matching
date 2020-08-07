from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
import os

#app = Flask(__name__)
#app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

app = Flask(
    __name__,  
    #static_folder='./frontend/build',
    static_folder='',
    static_url_path='', 
    )
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "build")
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
def init_database():
    import json
    try:
        from urllib.parse import quote_plus
    except ImportError:
        # Python 2.x
        from urllib import quote_plus

    with open('mongo.json') as f:
        config = json.load(f)
    uri = config['mongo_uri']
    return pymongo.MongoClient(uri)

#client = pymongo.MongoClient('localhost', 27017)
client = init_database()
db = client.interview_matcher
#app = Flask(__name__)
#app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

@app.route('/')
def index():
    return send_from_directory(root, 'index.html')

# Routes
from user import routes

if __name__ == '__main__':
    app.run()
