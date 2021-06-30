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

class Humano():
  def __init__(self,edad):
    self.edad = edad
    print("Soy un nuevo objeto")

  def hablar(self,mensaje):
    print(mensaje)

pedro = Humano(26)
raul = Humano(21)

print("soy pedro",pedro.edad)
print("soy raul",raul.edad)

pedro.hablar("Hola")
raul.hablar("Hola Pedro")