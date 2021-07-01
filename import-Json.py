# este si importa un json a mongodb
import json
from pymongo import MongoClient


myclient = MongoClient('localhost',27017,username="root",password="root")

db = myclient['pru']

Collection = db['temp']

with open('data.json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

