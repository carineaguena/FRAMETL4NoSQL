'''
Created on 14 de mar de 2017

@author: carineaguena
'''

from NoSQL_Invetory.SchemaData import SchemaData

#A CF is a collection of columns. These exist in a table.
#Rows are similar to relational rows, except that all rows in the same
#table do not necessarily have the same structure. A value in a cell, i.e.,
#the intersection of a row and a column, is an uninterpreted bit sequence. Each cell
#is versioned, meaning that it can contain multiple versions of the same data and that
#every version has a timestamp attached to it.
####NASHOLM, 2012 - Extracting Data from NoSQL Databases

class SchemaDataColumnFamily(SchemaData):
    
    def __init__(self, name, describe):
        self.columns = []
        self.name = name
        self.describe = describe
        
    def getSchema(self):
        return "Name Schema: " + self.name + " Describe Schema: " + self.describe
        
    def putColumn(self, column, key):
        self.columns.append(column, key)
        
    def getColumn(self, key):
        index = self.columns.index(key)
        return self.columns[index]
        
    def popColumn(self, key):
        self.columns.pop(self.columns.index(key))
        
    