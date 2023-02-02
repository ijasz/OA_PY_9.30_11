import pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb+srv://OA:QPHVdMYiHiKmnx5k@cluster0.2idklaw.mongodb.net/?retryWrites=true&w=majority")

db = client["database"]

users = db["Users"]

courses = db["Courses"]

# data = [
#     {"name": "lll", "age": 10},
#     {"name": "aaa", "age": 11},
#     {"name": "yyy", "age": 12}
# ]

# ***********insert***********

# users.insert_one({"name": "xxx", "age": 10})

# users.insert_many(data)

# courses.insert_one(
#     {"courseId": "PY", "courseName": "Python", "courseCost": 5000})

# *********find**********

# id = input("please enter your id to check your details : ")

# print(courses.find_one({"_id": ObjectId(id)}, {"courseName": 1}))

# for i in users.find():
#     print(i)

# ******query*****

# myquery = {"age": 10}

# mydoc = users.find(myquery, {"name": 1})

# for i in mydoc:
#     print(i)

# myquery = {"age": {"$gte": 10}}
# myquery = {"name": {"$gt": "x"}}

# mydoc = users.find(myquery)

# for x in mydoc:
#     print(x)

# ****sort *****

mydoc = users.find().sort("name")

for x in mydoc:
    print(x)
