from Vertex import Vertex
from Path import Path
from pymongo import MongoClient
import pickle
class Delivery:
	def __init__(self,start,end,graph):
		self.start = start
		self.end = end 
		self.graph = graph
		self.optimized_path = None
		self.stations = [self.end]
		self.agent = None
		self.cost = 0


	def set_optimized_path(self):
		self.optimized_path =  self.graph.get_shortest_path(self.start,self.end)


	def get_delivery_cost(self):
		delivery_cost = 0
		for x in range(len(self.optimized_path)-1):
			a = self.optimized_path[x]
			b = self.optimized_path[x+1]
			delivery_cost = delivery_cost + self.graph.weights[(a,b)]
		self.cost = delivery_cost
		return self.cost

	def insert_in_db(self):
		client = MongoClient('localhost', 27017)
		db = client['mydb']
		coll = db['deliveries']
		document = {"value":pickle.dumps(self)}
		coll.insert_one(document)


