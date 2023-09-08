from flask_pymongo import PyMongo

mongodb = PyMongo()

def initialize_db(app):
    
    mongodb.init_app(app)