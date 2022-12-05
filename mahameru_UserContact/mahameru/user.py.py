from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
import uuid

'''Channel = {
    '_id' : '',
    'owner_id' : '',
    'members_id' : '',
    'name': '',
    'description: '',
    'created_at': '',
    'updated_at': '',
}'''

app = Flask(__name__)
app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/mahamerudb"
mongo = PyMongo(app)

@app.route('/createuser',methods=['POST']) # KELAR
def add_user():
    _json = request.json
    _userid = _json['userid']
    _name = _json['name']
    _nickname=_json['nickname']
    _notelp=_json['notelp']
    _pin = _json['pin']
    createdat = _json['created_at']
    contactid = _json['contact_id']

    if _userid and _name and _nickname and _notelp and _pin and createdat and contactid and request.method == "POST":
        _id = mongo.db.user.insert_one({"userid": _userid, "name": _name, "nickname": _nickname ,"notelp": _notelp, "pin" : _pin, "created_at" : createdat,  "contact_id" : contactid })
        resp = jsonify("User was successfully added")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/update/<id>',methods=['PUT']) # jadiin update user
def update_user(id):
    _id = id
    _json = request.json
    _userid = _json['userid']
    _name = _json['name']
    _nickname=_json['nickname']
    _notelp=_json['notelp']
    _pin = _json['pin']
    createdat = _json['created_at']
    contactid = _json['contact_id']

    if _userid and _name and _nickname and _notelp and _pin and createdat and contactid and request.method == "POST":
        _id = mongo.db.user.update_one({"userid": _userid, "name": _name, "nickname": _nickname ,"notelp": _notelp, "pin" : _pin, "created_at" : createdat,  "contact_id" : contactid })
        resp = jsonify("User updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/getuser') #tampilin user (kelar)
def user_all():
    user = mongo.db.user.find()
    resp = dumps(user)
    return resp

@app.route('/user/<id>') # tampilin user sesuai dengan user ID
def user_one(id):
    user = mongo.db.user.find_one({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/delete/<id>',methods=['DELETE']) # hapus user sesuai dengan user ID
def delete_user(id):
    mongo.db.user.delete_one({'id':ObjectId(id)})
    resp = jsonify("user deleted successfully")
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run(debug=True)