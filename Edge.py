import uuid
class Edge:
	def __init__(self,vertex_1,vertex_2,weight):
		self.id = uuid.uuid1()
		self.vertex_1 = vertex_1
		self.vertex_2 = vertex_2
		self.weight = weight
		
