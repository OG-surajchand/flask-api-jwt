from app import app
from flask import jsonify

@app.route('/endPoint', methods = ['GET'])
def endpointRoute():
    return jsonify({"Message": "This is the message from Endpoint!!"})