import numpy as np
class Optimizer:
	def __init__(self,agents,graph):
		self.agents = agents
		self.graph = graph

	def add_agent(self,agent):
		self.agents.append(agent)
		

	def get_delivery_cost(delivery_path):
		cost = 0

	

	def squeeze(self,incoming_delivery):
		def subset_test(a, b):
		    b = iter(b)
		    try:
		        for i in a:
		            j = next(b)
		            while j != i:
		                j =next(b)
		    except StopIteration:
		        return False
		    return True
		all_deliveries_paths = []
		all_deliveries = []
		for agent in self.agents:
			for delivery in agent.deliveries:
				all_deliveries_paths.append(delivery.optimized_path)
				all_deliveries.append(delivery)
		incoming_delivery_path = incoming_delivery.optimized_path
		incoming_delivery_cost = 0
		for x in range(len(incoming_delivery_path)-1):
			a = incoming_delivery_path[x]
			b = incoming_delivery_path[x+1]
			incoming_delivery_cost = incoming_delivery_cost + self.graph.weights[(a,b)]
		all_lengths = []
		for delivery in all_deliveries:
			all_lengths.append(len(delivery.optimized_path))
		#print(all_deliveries_paths)
		if len(incoming_delivery.optimized_path) > np.max(np.array(all_lengths)):
			#all_deliveries.append(incoming_delivery_path)
			#print("new delivery was added to list")
			for delivery in all_deliveries:
				if (subset_test(incoming_delivery.optimized_path,delivery.optimized_path) == True) :
					delivery.stations.insert(0,incoming_delivery.optimized_path[len(incoming_delivery.optimized_path)-1])
					#print("Station updated")

					break;
				else :
					all_deliveries.append(incoming_delivery)
					self.agents[1].deliveries.append(incoming_delivery)

					#print("new delivery was added to list_")
					break;

		else:
			for delivery in all_deliveries:
				if subset_test(incoming_delivery.optimized_path,delivery.optimized_path) == True :
					delivery.stations.insert(0,incoming_delivery.optimized_path[len(incoming_delivery.optimized_path)-1])
					#print("Station updated")
					break;
				else :
					all_deliveries.append(incoming_delivery)
					self.agents[1].deliveries.append(incoming_delivery)
					#print("new delivery was added to list")
					break;
		
		
		



		"""
		for element in all_deliveries_paths:
			all_lengths.append(len(element))
		if len(incoming_delivery_path) > np.max(np.array(all_lengths)):
			all_deliveries_paths.append(incoming_delivery_path)
			print("new delivery was added to list")
			#optimize
		else:
			for path in all_deliveries_paths:
				if subset_test(incoming_delivery_path,all_deliveries_paths) == True:
					incoming_delivery_path.append

		"""

		

	def squeeze_2(self,new_delivery):
		def subset_test(a, b):
		    b = iter(b)
		    try:
		        for i in a:
		            j = next(b)
		            while j != i:
		                j =next(b)
		    except StopIteration:
		        return False
		    return True
		print("new delivery", new_delivery.optimized_path)
		for agent in self.agents:
			for delivery in agent.deliveries:
				print(delivery.optimized_path)
				if subset_test(new_delivery.optimized_path,delivery.optimized_path):
					agent.stops.insert(0,new_delivery.optimized_path[len(new_delivery.optimized_path)-1])
					print("stop added to agent ",agent.name)
					return agent
					break;
				elif subset_test(delivery.optimized_path,new_delivery.optimized_path):
					agent.stops.insert(0,new_delivery.optimized_path[len(new_delivery.optimized_path)-1])
					agent.deliveries.remove(delivery)
					agent.deliveries.append(new_delivery)
					print("Deliveries array updated for agent ",agent.name)
					return agent
					break;
				else:
					return None







	





