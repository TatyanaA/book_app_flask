# save this as app.py
# from flask import Flask, request
# from markupsafe import escape
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)
# app.json_provider_class.sort_keys = False
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://iqsyuxrn:DbGQEUu7wC4BmEvOkfEuM0bId12CrbnN@tyke.db.elephantsql.com/iqsyuxrn'
# app.config['SQLALCHEMY_DATABASE_URI']=os.
# db=SQLAlchemy(app)
# from application import routes

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app(env=None):
    load_dotenv()
    app = Flask(__name__)
    app.json_provider_class.sort_keys = False
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
    
    db.init_app(app)
    app.app_context().push()

    from application.routes import books
    app.register_blueprint(books)

    from application.books.routes import books2
    app.register_blueprint(books2)

    return app
    # from application import routes
