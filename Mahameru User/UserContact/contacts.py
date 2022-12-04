from flask import Flask, jsonify, request
import uuid
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from UserContact.db import *
from bson.objectid import ObjectId

bp = Blueprint('bp', __name__,
                        template_folder='templates')


'''bp = {
    "_id": '',
    'userid': '',
    'name': '',
    'created_at': '',
    'updated_at': ''
}'''

# bps
@bp.route('/contact', methods=['GET'])
def getuser():
    try:
        bp = {}
        bp['_id'] + '3'
        bp['userid'] = '3'
        bp['name'] = 'Daniella'
        bp['created_at'] = '22/11/2022'
        bp['updated_at'] = ''
        response = get_contacts(bp)
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return response


@bp.route('/createcontact', methods=['PUT'])
def getUser():
    try:
        bp = {}
        bp['_id'] = request.json['_id']
        bp['userid'] = request.json['userid']
        bp['name'] = request.json['name']
        bp['created_at'] = request.json['created_at']
        bp['updated_at'] = request.json['updated_at']

        response = insert_contacts(bp)
        response.status_code = 200
        response= jsonify({'id': bp['userid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return response



@ bp.route('/delcon', methods=['DELETE'])
def deleteUser():
        row = delete_contacts({"_id": row.inserted_id})
        return jsonify({'mesage': 'deleting the contact that you want'})


if __name__ == "__contact_":
    bp.run(debug=True)