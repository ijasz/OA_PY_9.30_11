import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://Ijass:nROzWTrrlGw3bl9V@cluster0.u49gmjr.mongodb.net/?retryWrites=true&w=majority")
db = client["py"]
users = db["users"]

name = input("enter your name")


users.insert_one({"name": name})
