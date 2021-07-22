## Practicando con manejo de objetos.

import os
import json
import pymongo
from pymongo import MongoClient
os.system ("clear")

class Estructura():
  'Clase principal.'
  def __init__(self):
    'Inicializa la clase'
    # self.aux1 = 0
    print("clase Prueba")

  def Imprime2(self,param1):
    'Método1'
    print("Método Imprime2")
    print(param1)
    self.aux1 = param1 * 2

  def Imprime3(self):
    'Método2'
    print("Metodo Imprime3",self.aux1)

if __name__ == '__main__':
  dato = Estructura()
  a = input("ingrese dato: ")
  dato.Imprime2(a) # Llama al método Imprime2, le pasa una valor con la variable a
  print(dato.aux1) # Imprime el atributo aux1, que se inicializa en el método Imprime2.


