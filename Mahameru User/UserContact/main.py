from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# placeholder data
user = {
    'userid': '',
    'name': '',
    'no_telp': '',
    'pin': '',
    'created_at': '',
    'updated_at': '',
    'contact_id': ''
}

# User 
@app.route('/user', methods=['GET'])
def getuser():
    try:
        user['userid'] = 3
        user['name'] = 'Daniella'
        user['no_telp'] = '0878987654321'
        user['pin'] = '123456'
        user['created_at'] = '22/11/2022'
        user['updated_at'] = ''
        user['contact_id'] = 2
        response = jsonify(user)
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create user'})
        response.status_code = 400
    finally:
        return response

# TODO : fix this so it match with the given docs
@app.route('/createuser', methods=['POST'])
def createUser():
    try:
        # for testing purpose only getting one request json
        user['name'] = request.json['user']
        user['no_telp'] = request.json['no_telp']
        user['pin'] = request.json['pin']
        user['created_at'] = request.json['created_at']
        user['userid'] = uuid.uuid4()

        response = jsonify({'id' : user['userid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to create user'})
        response.status_code = 400
    finally:
        return response
    
# TODO : dont modify it untill the above route is fixed
@app.route('/createuser', methods=['PUT'])
def editUser():
    try:
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
