from app import app
from bson import ObjectId
from config.constants import *
from flask import jsonify, abort, request
from app.utilities.mongoDB import connectMongo, closeMongo
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/v1/deleteOneUser/', methods = ['DELETE'])
@jwt_required()
def deleteOneUser():
    currentUser = get_jwt_identity()
    for user in USER_LIST:
        if currentUser == user.get('username'):
            assignedRole = user.get('roles')
    
    if assignedRole not in WRITE_ROLES:
        abort(403)
        
    userId = request.args.get('userId')
    client, db, collection = connectMongo(MONGO_URI, DATABASE, CUSTOMER_COLLECTION)

    try:
        result = collection.delete_one({'_id': ObjectId(userId)})
        if result.deleted_count > 0:
            return jsonify({"message": f"Record with _id {userId} deleted successfully."})
        else:
            return jsonify({"message": f"No Record found with _id {userId}"})
        
    except Exception as e:
        abort(501)

    finally:
        closeMongo(client)