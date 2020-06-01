from Delivery import Delivery
import numpy as np 
class Agent:
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



