'''
Created on 14 de mar de 2017

@author: carineaguena
'''

from NoSQL_Invetory.SchemaData import SchemaData

class SchemaDataColumnFamily(SchemaData):
    
    def __init__(self, name, describe):
        self.families = []
        self.columns = []
        self.name = name
        self.describe = describe
        
    def getSchema(self):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    def addFamily(self, family):
        self.families.append(family)
        
    def addColumn(self, column):
        self.columns.append(column)
        
    def getColumn(self):
        return self.columns
    
    def getFamilies(self):
        return self.families
    
    