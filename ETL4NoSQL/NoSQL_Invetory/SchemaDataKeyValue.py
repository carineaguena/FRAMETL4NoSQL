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
    
    def createSchema(self):
        key = raw_input("Insert key value: ")
        self.putColumn(key)
  
        
        

        
        