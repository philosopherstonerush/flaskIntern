from database.db import mongodb
from bson.objectid import ObjectId

class User:

    def __init__(self):
        self.db = mongodb.db

    def getUsers(self):
        users = self.db.userCRUD.find()
        data = []
        for user in users:
            item = {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
            }
            data.append(item)
        return data

    def createUser(self, user):
        result = self.db.userCRUD.insert_one(user)
        return result.inserted_id

    def updateUser(self, userUpdateInfo, id):
        response = self.db.userCRUD.update_one(
            {"_id": ObjectId(id)},
            {"$set": userUpdateInfo}
        )

        if response.matched_count:
            return response.upserted_id
        else:
            return None
        
    def findUser(self, id):
        user = self.db.userCRUD.find_one({"_id": ObjectId(id)})
        return user
    
    def delUser(self, id):
        response = self.db.userCRUD.delete_one({"_id": ObjectId(id)})

        if response.deleted_count:
            return True
        else:
            return False