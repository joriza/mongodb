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
    print("clase Prueba")
    # inicializa los datos en en valor prefijado, para que tenga algo cargado para las pruebas.
    self.lst_resultado=[]
    self.dic_resultado={}

  def Muestra_dato(self):
    'Muestra los items de la lista'
    print(self.lst_resultado)
    a = input("Ingrese una tecla para continuar")

  def Agrega_a_mano(self):
    '''Pide dato para ingresar a la lista.
    Y lo agrega'''
    a = input("ingrese dato para agregar a la lista: ")
    self.lst_resultado.append(a)

  def Menu_principal(self):
    ans=True
    while ans:
      os.system ("clear")
      print ("""
      1.Mostrar
      2.Agregar a mano una dato a la lista
      3.Lee de archivo por parámetro y agrega a lst_resultado
      4.Graba en archivo el lst_resultado actual
      0.Exit/Quit
      """)
      ans=input("ingrese opcion: ")
      if ans=="1":
        self.Muestra_dato()
      elif ans=="2":
        self.Agrega_a_mano()
      elif ans=="3":
        aux = self.Lee_lst_ArchivoJson("RequiredDomains.json")
        self.Agrega_A_lst_Resultado(aux)
      elif ans=="4":
          self.Graba_lst_en_archivo(self.lst_resultado)
      elif ans=="0":
        exit()
      elif ans !="":
        print("\n Opción inválida")
        self.PressEnter()

  def PressEnter(self):
    '''Solo pausa hasta que se presione enter'''
    input("Presione Enter para continuar...")

  def Graba_lst_en_archivo(self,param1):
    '''Graba en archivo objeto pasado
    por parámetro'''
    # Escribe en archivo json string
    with open("data_lst_string.json", "w") as write_file:
      json.dump(param1, write_file)
    # Escribe en archivo json indentado
    with open("data_lst_dump.json", "w") as write_file:
      json.dump(param1, write_file,indent=2)

  def Lee_lst_ArchivoJson(self,param1):
    '''Lee archivo pasado por parámetro
    y devuelve lo leido en un objeto'''
    with open(param1, "r") as read_file:
      documento = json.load(read_file)
      print(documento)
      self.PressEnter()
    return(documento)

  def Agrega_A_lst_Resultado(self,param1):
    '''Agrega como item de una lista,
    un objeto pasado por parámetro'''
    self.lst_resultado.append(param1)


if __name__ == '__main__':
  udt = Estructura()
  # a = input("ingrese udt: ")
  # udt.Imprime2(a) # Llama al método Imprime2, le pasa una valor con la variable a
  # print(udt.aux1) # Imprime el atributo aux1, que se inicializa en el método Imprime2.

  udt.Menu_principal()