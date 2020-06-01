from flask import Flask, request, render_template, send_from_directory,jsonify,Response
import os
import json
from pymongo import MongoClient
import pickle
from Temp import Temp
from Temp_arr import Temp_arr
from Graph import Graph

app = Flask(__name__)

from collections import defaultdict
from Graph import Graph
from Delivery import Delivery
from Optimizer import Optimizer
from Agent import Agent


graph = Graph()

edges = [
   ('TATAOUINE','MEDENINE',50),
('TATAOUINE','KEBILI',242),
('MEDENINE','KEBILI',192),
('MEDENINE','GABES',77),
('KEBILI','GABES',115),
('KEBILI','TOZEUR',98),
('KEBILI','GAFSA',191),
('GABES','GAFSA',134),
('GABES','SFAX',133),
('GABES','SIDIBOUZID',191),
('TOZEUR','GAFSA',93),
('GAFSA','KASSERINE',197),
('GAFSA','SIDIBOUZID',160),
('SFAX','MAHDIA',104),
('SFAX','SIDIBOUZID',125),
('SFAX','KAIROUANE',136),
('MAHDIA','MONASTIR',44),
('MAHDIA','SOUSSE',61),
('MAHDIA','KAIROUANE',111),
('MONASTIR','SOUSSE',25),
('SOUSSE','KAIROUANE',68),
('SOUSSE','ZAGHOUANE',85),
('SOUSSE','NABEUL',96),
('KASSERINE','SIDIBOUZID',10),
('KASSERINE','SILIANA',235),
('KASSERINE','ELKEF',128),
('SIDIBOUZID','KAIROUANE ',130),
('SIDIBOUZID ','SILIANA',191),
('KAIROUANE ','SILIANA ',119),
('KAIROUANE ','ZAGHOUANE',100),
('SILIANA ','ELKEF',91),
('SILIANA ','ZAGHOUANE ',99),
('SILIANA ','JENDOUBA',122),
('SILIANA ','BEJA',101),
('ELKEF','JENDOUBA',59),
('ZAGHOUANE ','BEJA',121),
('ZAGHOUANE ','NABEUL',57),
('ZAGHOUANE ','MANOUBA',54),
('JENDOUBA','BEJA',45),
('BEJA','BIZERTE',102),
('BEJA','MANOUBA',105),
('BIZERTE','MANOUBA',78),
('NABEUL','BENAROUS',65),
('BENAROUS','MANOUBA ',23),
('MANOUBA','ARIANA',14),
('ARIANA','BIZERTE',65),
('TUNIS','BENAROUS ',11),
('TUNIS','ARIANA',11),
('TUNIS','MANOUBA',10)
]



client = MongoClient('localhost', 27017)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

graph = Graph()



agent_1 = Agent("Moshen")
agent_2 = Agent("Ali")
agents = [agent_1,agent_2]

for edge in edges:
    graph.add_edge(*edge)



@app.route("/",methods=['POST','GET'])
def main() :

	return "Server is Active"

@app.route("/optimize",methods=['POST','GET'])
def optimize() :
	#loaaaadd from db
	db = client['mydb']
	coll = db['deliveries']
	coll.delete_many({})
	doc = coll.find()
	for x in doc:
		try:
			#print(x)
			print("========================")
			my_del = x['value']
			my_del = pickle.loads(my_del)
			print("start:", my_del.start)
			print("end:", my_del.end)
			my_del.set_optimized_path()
			print(my_del.agent)
			print("paths", my_del.optimized_path)
			print("========================")
			'''
			if my_del.agent.name == "Mohsen":
				agent_1.add_delivery(my_del)
			elif my_del.agent.name == "Ali":
				agent_2.add_delivery(my_del)
			'''
		except Exception as e:
			print(e)
			continue

	print(doc)
	data = request.get_json()
	d = Delivery(data['start'],data['end'], graph)
	d.set_optimized_path()
	print(data)
	op = Optimizer(agents, graph)
	result = op.squeeze_2(d)
	print("result ", result)
	if result != None:
		res = "delivery assigned to " + result.name
	else :
		res =" Could not assign this delivery to any agent" 

	return jsonify({"path":d.optimized_path,"res":res})


@app.route("/get_shortest_path",methods=['POST','GET'])
def get_shortest_path() :
	data = request.get_json()
	d = Delivery(data['start'],data['end'], graph)
	d.set_optimized_path()
	print(data)
	return jsonify({"path":d.optimized_path})

@app.route("/add_delivery",methods=['POST','GET'])
def add_delivery() :
	data = request.get_json()
	print(data)
	start = data['start']
	end = data['end']
	agent = data['agent']

	d_1 = Delivery(start,end,graph)
	d_1.set_optimized_path()

	if agent == "Mohsen":
		agent_1.add_delivery(d_1)
	if agent == "Ali":
		agent_2.add_delivery(d_1)
	d_1.insert_in_db()

	return "ok"

@app.route("/get_deliveries",methods=['POST','GET'])
def get_deliveries() :
	db = client['mydb']
	coll = db['deliveries']
	doc = coll.find()
	temp_arr = Temp_arr()
	for x in coll.find():
		try:
			print(x)
			my_del = x['value']
			my_del = pickle.loads(my_del)
			start = my_del.start
			end = my_del.end
			agent = my_del.agent.name
			temp = Temp(start,end,agent)
			temp_arr.data.append(temp)
		except Exception as e:
			print(e)
			continue
	all_deliveries = temp_arr.toJSON()
	print(all_deliveries)
	return all_deliveries

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port=8081,threaded = True)

