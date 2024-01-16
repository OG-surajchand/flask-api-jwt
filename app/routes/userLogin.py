from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app import app

usersList = [
    {"username": "Admin", "password": "Admin123", "roles": ["admin"]},
]
usersDict = {user["username"]: user for user in usersList}

@app.route('/v1/userLogin', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in usersDict[username]['username'] and usersDict[username]['password'] == password:
        print(usersDict[username]['username'])
        additional_claims = {"roles": usersDict[username]["roles"]}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

