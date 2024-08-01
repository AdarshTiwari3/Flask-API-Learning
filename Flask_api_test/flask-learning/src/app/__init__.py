from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config # Import the Config class from config which is in the config folder of the app package

db = SQLAlchemy()  # Create a SQLAlchemy object db

def create_app():  # Create a function create_app
    app = Flask(__name__)  # Create a Flask application instance
    
    app.config.from_object(Config)  # Load configuration from config.py
    db.init_app(app)  # Initialize the SQLAlchemy object with the Flask app
    app.config['SESSION_COOKIE_SECURE'] = True  # Cookies should only be sent over HTTPS
    app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to cookies
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
    # Register the blueprint
    from .auth.auth import auth  # Import the auth blueprint
    app.register_blueprint(auth, url_prefix='/auth')
    
    
    
    return app
