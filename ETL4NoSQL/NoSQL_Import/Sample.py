'''
Created on 20 de mar de 2017

@author: carineaguena
'''
#Responsible for create the sample basead on schema

class Sample:
    
    #metodo para fazer a leitura de values e separar para adicionar os valores no esquema
    def createSample(self):
        paradigma = input("Escolha o paradigma 1 2 3 4: ")
        #identifica o tipo de esquema e grava o que deve ser importado
        if paradigma == 1:
                name = raw_input("Nome do esquema: ")
                descricao = raw_input("Descricao do esquema: ")

                if __name__ == '__main__':
                    schema_type = "SchemaDataColumnFamily"
                    schema = eval(schema_type)(name, descricao)
                    print("Criando esquema..", type(schema).__name__)
        else:
            if paradigma==2:
                name = raw_input("Nome do esquema: ")
                descricao = raw_input("Descricao do esquema: ")

                if __name__ == '__main__':
                    schema_type = "SchemaDataDocument"
                    schema = eval(schema_type)(name, descricao)
                    print("Criando esquema..", type(schema).__name__)
            else:
                if paradigma == 3:
                    name = raw_input("Nome do esquema: ")
                    descricao = raw_input("Descricao do esquema: ")

                if __name__ == '__main__':
                    schema_type = "SchemaDataGraph"
                    schema = eval(schema_type)(name, descricao)
                    print("Criando esquema..", type(schema).__name__)
                else:
                    if paradigma == 4:
                        name = raw_input("Nome do esquema: ")
                        descricao = raw_input("Descricao do esquema: ")

                    if __name__ == '__main__':
                        schema_type = "SchemaDataKeyValue"
                        schema = eval(schema_type)(name, descricao)
                        print("Criando esquema..", type(schema).__name__)
                    
                
    def getSample(self):
        return self.schema
    
    def setSample(self):
        pass   