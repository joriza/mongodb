# Sencillo ejemplo con POO

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