'''
Created on 14 de mar de 2017

@author: carineaguena
'''
from NoSQL_Invetory.Inventory import Inventory

class InventoryFactory:
        
    def __init__(self):
        self.inventories = []
    
    def addInventory(self, schemaData, nameInventory, describeInventory):
        self.inventories.append(Inventory(schemaData, nameInventory, describeInventory))
        
    def removeInventory(self, inventory):
        self.inventories.remove(inventory.getInventoryName())
        
    def getInventories(self):
        return self.inventories
    
        
        


    
        

    
    