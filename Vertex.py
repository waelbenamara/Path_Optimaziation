import uuid
from Edge import Edge

class Vertex:
	def __init__(self,name):
		self.name = name
		self.id = uuid.uuid1()
		self.adjacents = [self]
		self.edges = []

	def add_adjacent(self,vertex,weight):
		edge = Edge(self,vertex,weight)
		self.edges.append(edge)
		self.adjacents.append(vertex)
		vertex.adjacents.append(self)

	def is_adjacent(self,vertex):
		result = False
		for x in self.adjacents:
			if vertex == x:
				result = True
		return result






