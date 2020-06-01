import json
class Temp():
	"""docstring for Temp"""
	def __init__(self,start,end,agent):
		self.start = start
		self.end = end
		self.agent = agent
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
		
		