import os
import json

qry_input = "frases.txt" # Archivo con las frases origen

os.system ("clear")

class EstructuraUDT():
  'Clase principal.'
  def __init__(self):
    'Inicializa la clase'
    print(__name__)

  def PressEnter(self):
    '''Solo pausa hasta que se presione enter'''
    input("Presione Enter para continuar...")

  def AbreArchivoOrigen(self,sourcefile):
    aux = open(sourcefile, "r")
    return(aux)

  def AbreJsonModelo(self,param1):
    '''Lee archivo pasado por parámetro
    y devuelve lo leido en un objeto'''
    with open(param1, "r") as read_file:
      documento = json.load(read_file)
      print(documento)
      self.PressEnter()
    return(documento)

if __name__ == '__main__':
  udt = EstructuraUDT()
  frases = udt.AbreArchivoOrigen(qry_input)

  for frase_actual in frases:
    print(frase_actual)

  udt.AbreJsonModelo("jsonModelo.json")

  print("Terminado normalente")
