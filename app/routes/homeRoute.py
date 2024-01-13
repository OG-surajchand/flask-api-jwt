from app import app
from flask import jsonify

@app.route('/', methods = ['GET'])
def homeRoute():
    return jsonify({"Message": "Hello World API!!"})