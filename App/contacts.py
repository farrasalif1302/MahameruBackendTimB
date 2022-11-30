from flask import Flask, jsonify, request
import uuid
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from db import *

contact = Blueprint('contact', __name__,
                        template_folder='templates')

app = Flask(__name__)

contact = {
    "_id": '',
    'userid': '',
    'name': '',
    'created_at': '',
    'updated_at': ''
}

# contacts
@app.route('/contacts', methods=['GET'])
def getuser():
    try:
        contact['_id'] + '3'
        contact['userid'] = '3'
        contact['name'] = 'Daniella'
        contact['created_at'] = '22/11/2022'
        contact['updated_at'] = ''
        response = jsonify(contact)
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return response


@app.route('/createcontact', methods=['PUT'])
def getuser():
    try:
        contact['_id'] = request.json['_id']
        contact['userid'] = request.json['userid']
        contact['name'] = request.json['name']
        contact['created_at'] = request.json['created_at']
        contact['updated_at'] = request.json['updated_at']

        response = jsonify(contact)
        response.status_code = 200
        response= jsonify({'id': contact['userid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return response



@ app.route('/delcon', methods=['DELETE'])
def deleteUser():
        return jsonify({'mesage': 'deleting the contact that you want'})


if __name__ == "__contacts_":
    app.run(debug=True)
