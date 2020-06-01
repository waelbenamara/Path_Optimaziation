from pymongo import MongoClient
import pickle
#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydb']

#Creating a collection
coll = db['deliveries']

doc = coll.find()
'''
my_object = doc['value']
my_object = pickle.loads(my_object)
print(my_object)
'''
for x in coll.find():
  print(x)