import secrets
from flask import Flask, jsonify, request
from flask_cors import CORS
from config.constants import *
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)

#App Configuration
app.config.from_pyfile('../config/config.py')
app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
jwt = JWTManager(app)

from app.routes import getAllUser, createOneUser, deleteOneUser, userLogin