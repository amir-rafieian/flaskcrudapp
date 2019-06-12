# app/__init__.py
# =============================================================================
# Import Libraries
# =============================================================================
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# =============================================================================
# Config
# =============================================================================
db = SQLAlchemy() #Create a database instance
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login' #let the login manager know about the function we use to log the user
login_manager.session_protection = 'strong' #for security. flask will delete the session info, and force user to login/logout each time
bcrypt = Bcrypt()

#Define a function to use different configurations (dev, test, prod)
def create_app(config_type):
    app = Flask(__name__)
    #pass the configuration file:
    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')
    app.config.from_pyfile(configuration)
    db.init_app(app) #bind database to flask app
    bootstrap.init_app(app) #initiate bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    from app.catalog import main #let flask knows we are using blueprint. the app here is the application name
    app.register_blueprint(main) #the app is here is the flask application
    
    from app.auth import authentication
    app.register_blueprint(authentication)
    
    return app



    
    


