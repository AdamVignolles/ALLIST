import pymongo
import datetime
import random

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
    
    def create_code(self, num):
        nums = "0123456789"
        id_num = num
        id = ""
        for i in range(id_num):
            id += nums[random.randint(0, len(nums)-1)]
        return int(id)

    def create_liste(self, name, user):
        creator = user['user']
        name_liste = name
        watchers = {}
        content = ""
        code = str(self.create_code(4))
        user_id = user['_id']
        listes = self.db["listes"]
        run = True
        while run:
            liste_id = self.create_code(15)
            if listes.find_one({"_id": liste_id}) == None:
                run = False

        listes.insert_one({"_id": liste_id, "creator": creator, "name": name_liste, "watchers": watchers, "content": content, "code": code})

    def get_user_listes(self, user):
        listes = self.db["listes"].find({"creator": user['user']})
        l = []
        for liste in listes:
            l.append(liste)

        liste = {"name" : "create a new liste"}
        l.append(liste)
        all_listes = []
        # create liste of 5 liste in listes
        waiting_listes = []
        for liste in l:
            waiting_listes.append(liste)
            if len(waiting_listes) == 5:
                all_listes.append(waiting_listes)
                waiting_listes = []
        if len(waiting_listes) != 0:
            all_listes.append(waiting_listes)
        print(all_listes)
        return all_listes


        
    


if __name__ == "__main__":
    m = ManageUser()
    #m.insert_user("test", "test",  "test@gmail.com")
    for user in m.get_user("test"): print(user)
    for user in m.get_user_by_email("test@gmil.com"): print(user)
    for user in m.get_user_by_email_and_password("test@gmail.com", "test") : print(user)
    for user in m.get_user_by_name_and_password("test", "test") : print(user)

    print(m.get_user_by_email('adam'))

    m.create_liste("test", m.get_user_by_email('adam.vignolles@gmail.com')[0])