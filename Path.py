class Path:
	def __init__(self,start,end,graph):
		self.start = start 
		self.end = end
		self.shortest_path = [] 
		self.graph = graph  
		


	def get_shortest_path(self):
		shortest_paths = {initial: (None, 0)}
		current_node = initial
		visited = set()
		while current_node != end:
			visited.add(current_node)
			destinations = selfgraph.edges[current_node]
			weight_to_current_node = shortest_paths[current_node][1]

			for next_node in destinations:
				weight = self.graph.weights[(current_node, next_node)] + weight_to_current_node
				if next_node not in shortest_paths:
					shortest_paths[next_node] = (current_node, weight)
				else:
					current_shortest_weight = shortest_paths[next_node][1]
					if current_shortest_weight > weight:
						shortest_paths[next_node] = (current_node, weight)
	        
			next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
			if not next_destinations:
				return "Route Not Possible"
	        # next node is the destination with the lowest weight
			current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
		path = []
		while current_node is not None:
			path.append(current_node)
			next_node = shortest_paths[current_node][0]
			current_node = next_node
	    # Reverse path
		path = path[::-1]
		self.shortest_path = path
	    
