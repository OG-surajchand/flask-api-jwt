from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('../config/config.py')

from app.routes import getAllUser, createOneUser, deleteOneUser