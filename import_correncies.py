from pymongo import MongoClient
client = MongoClient ("localhost", 27017)
db = client["countries_db"]
collection_currency = db["currency"]


import json
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["countries_db"]
collection_currency = db["currency"]

with open("currencies.json") as f:
file_data = json.load(f)

collection_currency.insert(file_data)
client.close()
