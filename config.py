from os import environ,path
from dotenv import load_dotenv
import datetime


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = 'application.py'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    FLASK_ENV = environ.get('FLASK_ENV')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_COOKIE_CSRF_PROTECT = environ.get('JWT_COOKIE_CSRF_PROTECT')
    JWT_CSRF_CHECK_FORM = environ.get('JWT_CSRF_CHECK_FORM')
    JWT_TOKEN_LOCATION = environ.get('JWT_TOKEN_LOCATION')
