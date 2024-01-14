from app import app
from flask import request, jsonify
from config.constants import *
from app.utilities.mongoDB import connectMongo, closeMongo

@app.route('/v1/createOneUser', methods = ['POST'])
def createOneUser():
    client, db, collection = connectMongo(MONGO_URI, DATABASE, CUSTOMER_COLLECTION)

    sourcePayload = request.get_json()
    try:
        targetPayload = {
            "first_name": sourcePayload['first_name'],
            "last_name": sourcePayload['last_name'],
            "phone_number": sourcePayload['phone_number'],
            "designation": sourcePayload['designation'],
            "start_date": sourcePayload['start_date'],
            "end_date": sourcePayload['end_date']
        }
        alreadyExisting = collection.find_one(targetPayload)
        if alreadyExisting:
            return jsonify({"message": "The record already exists."})
        else:
            result = collection.insert_one(targetPayload)
            return jsonify({"created_user_id": int(str(result.inserted_id), 16)})
    
    except Exception as e:
        return jsonify({"message": "Error Formatting in the Payload."})

    finally:
        closeMongo(client)
        