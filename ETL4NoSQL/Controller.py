'''
Created on 2 de mar de 2017

@author: carineaguena
Componente responsavel pelas operacoes
Component responsible for operations

'''
from NoSQL_Invetory.SchemaDataColumnFamily import SchemaDataColumnFamily
'''from NoSQL_Import.Import import connectionSource

conexao = connectionSource("localhost","root","12346","Cassandra")
print(conexao.DMLImport)
conexao.setDMLImportDB()
print(conexao.getDMLImportDB())'''

inventario = SchemaDataColumnFamily("Familia de Coluna", "Esquema da base fonte")
inventario.addFamily("automovel")
inventario.addFamily("imovel")
inventario.addColumn("Sedan")
print(inventario.getFamilies())
print(inventario.getSchema())


