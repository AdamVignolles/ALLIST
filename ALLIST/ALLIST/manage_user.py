import pymongo
import datetime

class ManageUser:
    def __init__(self):
        uri = "mongodb+srv://admin:admin@cluster0.65u1dbk.mongodb.net/?retryWrites=true&w=majority"

        self.client = pymongo.MongoClient(uri)
        self.db = self.client["allist"]
        self.collection = self.db["users"]

    def insert_user(self, user, password, email):
        self.collection.insert_one({"user": user, "password": password, "email": email, "date": datetime.datetime.utcnow()})
        print("user inserted")

    def get_user(self, user):
        return self.collection.find({"user": user})
    
    def get_user_by_email(self, email):
        return self.collection.find({"email": email})
    
    def get_user_by_email_and_password(self, email, password):
        return self.collection.find({"email": email, "password": password})
    
    def get_user_by_name_and_password(self, user, password):
        return self.collection.find({"user": user, "password": password})
    


if __name__ == "__main__":
    m = ManageUser()
    #m.insert_user("test", "test",  "test@gmail.com")
    for user in m.get_user("test"): print(user)
    for user in m.get_user_by_email("test@gmil.com"): print(user)
    for user in m.get_user_by_email_and_password("test@gmail.com", "test") : print(user)
    for user in m.get_user_by_name_and_password("test", "test") : print(user)

    print(m.get_user_by_email('adam'))