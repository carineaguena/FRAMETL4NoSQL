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
    
    def createSchema(self):
        node = raw_input("Insert node value: ")
        edge = raw_input("Insert edge value: ")
        vertice = raw_input("Insert vertice value:")
        self.putColumn([node, edge, vertice])
    