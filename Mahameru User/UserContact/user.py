from flask import Flask, jsonify, request
import uuid
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from UserContact.db import *
from bson.objectid import ObjectId

bp = Blueprint('user', __name__,
                        template_folder='templates')


# placeholder data
'''user = {
    'userid': '',
    'name': '',
    'no_telp': '',
    'pin': '',
    'created_at': '',
    'updated_at': '',
    'contact_id': ''
}'''

# User 
@bp.route('/get', methods=['GET'])
def getuser():
    data = get_user()
    return data

@bp.route('/createuser', methods=['POST'])
def createuser():
        try:
            bp = {}
            bp['name'] = request.json['user']
            bp['no_telp'] = request.json['no_telp']
            bp['pin'] = request.json['pin']
            bp['created_at'] = request.json['created_at']
            bp['updated_at'] = request.json['updated_at']
            bp['userid'] = uuid.uuid4()

            response = get_user({"_id" : ObjectId('userid')})
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message' : 'Failed to create user'})
            response.status_code = 400
        finally:
            return response

@bp.route('/createuser', methods=['PUT'])
def edituser():
        try:
            bp = {}
            bp['userid'] = request.json['userid']
            bp['name'] = request.json['name']
            bp['no_telp'] = request.json['no_telp']
            bp['pin'] = request.json['pin']
            bp['updated_at'] = request.json['updated_at']

            response = insert_user(bp)
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message': 'Failed to create user'})
            response.status_code = 400
        finally:
            return response

@bp.route('/createuser/<string:user_id>', methods=['GET'])
def newuser(userid):
    try:
        if userid == '3':
            response = get_user({"_id" : ObjectId('userid')})
            response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to get user'})
        response.status_code = 400
    finally:
        return response

@bp.route('/deluser', methods=['DELETE'])
def deleteuser():
    row = delete_user({"_id": row.inserted_id})
    return jsonify({'mesage' : 'deleting the user that you want'})

if __name__ == "__user__":
        bp.run(debug=True)