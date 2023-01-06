from flask import Flask, jsonify, request, current_app
import uuid
import datetime
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .model.db_chat import *
from flask_pymongo import PyMongo
import datetime

bp = Blueprint('chat', __name__,
                        template_folder='templates')

@bp.route('/getchat/all')
def get_chats():
    chats = get_byAll()
    result = dumps(chats)
    return result

@bp.route('/sendchat', methods=['POST'])
def send_chat():
    date = datetime.datetime.now()
    date_time = date.strftime("%m/%d/%Y, %H:%M:%S")
    json = request.json 
    telp = json['telp']
    from_user = json['from_user']
    message = json['message']
    sent = date_time

    if request.method == "POST":
        _id = sendchat(telp, from_user, message, sent)
        resp = dumps(_id)
        current_app.logger.debug(_id)
        return resp
    else:
        return "Unable to send chat"
    # except:
    #     return "failed to send chat"

@bp.route('/getchat/id')
def chatbyID():
    chat = request.json
    conv = ObjectId(chat)
    chats = getbyID(conv)
    resp = dumps(chats)
    return resp

@bp.route('/getchat/nickname')
def chat_byID():
    nick = {}
    nick['nickname'] = request.json['nickname']
    chats = get_byNick(nick['nickname'])
    resp = dumps(chats)
    return resp

@bp.route('/updatechat/<id>', methods = ['PUT'])
def updatechat(id):
    json = request.json
    chat = {}
    chat["message"] = json['message']
    chat["update_at"] = datetime.datetime.now()

    if json['message']:
        _id = update_chats(id, chat)
        resp = dumps(_id)
        return resp
    else:
        return "Failed to update chat"

@bp.route('/deletechat/<id>', methods=['DELETE'])
def deletechat(id):
    chat = delete_chat(id)
    resp = dumps(chat)
    return resp

@bp.route('/channelmessages/id', methods=['GET'])
def listchannels():
    json = request.json
    channel = json['_id']
    conv = ObjectId(channel)
    chats = get_channel_messages(conv)
    answer = dumps(chats)
    return answer

@bp.route('/getpersonalchat/id', methods=['GET'])
def get_personal_id():
    json = request.json
    to_user = ObjectId(json['to_user'])
    from_user = ObjectId(json['from_user'])
    chats = get_personalChat_id(to_user, from_user)
    answer = dumps(chats)
    return answer

@bp.route('/getpersonalchat/text', methods=['GET'])
def get_personal_text():
    json = request.json
    to_user = json['to_user']
    message = json['message']
    toID = ObjectId(to_user)
    chats = get_personalChat_text(toID, message)
    answer = dumps(chats)
    return answer

if __name__ == "__main__":
    bp.run(debug=True)