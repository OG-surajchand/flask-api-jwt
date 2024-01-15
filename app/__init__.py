from flask import Flask
from flask_cors import CORS
from config.constants import *
from app.utilities.secretKey import *
from werkzeug.security import safe_str_cmp
from flask_jwt import JWT, jwt_required, current_identity

#########################################################
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'Admin', 'Admin@123')
]
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

#########################################################
app = Flask(__name__)
CORS(app)

app.config.from_pyfile('../config/config.py')
app.config['SECRET_KEY'] = generateSecretKey()

jwt = JWT(app, authenticate, identity)

from app.routes import getAllUser, createOneUser, deleteOneUser