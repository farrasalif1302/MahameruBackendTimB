from flask import Flask, jsonify, request
import uuid
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from UserContact.db import *

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

# TODO : fix this so it match with the given docs

@bp.route('/createuser', methods=['POST'])
def createuser():
        try:
            # for testing purpose only getting one request json
            bp['name'] = request.json['user']
            bp['no_telp'] = request.json['no_telp']
            bp['pin'] = request.json['pin']
            bp['created_at'] = request.json['created_at']
            bp['updated_at'] = request.json['updated_at']
            bp['userid'] = uuid.uuid4()

            response = jsonify({'id' : bp['userid']})
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message' : 'Failed to create user'})
            response.status_code = 400
        finally:
            return response

# TODO : dont modify it untill the above route is fixed
@bp.route('/createuser', methods=['PUT'])
def edituser():
        try:
            bp['userid'] = request.json['userid']
            bp['name'] = request.json['name']
            bp['no_telp'] = request.json['no_telp']
            bp['pin'] = request.json['pin']
            bp['updated_at'] = request.json['updated_at']

            response = jsonify({'id' : bp['userid']})
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message': 'Failed to create user'})
            response.status_code = 400
        finally:
            return response

@bp.route('/createuser/<string:user_id>', methods=['GET'])
def newuser(user_id):
    try:
        # this code must be changed after implementing the database
        if user_id == '2c535c8b-5d2b-4a72-9268-1c83aaf61902':
            response = jsonify({'user': 'Aditya'})
            response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to get user'})
        response.status_code = 400
    finally:
        return response

@bp.route('/deluser', methods=['DELETE'])
def deleteuser():
    # this code must be fixed after implmenting the database and getting clarity from director
    return jsonify({'mesage' : 'deleting the user that you want'})

if __name__ == "__user__":
        bp.run(debug=True)