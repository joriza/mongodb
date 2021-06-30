# Para ejecutar Mongo en Docker
# docker run -d -p 27017:27017 --name mydatabase mongo:4.2
# docker run --rm -d -p 27017:27017 --name mongo mongo:4.2
# docker start mydatabase
# hasta que recuerde mejor el uso de docker, para poder usar nuevamente el contenedor
# Primero se debe borrar el contenedor con el comando
# docker rm <nombre>

import os
import pymongo
from pymongo import MongoClient
os.system ("clear")

class Basededatos():
  def __init__(self):
      self.client = MongoClient('localhost',27017,username="root",password="root")
      self.db = self.client['pru']
      self.col = self.db['temp']
      # self.cliente = client
      # self.db = db
      # self.col = col

  def imprime(self):
      print("\nDesde metodo imprime")
      cant = self.col.count_documents({})
      print("cantidad de registros:", cant)
      for documento in self.col.find({}):
          print(documento)

  def agrega(self):
    registro = {"nombre":"jorge","intereses":["dato1","dato2"]}
    self.col.insert_one(registro)

if __name__ == '__main__':
  datos = Basededatos()
  datos.agrega()
  print("desde main\n",datos.cliente)
  datos.imprime()


# registro = {"nombre":"jorge","intereses":["dato1","dato2"]}
# col.insert_one(registro)

# importacion 1
# with open("importar2.json") as f:
# file_data = json.load(f)
# col.insert(file_data)
# client.close()


# importacion 2
# #Abriendo el archivo con la funcion open()
# f = open("importar2.json", 'r')
# #Recorriendo las lineas del archivo
# for linea in f:
#   #Insertando los registros en la DB
#   dic = json.loads(linea) #Crea los diccionarios a partir del string linea
#   col.insert(dic)
# #Cerramos el archivo
# f.close()
# print ("\nSe han importado los datos exitosamente!")


# # importacion 3
# with open('currencies.json') as file:
#     fil e_data = json.load(file)

# if isinstance(file_data, list):
#     col.insert_many(file_data)
# else:
#     col.insert_one(file_data)