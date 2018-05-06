#
# FlowGraph.py
# Authors:
#   Sergio Corral
#

from Node import Node
class FlowGraph:
    def __init__(self,startNode,endNode):
        self.nodeList = []
        self.start = startNode
        self.end = endNode
    
    def addNode(self,node):
        self.nodeList.append(node)
        