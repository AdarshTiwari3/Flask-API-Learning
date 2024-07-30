from flask import Flask
from .auth.auth import auth # Import the auth blueprint . means from the same directory and .auth means from the auth folder and auth means from the auth.py file

def create_app(): # Create a function create_app, this is a special function name from Flask
    app = Flask(__name__) # Create a Flask application, this is a special variable name app that is calling Flask class
    
    # Register the blueprint
    app.register_blueprint(auth)
    
    return app
