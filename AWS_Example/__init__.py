from flask import Flask
from AWS_Example.model import db,Database,jwt_manager
from .home import home
import datetime


#create application
def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')
    with app.app_context():
        engine = Database.init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        db.init_app(app)

        #.env file
        if app.config.get('JWT_COOKIE_CSRF_PROTECT') == 'True':
            app.config['JWT_COOKIE_CSRF_PROTECT'] = True
        else: app.config['JWT_COOKIE_CSRF_PROTECT'] = False

        if app.config.get('JWT_CSRF_CHECK_FORM') == 'True':
             app.config['JWT_CSRF_CHECK_FORM'] = True
        else: app.config['JWT_CSRF_CHECK_FORM'] = False

        jwt_manager.init_app(app)

        app.register_blueprint(home.home_bp)
        return app
