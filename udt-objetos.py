# Phrases input from a txt file

import os
import json
import copy

qry_input = "frases.txt" # Archivo con las frases origen

os.system ("clear")

class EstructuraUDT():
  'Clase principal.'
  def __init__(self):
    'Inicializa la clase'
    # print("Nombre: ",__name__)

  def PressEnter(self):
    '''Solo pausa hasta que se presione enter'''
    input("Presione Enter para continuar...")

  def AbreArchivoOrigen(self,sourcefile):
    '''Abre archivo que contiene las frases a procesar'''
    aux = open(sourcefile, "r")
    return(aux)

  def LeeJsonModelo(self,filename):
    '''Lee archivo json Modelo pasado por parámetro
    y devuelve lo leido en un objeto'''
    with open(filename, "r") as read_file:
      docJson = json.load(read_file)
    return(docJson)

  def GrabaJsonSalida(self,object,filename):
    '''Graba en archivo json de salida
    el objeto pasado por parámetro'''
    with open(filename, "w") as write_file: # Escribe en archivo json indentado
      json.dump(object, write_file, ensure_ascii= False, indent=2)
    # return(docJson)

if __name__ == '__main__':
  udt = EstructuraUDT()
  frases = udt.AbreArchivoOrigen(qry_input)
  jsonModelo = udt.LeeJsonModelo("jsonModeloCortoMPC.json")
  TestCaseModelo = jsonModelo['TestCases'][0]  # Extrae el primer testcase para reutilizar
  jsonModelo['TestCases'].clear() # Elimina los test cases del json modelo.

  for frase_actual in frases:
    frase_actual= frase_actual. rstrip("\n") ## Quita el retorno de carra de cada frase.
    nuevoTestCase = copy.deepcopy(TestCaseModelo) ## Ojo al copiar un diccionario o lista
    nuevoTestCase['Input'][0]['Input'] = frase_actual ## Reemplaza la frase en el testcase_modelo recurrente
    jsonModelo['TestCases'].append(nuevoTestCase) ## Agrega un nuevo test_case a la lista de testcases

  udt.GrabaJsonSalida(jsonModelo,"salida.json")
  print("Generados",len(jsonModelo['TestCases']),"test")
  print("Actualizar",len(jsonModelo['TestCases']))
