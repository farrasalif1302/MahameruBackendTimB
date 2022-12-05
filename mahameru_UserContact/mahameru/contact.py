from flask import Flask, jsonify, request, current_app
import uuid
import datetime
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mahameru.db import *

contact = Blueprint('contact', __name__,
                        template_folder='templates')


# placeholder data


# contact 
@contact.route('/get', methods=['GET'])
def getcontact():
    try:
        # kalau variabel contact = {} diapus, makan akan dapet response {'message': 'Failed to create contact'}
        # jadi kesalahannya itu belom nyambung ke mongodb
        current_app.logger.debug("test")
        contact = {}
        contact['contactid'] = 3
        contact['name'] = 'Daniella'
        contact['no_telp'] = '6287885728208'
        contact['pin'] = '1234'
        contact['created_at'] = '12/2/2022'
        contact['updated_at'] = ''
        contact['contact_id'] = 2
        current_app.logger.debug(contact)
        response = jsonify(contact)
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return response


# TODO : fix this so it match with the given docs
@contact.route('/createcontact', methods=['POST'])
def createcontact():
    try:
        # ini juga sama. kalau nambahin variabel contact = {}, baru bisa di run.
        # sama kek tadi, tinggal konekin ke mongodbnya.
        contact['name'] = request.json['contact']
        contact['no_telp'] = request.json['no_telp']
        contact['pin'] = request.json['pin']
        contact['created_at'] = request.json['created_at']
        contact['updated_at'] = request.json['updated_at']
        contact['contactid'] = uuid.uuid4()

        response = jsonify({'id' : contact['contactid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to create channnel'})
        response.status_code = 400
    finally:
        return response

# TODO : dont modify it unt ill the above route is fixed
@contact.route('/createcontact', methods=['PUT'])
def editcontact():
    try:
        # ini juga sama
        contact['contactid'] = request.json['contactid']
        contact['name'] = request.json['name']
        contact['no_telp'] = request.json['no_telp']
        contact['pin'] = request.json['pin']
        contact['updated_at'] = request.json['updated_at']

        response = jsonify({'id' : contact['contactid']})
        response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Failed to create contact'})
        response.status_code = 400
    finally:
        return 'page not found'

@contact.route('/createcontact/<string:contact_id>', methods=['GET'])
def newcontact(contact_id): #/createcontact/2c535c8b-5d2b-4a72-9268-1c83aaf61902
    try:
        # ini bisa.
        if contact_id == '2c535c8b-5d2b-4a72-9268-1c83aaf61902':
            response = jsonify({'contact': 'Daniella'})
            response.status_code = 200
    except Exception as e:
        print(e)
        response = jsonify({'message' : 'Failed to get contact'})
        response.status_code = 400
    finally:
        return 'page not found'

@contact.route('/contact', methods=['DELETE'])
def deletecontact():
    # belom di tes
    return jsonify({'mesage' : 'deleting the contact that you want'})

if __name__ == "__main__":
    contact.run(debug=True)
