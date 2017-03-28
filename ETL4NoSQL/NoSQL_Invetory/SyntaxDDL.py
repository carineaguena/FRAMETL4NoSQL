'''
Created on 16 de mar de 2017

@author: carineaguena
'''
from abc import abstractmethod

class SyntaxDDL:

    
    @abstractmethod
    def createSyntaxDDL(self):
        pass
    
    @abstractmethod
    def alterSyntaxDDL(self):
        pass
    
    @abstractmethod
    def dropSyntaxDDL(self):
        pass
    
    
    