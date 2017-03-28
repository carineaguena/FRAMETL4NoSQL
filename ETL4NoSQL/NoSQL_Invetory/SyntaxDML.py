'''
Created on 15 de mar de 2017

@author: carineaguena
'''
from abc import abstractmethod

class SyntaxDML:
    
    @abstractmethod
    def selectSyntaxDML(self):
        pass
    
    @abstractmethod
    def updateSyntaxDML(self):
        pass
    
    @abstractmethod
    def insertSyntaxDML(self):
        pass
    
    @abstractmethod
    def deleteSyntaxDML(self):
        pass
    
    