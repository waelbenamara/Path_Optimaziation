from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydb']

#Creating a collection
collection = db['example']
print("Collection created........")

doc1 = {"name": "Ram", "age": "26", "city": "Hyderabad"}
collection.insert_one(doc1)
print(collection.find_one())