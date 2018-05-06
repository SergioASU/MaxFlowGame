#
# Node.py
# Authors:
#   Sergio Corral
#

from Edge import Edge
class Node:
    def __init__(self,name):
        self.edgeList = []
        self.name = name
    
    def addEdge(self, nodeEnd,capacity):
        newEdge = Edge(self,nodeEnd,capacity)
        self.edgeList.append(newEdge)
