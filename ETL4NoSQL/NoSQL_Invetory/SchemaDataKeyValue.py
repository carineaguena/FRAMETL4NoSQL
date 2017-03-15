'''
Created on 14 de mar de 2017

@author: carineaguena
'''
from NoSQL_Invetory.SchemaData import SchemaData

class SchemaDataKeyValue(SchemaData):
    
    def __init__(self, name, describe):
        self.keys = []
        self.values = []
        self.name = name
        self.describe = describe
    
    def getSchema(self, name):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    def addKey(self, key):
        self.keys.append(key)
        
    def addValue(self, value):
        self.values.append(value)
        
        

        
        