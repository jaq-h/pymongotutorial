import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jaq:<PASSWORD>@cluster0.mgtoa.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

document = {"_id": 0, "name":"hello world"}

collection.insert_one(document)