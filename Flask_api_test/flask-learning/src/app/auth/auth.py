from flask import Blueprint, request, jsonify, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .models import User
from functools import wraps
import jwt
import datetime
import os

auth = Blueprint('auth', __name__)

# Middleware to verify JWT

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            print("Request=",request.headers)
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            # Decode token and verify its expiration
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(username=data['username']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs) # this will return the route function example protected(), with the current_user as an argument
    return decorator

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@auth.route('/login', methods=['POST'])
def login():
    print("REquest=",request.headers)
    data = request.get_json()
    print("Data=",data)
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Set expiration time to 30 minutes
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    token = jwt.encode({'username': user.username, 'exp': expiration}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token}), 200

@auth.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logged out successfully"}), 200

@auth.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({"message": f"Hello, {current_user.username}!"}), 200 # this will return the current_user.username from the token
