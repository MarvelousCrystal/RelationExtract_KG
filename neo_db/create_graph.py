from config import graph
from py2neo import Graph,Node,Relationship
# graph = Graph(
#     "http://localhost:7474",
#     username="neo4j",
#     password="123456"
# )
with open(r"../raw_data/result.txt",encoding='utf-8') as f:
    for line in f.readlines():
        resultarray = line.strip("\n").split(",")
        # 覆盖式创建节点
        start_node = Node("Person",name=resultarray[0])
        end_node = Node("Person", name=resultarray[1])
        relation = Relationship(start_node,resultarray[2],end_node)
        graph.merge(start_node, 'Person', 'name')
        graph.merge(end_node, 'Person', 'name')
        graph.merge(relation, 'Person', 'name')
        relation = Relationship(end_node, resultarray[2], start_node)
        graph.merge(start_node, 'Person', 'name')
        graph.merge(end_node, 'Person', 'name')
        graph.merge(relation, 'Person', 'name')