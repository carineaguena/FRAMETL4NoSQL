'''
Created on 22 de mar de 2017

@author: carineaguena
'''

#
#Classe que mantem o inventario das bases de dados
#Possui como atributos uma lista de esquemas, o nome do inventario
#descricao do inventario, conexao com o banco de dados
# 

class Inventory:
    
    def __init__(self, nameInventory, describeInventory, connection):
        self.schemas = []
        self.nameInventory = nameInventory
        self.describeInventory = describeInventory
        self.connection = connection
        
    def getInventoryName(self):
        return self.nameInventory
    
    def getInventoryDescribe(self):
        return self.describeInventory
    
    def getSchemas(self):
        return self.schemas
    
    def addSchema(self, schema):
        self.schemas.append(schema)