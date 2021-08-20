# Para ejecutar Mongo en Docker
# docker run -d -p 27017:27017 --name mydatabase mongo:4.2
# docker run --rm -d -p 27017:27017 --name mongo mongo:4.2
# docker start mydatabase
# hasta que recuerde mejor el uso de docker, para poder usar nuevamente el contenedor
# Primero se debe borrar el contenedor con el comando
# docker rm <nombre>

import os
import json
import pymongo
from pymongo import MongoClient
os.system ("clear")

class Basededatos():
  def __init__(self):
      self.client = MongoClient('localhost',27017,username="root",password="root")
      self.db = self.client['pru']
      self.col = self.db['temp']

  def imprime(self):
      print("\nDesde metodo imprime")
      cant = self.col.count_documents({})
      print("cantidad de registros:", cant)
      for documento in self.col.find({},{"_id":0}): # imprime sin el :id
          print(documento)

  def agrega(self):
    registro = {"nombre":"jorge","intereses":["dato1","dato2"]}
    self.col.insert_one(registro)

  def RequiredDomains(self,file):
    file = file+".json"
    print("archivo: ",file)
    with open("RequiredDomains.json", "r") as read_file:
      registro = json.load(read_file)
    self.col.insert_one(registro)

  def exporta(self):
    pass


if __name__ == '__main__':
  datos = Basededatos()
  datos.agrega()
  print("desde main\n",datos.client)
  datos.RequiredDomains("data_file")
  datos.imprime()


# registro = {"nombre":"jorge","intereses":["dato1","dato2"]}
# col.insert_one(registro)

