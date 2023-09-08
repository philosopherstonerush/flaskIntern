from flask_restful import Resource
from flask import Response, request
from database.models import User
import resources.helpers as helpers
from werkzeug.security import generate_password_hash
import json

class UsersApi(Resource):
    def __init__(self):
        super().__init__()
        self.userDB = User()

    def get(self):
        data = json.dumps(self.userDB.getUsers())
        
        return Response(data)
    
    def post(self):
        content = request.get_json()
        validUser = helpers.validateCreateUser(content)

        if validUser:
            password = generate_password_hash(content["password"])
            user = {
                "name": content["name"],
                "email": content["email"],
                "password": password
            }
            insertedID = self.userDB.createUser(user)

            return Response(json.dumps({"id": str(insertedID)}), status=200)
        else:
            return Response(status=400)
        
class UserApi(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.userDB = User()

    def get(self, id):

        user = self.userDB.findUser(id)

        if user:
            user["_id"] = str(user["_id"])
            del user["password"]
            return Response(
                json.dumps(user),
                status=200
            )
        else:
            return Response(
                status=400
            )
    
    def put(self, id):
        content = request.get_json()

        validUpdate = helpers.validateUpdateUser(content)

        if validUpdate:
            updated = self.userDB.updateUser(content, id)
            if updated != None:
                return Response(
                    json.dumps({"id": str(updated)}),
                    status=200
                )
            else:
                return Response(
                    status=400
                )
        else:
            return Response(
                status=400
            )
        
    def delete(self, id):
        deleted = self.userDB.delUser(id)
        if deleted:
            return Response(
                status=200
            )
        else:
            return Response(
                status=400
            )
