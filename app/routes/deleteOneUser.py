from app import app
from bson import ObjectId
from config.constants import *
from flask import jsonify, abort, request
from app.utilities.mongoDB import connectMongo, closeMongo

@app.route('/deleteOneUser/', methods = ['DELETE'])
def deleteOneUser():
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