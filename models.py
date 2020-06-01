from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from sqlalchemy.ext.declarative import declarative_base


file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)


taking = db.Table('takers',
	db.Column('delivery_id',db.Integer,db.ForeignKey('delivery.delivery_id')),
	db.Column('agent_id',db.Integer,db.ForeignKey('agent.agent_id'))
	)

class Delivery(db.Model):
	delivery_id  = db.Column(db.Integer,primary_key = True)
	start = db.Column(db.String(100))
	end = db.Column(db.String(100))
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


class Agent(db.Model):
	agent_id = db.Column(db.Integer,primary_key = True)
	def __init__(self,name):
		self.name = name
		self.deliveries = []
		self.costs = []
		self.total_cost = 0
		self.stops = []
		
	def all_paths(self):
		for x in self.deliveries:
			self.paths.append(x.optimized_paths)

	def add_delivery(self,delivery):
		self.deliveries.append(delivery)
		delivery.agent = (self)

	def cost(self):
		for delivery in self.deliveries:
			costs.append(delivery.get_delivery_cost())

	def get_total_cost(self):
		return np.sum(np.array(self.costs))

	def set_stops(self):
		for x in self.deliveries:
			self.stops.insert(0,x.optimized_path[len(x.optimized_path)-1])
		return self.stops


