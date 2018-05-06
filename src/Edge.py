#
# Edge.py
# Authors:
#   Sergio Corral
#
class Edge:
    def __init__(self, start, end, capacity):
        self.nodeStart = start
        self.nodeEnd = end
        self.edgeCapacity = capacity
        self.currentFlow = 0