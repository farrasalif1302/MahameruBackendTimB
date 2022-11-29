import os
from flask import Flask, render_template
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_pyfile('settings.cfg', silent=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    @app.route('/')
    def index():
        print("test")
        return "Here's the page"


    return app
