'''
Created on 14 de mar de 2017

@author: carineaguena
'''

from NoSQL_Invetory.SchemaData import SchemaData

#The common theme among Graph Databases (GDs) is that data is structured in
#a mathematical graph. A graph G=(V,E) generally consists of a set of vertices
#V and a set of edges E. An edge e € E is a pair of vertices (v1, v2) € V x V.
#If the graph is directed, theses pairs are ordered.
#Graph vertices are called nodes, and edges are called relationships.
#Every node contains a set of properties.
####NASHOLM, 2012 - Extracting Data from NoSQL Databases

class SchemaDataGraph(SchemaData):
    
    def __init__(self, name, describe):
        self.edges = []
        self.vertices = []
        self.name = name
        self.describe = describe
        self.nodes = []
    
    def getSchema(self, name):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    def addEdges(self, edge):
        self.edges.append(edge)
        
    def addVertices(self, vertice):
        self.vertices.append(vertice)
        
    def putNodes(self, vertice, edge):
        self.nodes.append(vertice, edge)
        
    def getNodes(self, node):
        index = self.nodes.index(node)
        return self.nodes[index]
    
    def popNodes(self, node):
        self.nodes.pop(self.nodes.index(node))