'''
Created on 14 de mar de 2017

@author: carineaguena
'''
from NoSQL_Invetory.SchemaData import SchemaData

#The data model is based on the abstract data type MAP.
#KVS contains a collection of key-value pairs where all keys are unique.
#Each pair can be queried by key via get operation.
####NASHOLM, 2012 - Extracting Data from NoSQL Databases

class SchemaDataKeyValue(SchemaData):
    
    def __init__(self, name, describe):

        self.name = name
        self.describe = describe
        self.pairs = []
    
    def getSchema(self, name):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    
    def getPairs(self, key):
        index = self.pairs.index(key)
        return self.pairs[index]
               
    def putPairs(self, key, value):
        self.pairs.append(key, value)
        
    def popPairs(self, key):
        self.pairs.pop(self.pairs.index(key))
        
        

        
        