'''
Created on 14 de mar de 2017

@author: carineaguena
'''
from abc import abstractmethod

class SchemaData:
    def __init__(self, name, describe):
        self.columns = []
        self.name = name
        self.describe = describe
        self.createSchema()
   
    @abstractmethod
    def createSchema(self):
        pass
    
    def getSchema(self):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
    
    def putColumn(self, key):
        self.columns.append(key)
        
    def getColumn(self, key):
        index = self.columns.index(key)
        return self.columns[index]
    
    def getColumns(self):
        return self.columns
        
    def popColumn(self, key):
        self.columns.pop(self.columns.index(key))
            