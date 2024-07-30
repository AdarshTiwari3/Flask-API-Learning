from flask import Blueprint

# Create a blueprint for authentication routes
auth = Blueprint('auth', __name__) # 'auth' is the name of the blueprint and __name__ is the name of the module or package.

@auth.route('/login') # This is a route decorator, it is used to register a view function for a given URL rule. this is a routing mechanism in Flask
def login():
    return 'This is going to be a Login page'

@auth.route('/logout')
def logout():
    return 'This is going to be a Logout page'

@auth.route('/signup')
def signup():
    return 'This is going to be a Signup page'
