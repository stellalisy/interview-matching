"""Initialize app."""
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_jwt_extended import JWTManager
import pymysql
from pymongo import MongoClient
#from flask_assets import Environment


# Globally accessible libraries
client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.mymongodb  # Select the database
tasks_collection = db.task
initial_tasks = [task for task in tasks_collection.find()]
r = FlaskRedis()


def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    #assets = Environment(app)

    #assets.init_app(app)
    #db.init_app(app)
    r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from . import auth

        #db.create_all()  # Create sql tables for our data models

        # Register Blueprints
        app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        #compile_static_assets(assets)

        return app