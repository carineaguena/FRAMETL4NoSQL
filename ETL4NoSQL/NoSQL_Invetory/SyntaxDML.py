'''
Created on 15 de mar de 2017

@author: carineaguena
'''

class SyntaxDML:
    _instances = None
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SyntaxDML, cls).__new__(*args, **kwargs)
        return cls._instances[cls]
    
    def selectSyntaxDML(self):
        pass
    
    def updateSyntaxDML(self):
        pass
    
    def insertSyntaxDML(self):
        pass
    
    def deleteSyntaxDML(self):
        pass
    
    