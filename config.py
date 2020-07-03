"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

LESS_BIN = '/usr/local/bin/lessc'
ASSETS_DEBUG = False
ASSETS_AUTO_BUILD = True

class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'GDtfDCFYjD'
    #SECRET_KEY = environ.get('SECRET_KEY')
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_HOST = 'mongodb://localhost/'
    DB_PORT = 27017
    DB_DBNAME = 'interview'

    'MONGO_DBNAME' = 'interview'
    
    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')