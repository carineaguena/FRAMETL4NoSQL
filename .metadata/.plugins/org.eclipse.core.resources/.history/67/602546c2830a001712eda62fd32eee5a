'''
Created on 14 de mar de 2017

@author: carineaguena
'''

from NoSQL_Invetory.SchemaData import SchemaData

class SchemaDataGraph(SchemaData):
    
    def __init__(self, name, describe):
        self.edges = []
        self.vertices = []
        self.name = name
        self.describe = describe
    
    def getSchema(self, name):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    def addEdges(self, edge):
        self.edges.append(edge)
        
    def addVertices(self, vertice):
        self.vertices.append(vertice)