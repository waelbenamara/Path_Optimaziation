from collections import defaultdict
from Graph import Graph
from Delivery import Delivery
from Optimizer import Optimizer
from Agent import Agent
import json
from io import BytesIO 
import pickle
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



for edge in edges:
    graph.add_edge(*edge)

d_1 = Delivery('TUNIS','SFAX', graph)
d_2 = Delivery('TUNIS','ARIANA', graph)

d_1.set_optimized_path()
d_2.set_optimized_path()
print(d_1.optimized_path)

agent_1 = Agent("Moshen")
agent_2 = Agent("Salah")

agent_1.add_delivery(d_1)
agent_2.add_delivery(d_2)

agents = [agent_2,agent_1]
agent_1.set_stops()
agent_2.set_stops()

new_del = Delivery('SOUSSE','MAHDIA',graph)
new_del.set_optimized_path()

op = Optimizer(agents, graph)
op.squeeze_2(new_del)

for a in agents:
    print(a.name)
    print(a.stops)
'''
new_del_2 = Delivery('TUNIS','SIDIBOU',graph)
new_del_2.set_optimized_path()
op.squeeze_2(new_del_2)

for a in agents:
    print(a.name)
    print(a.stops)
'''    
'''
def my_dict(obj):
    if not  hasattr(obj,"__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(my_dict(item))
        else:
            element = my_dict(val)
        result[key] = element
    return result
hh = my_dict(new_del)    
a= pickle.dumps(new_del)
print(a)

b = pickle.loads(a)
print(b)
#def write_in_db():
'''