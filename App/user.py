from flask import Flask, jsonify, request
import uuid
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from db import *

app = Blueprint('user', __name__,
                        template_folder='templates')

app = Flask(__name__)

# placeholder data
app = {
    'userid': '',
    'name': '',
    'no_telp': '',
    'pin': '',
    'created_at': '',
    'updated_at': '',
    'contact_id': ''
}

# User 
@app.route('/get', methods=['GET'])
def getuser():
    data = get_user()
    return data

# TODO : fix this so it match with the given docs

@app.route('/createuser', methods=['POST'])
def createuser():
        try:
            # for testing purpose only getting one request json
            app['name'] = request.json['user']
            app['no_telp'] = request.json['no_telp']
            app['pin'] = request.json['pin']
            app['created_at'] = request.json['created_at']
            app['updated_at'] = request.json['updated_at']
            app['userid'] = uuid.uuid4()

            response = jsonify({'id' : app['userid']})
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message' : 'Failed to create channnel'})
            response.status_code = 400
        finally:
            return response

# TODO : dont modify it untill the above route is fixed
@app.route('/createuser', methods=['PUT'])
def editUser():
        try:
            app['userid'] = request.json['userid']
            app['name'] = request.json['name']
            app['no_telp'] = request.json['no_telp']
            app['pin'] = request.json['pin']
            app['updated_at'] = request.json['updated_at']

            response = jsonify({'id' : app['userid']})
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message': 'Failed to create user'})
            response.status_code = 400
        finally:
            return response

@app.route('/createuser/<string:user_id>', methods=['GET'])
def newUser(user_id):
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

@app.route('/user', methods=['DELETE'])
def deleteUser():
    # this code must be fixed after implmenting the database and getting clarity from director
    return jsonify({'mesage' : 'deleting the user that you want'})

if __name__ == "__main__":
        app.run(debug=True)
