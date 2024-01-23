import json
from app import app
from flask import request, jsonify, abort
from config.constants import *
from app.utilities.mongoDB import connectMongo, closeMongo
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/v1/createOneUser', methods = ['POST'])
@jwt_required()
def createOneUser():
    currentUser = get_jwt_identity()
    for user in USER_LIST:
        if currentUser == user.get('username'):
            assignedRole = user.get('roles')
    
    if assignedRole not in WRITE_ROLES:
        abort(403)
    
    client, db, collection = connectMongo(MONGO_URI, DATABASE, CUSTOMER_COLLECTION)
    sourcePayload = request.get_json()
    try:
        alreadyExisting = collection.find_one(sourcePayload)
        if alreadyExisting:
            return jsonify({"message": "The record already exists."})
        
        else:
            targetPayload = {
                "first_name": sourcePayload['first_name'],
                "last_name": sourcePayload['last_name'],
                "phone_number": sourcePayload['phone_number'],
                "designation": sourcePayload['designation'],
                "start_date": sourcePayload['start_date'],
                "end_date": sourcePayload['end_date']
            }
            result = collection.insert_one(targetPayload)
            return jsonify({"created_user_id": int(str(result.inserted_id), 16)})
    
    except Exception as e:
        return jsonify({"message": "Error Formatting in the Payload."})

    finally:
        closeMongo(client)
        