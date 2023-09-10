from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from database.db import initialize_db


# Connecting to the docker mongo instance
app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://test_users:27017/user"

initialize_db(app)

initialize_routes(api)