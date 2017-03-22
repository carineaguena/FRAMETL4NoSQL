'''
Created on 20 de mar de 2017

@author: carineaguena
'''
#Responsible for create the sample basead on schema

from NoSQL_Invetory.SchemaDataColumnFamily import SchemaDataColumnFamily
from NoSQL_Invetory.SchemaDataDocument import SchemaDataDocument
from NoSQL_Invetory.SchemaDataGraph import SchemaDataGraph
from NoSQL_Invetory.SchemaDataKeyValue import SchemaDataKeyValue


class Sample:
    
    def __init__(self, schema):
        self.schema = schema
    
    #metodo para fazer a leitura de values e separar para adicionar os valores no esquema
    def createSample(self):
        response = ''
        #identifica o tipo de esquema e grava o que deve ser importado
        if isinstance(self.schema, SchemaDataColumnFamily):
            while response != 'y':
                #pode ser utilizado outros tipos de entrada
                column = raw_input("Digit column value:")
                key = raw_input("Digit key value:" )
                self.schema.putColumn(column, key)
                finish = raw_input("finish? [y / n]: ")
                if finish == 'y':
                    break;
        else:
            if isinstance(self.schema, SchemaDataDocument):
                while response != 'y':
                    document = raw_input("Digit document:")
                    self.schema.putDocuments(document)
                    finish = raw_input("finish? [y / n]: ")
                if finish == 'y':
                    break;
            else:
                if isinstance(self.schema, SchemaDataGraph):
                    while response != 'y':
                        node = raw_input("Digit node:")
                        self.schema.putNodes(node)
                        finish = raw_input("finish? [y / n]: ")
                        if finish == 'y':
                            break;
                else:
                    if isinstance(self.schema, SchemaDataKeyValue):
                        while response != 'y':
                            key = raw_input("Digit Key: ")
                            value = raw_input("Digit Value: ")
                            self.schema.putPairs(key+value)
                            finish = raw_input("finish? [y / n]: ")
                            if finish == 'y':
                                break;
                    
                
    def getSample(self):
        return self.schema
    
    def setSample(self):
        pass   