import pymongo
from bson import ObjectId


client = pymongo.MongoClient(
    "mongodb+srv://OA:9BOg8NPWvlLt5dmk@cluster0.2idklaw.mongodb.net/?retryWrites=true&w=majority")

db = client["PY"]
users = db["Users"]

# name = input("enter your name")

# users.insert_many([
#     {"name": "rahul", "age": 16, "location": "pondy"},
#     {"name": "prabu", "age": 16, "location": "cuddalore"},
#     {"name": "brathesh", "age": 16, "location": "pondy"},
# ])

id = input("Please your Id to update your data :")


for i in users.find():
    # print(i["_id"])
    if i["_id"] == ObjectId(id):
        print("it matches", i)
        name = input("name change")
        age = int(input("age change"))
        location = input("location change")
        users.update_one({"_id": ObjectId(id)}, {"$set": {
                         "name": name, "age": age, "location": location}})

    # myquery = {"_id": ObjectId('639aa637bd6fcef863b7293a')}
    # newvalues = {"$set": {"location": "london"}}

    # users.update_one(myquery, newvalues)
