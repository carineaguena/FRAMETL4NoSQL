'''
Created on 21 de mar de 2017

@author: carineaguena
'''

class SampleMap:
    
    def __init__(self, schema):
        self.schema = schema
        
    def getSampleMap(self):
        return self.schema
    
    def setSampleMap(self, newSchema):
        self.schema = newSchema
        
    def createSampleMap(self):
        pass
    