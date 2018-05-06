from FlowGraph import FlowGraph
from Node import Node
from Edge import Edge

startNode = Node('S')
a = Node('a')
b = Node('b')
c = Node('c')
endNode = Node('E')

startNode.addEdge(a,5)
startNode.addEdge(b,10)
startNode.addEdge(c,5)

a.addEdge(endNode,10)
b.addEdge(endNode,5)
c.addEdge(endNode,10)

flow = FlowGraph(startNode,endNode)

flow.addNode(a)
flow.addNode(b)
flow.addNode(c)

for node in flow.nodeList:
    print("Node: " + node.name + '\n')
