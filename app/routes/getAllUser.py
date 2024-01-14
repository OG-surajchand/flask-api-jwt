import json
import app.utilities.utils as utils

from app import app
from flask import jsonify, abort
from config.constants import *
from app.utilities.mongoDB import connectMongo, closeMongo

@app.route('/v1/getAllUser', methods = ['GET'])
def getOneUser():
    try:
        client, db, collection = connectMongo(MONGO_URI, DATABASE, CUSTOMER_COLLECTION)

        response = [{key: utils.jsonDecoder(value) for key, value in document.items()} for document in collection.find()]
        jsonData = json.dumps(response)

        return json.loads(jsonData)
    except Exception as e:
        abort(501)
    finally:
        closeMongo(client)