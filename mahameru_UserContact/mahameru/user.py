from flask import Flask, jsonify, request, current_app
import uuid
import datetime
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mahameru.db import *

user = Blueprint('user', __name__,
                        template_folder='templates')


# placeholder data


# user 
@user.route('/get', methods=['GET'])
def getuser():
    try:
        # kalau variabel user = {} diapus, makan akan dapet response {'message': 'Failed to create user'}
        # jadi kesalahannya itu belom nyambung ke mongodb
        current_app.logger.debug("test")
        user = {}
        user['userid'] = 3
        user['name'] = 'Daniella'
        user['no_telp'] = '6287885728208'
        user['pin'] = '1234'
        user['created_at'] = '12/2/2022'
        user['updated_at'] = ''
        user['contact_id'] = 2
        current_app.logger.debug(user)
        response = jsonify(user)
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create user'})
        response.status_code = 400
    finally:
        return response


# TODO : fix this so it match with the given docs
@user.route('/createuser', methods=['POST'])
def createuser():
    try:
        # ini juga sama. kalau nambahin variabel user = {}, baru bisa di run.
        # sama kek tadi, tinggal konekin ke mongodbnya.
        user['name'] = request.json['user']
        user['no_telp'] = request.json['no_telp']
        user['pin'] = request.json['pin']
        user['created_at'] = request.json['created_at']
        user['updated_at'] = request.json['updated_at']
        user['userid'] = uuid.uuid4()

        response = jsonify({'id' : user['userid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to create channnel'})
        response.status_code = 400
    finally:
        return response

# TODO : dont modify it unt ill the above route is fixed
@user.route('/createuser', methods=['PUT'])
def edituser():
    try:
        # ini juga sama
        user['userid'] = request.json['userid']
        user['name'] = request.json['name']
        user['no_telp'] = request.json['no_telp']
        user['pin'] = request.json['pin']
        user['updated_at'] = request.json['updated_at']

        response = jsonify({'id' : user['userid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create user'})
        response.status_code = 400
    finally:
        return 'page not found'

@user.route('/createuser/<string:user_id>', methods=['GET'])
def newuser(user_id): #/createuser/2c535c8b-5d2b-4a72-9268-1c83aaf61902
    try:
        # ini bisa.
        if user_id == '2c535c8b-5d2b-4a72-9268-1c83aaf61902':
            response = jsonify({'user': 'Daniella'})
            response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to get user'})
        response.status_code = 400
    finally:
        return 'page not found'

@user.route('/user', methods=['DELETE'])
def deleteuser():
    # belom di tes
    return jsonify({'mesage' : 'deleting the user that you want'})

if __name__ == "__main__":
    user.run(debug=True)
