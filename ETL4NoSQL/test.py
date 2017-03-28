'''
Created on 21 de mar de 2017

@author: carineaguena
'''



paradigma = input("Escolha o paradigma 1 2 3 4: ")
name = raw_input("Nome do esquema: ")
descricao = raw_input("Descricao do esquema: ")

if __name__ == '__main__':
    schema_type = "SchemaDataColumnFamily"
    schema = eval(schema_type)(name, descricao)
    print("Criando esquema..", type(schema).__name__)
    print("Schema tem colunas: ", schema.getColumns())

if __name__ == '__main__':    
    schema_type = "SchemaDataKeyValue"
    schema = eval(schema_type)(name, descricao)
    print("Criando esquema..", type(schema).__name__)


#sample.createSample()