import click
import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    mongocon = current_app.config['MONGO_CON']
    dbclient = pymongo.MongoClient(mongocon)
    g.db = dbclient[current_app.config['DATABASE']]
    return g.db

def get_collection(colname):
    if 'db' not in g:
        get_db()
    return g.db[colname]

"""
Helper function to query all user on system 
"""
def get_users(filter={}):
    collection = get_collection("user")
    return collection.find(filter)

def get_user(filter={}):
    collection = get_collection("user")
    return collection.find_one(filter)

def create_user(data):
    collection = get_collection("user")
    row = collection.create_one(data)
    return row

def update_user(filter, update):
    collection = get_collection("user")    
    return collection.update_one(filter, update)    

def delete_user(data):
    collection = get_collection("user")
    collection.delete_one(data)

def contact_id(User={}):
    collection = contact_id("kontak")
    return collection.find(User)

def User_id(UserContact={}):
    collection = get_collection("id user")
    return collection.find(UserContact)

def Created_at(UserContact={}):
    collection = get_collection("dibuat")
    return collection.created_one(UserContact)

def Updated_at(UserContact={}):
    collection = get_collection("diupdate")
    row = collection.update_one(UserContact)
    return row
    
def close_db(e=None):
    db = g.pop(current_app.config['DATABASE'], None)
    if db is not None:
        db.close()
        
def init_db():
    """clear the existing data and create new tables."""    
    db = get_db()    
    db.client.drop_database(current_app.config['DATABASE'])
    
@click.command('init-db')
@with_appcontext
def init_db_command():    
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

