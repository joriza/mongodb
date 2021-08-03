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
    self.dic_resultado={"Nombre":"Jorge","Apellido":"Izaguirre"}

  def Muestra_lst(self):
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
      1.Mostrar Lista
      2.Agregar a mano una dato a la lista
      3.Lee de archivo lst por parámetro y agrega a lst_resultado
      4.Graba en archivo el lst_resultado actual
      5.Mostrar Dic.
      6.Agrega item al Dic.
      8.Lee de archivo dic por parámetro y agrega a dic_resultado

      0.Exit/Quit
      """)
      ans=input("ingrese opcion: ")
      if ans=="1":
        self.Muestra_lst()
      elif ans=="2":
        self.Agrega_a_mano()
      elif ans=="3":
        aux = self.Lee_lst_ArchivoJson("RequiredDomains.json")
        self.Agrega_A_lst_Resultado(aux)
      elif ans=="4":
        self.Graba_lst_en_archivo(self.lst_resultado)
      elif ans=="5":
        self.Muestra_dic()
      elif ans=="6":
        self.Agrega_item_dic()
      elif ans=="8":
        # aux = self.Lee_dic_ArchivoJson("Diccionario.json")
        aux = self.Lee_dic_ArchivoJson("TestCases.json")
        self.Agrega_a_dic_Resultado(aux)
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
    with open("data_lst_string.json", "w") as write_file: # Escribe en archivo json string
      json.dump(param1, write_file)
    with open("data_lst_dump.json", "w") as write_file: # Escribe en archivo json indentado
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

  def Muestra_dic(self):
    'Muestra los items del diccionario'
    print(self.dic_resultado)
    a = input("Ingrese una tecla para continuar")

  def Agrega_item_dic(self):
    'Agrega item al diccionario'
    self.dic_resultado['Edad'] = 22
    self.PressEnter()

  def Lee_dic_ArchivoJson(self,param1):
    '''Lee archivo pasado por parámetro
    y devuelve lo leido en un objeto'''
    with open(param1, "r") as read_file:
      documento = json.load(read_file)
      print(documento)
      self.PressEnter()
    return(documento)

  def Agrega_a_dic_Resultado(self,param1):
    '''Agrega como item de un diccionario,
    un objeto pasado por parámetro'''
    self.dic_resultado.update(param1)

if __name__ == '__main__':
  udt = Estructura()
  # a = input("ingrese udt: ")
  # udt.Imprime2(a) # Llama al método Imprime2, le pasa una valor con la variable a
  # print(udt.aux1) # Imprime el atributo aux1, que se inicializa en el método Imprime2.

  udt.Menu_principal()

