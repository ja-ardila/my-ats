from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from views import *
from os import environ
from models import db

def create_flask_app():
    dbURL = "postgresql://{}:{}@{}:{}/{}".format(environ.get('DB_USER', ""), environ.get('DB_PASSWORD', ""), 
                      environ.get('DB_HOST', ""), environ.get('DB_PORT', ""), environ.get('DB_NAME', ""))
    if dbURL == "postgresql://:@:/":
        dbURL = 'sqlite:///my_ats.db'
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = dbURL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()
    endpoints(app)

    return app

def endpoints(app):
    api = Api(app)
    #api.add_resource(UsersView, '/users')


app = create_flask_app()
db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=3000)