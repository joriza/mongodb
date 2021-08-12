# CSV version
import os
import json
import copy
import csv

# qry_input = "frases.txt" # Name of the source file that contains the phrases

class UDTstructure():
  'Main class.'
  os.system ("clear")
  def __init__(self):
    'Initialize the class'
    # print("Nombre: ",__name__)

  def PressEnter(self):
    '''Just pause until Enter is pressed'''
    input("Presione Enter para continuar...")

  def OpenSourceDataFile(self,sourcefile):
    '''Opens file containing the phrases to be processed'''
    aux = open(sourcefile, "r")
    return(aux)

  def OpenSourceJsonFile(self,filename):
    '''Read model json file sent by parameter and return an object'''
    with open(filename, "r") as read_file:
      docJson = json.load(read_file)
    return(docJson)

  def SaveTargetFile(self,object,filename):
    '''Write the output in json format, the object sent by parameter'''
    with open(filename, "w") as write_file: # Escribe en archivo json indentado
      json.dump(object, write_file, ensure_ascii= False, indent=2)
    # return(docJson)

if __name__ == '__main__':
  udt = UDTstructure()
  csvfile = udt.OpenSourceDataFile("frasesPSA_MPC.csv")
  reader = csv.DictReader(csvfile,delimiter='\t')
  for row in reader:
    print(row['Query'])


  # jsonModelo = udt.OpenSourceJsonFile("jsonModeloCortoMPC.json")
  # TestCaseModelo = jsonModelo['TestCases'][0]  ## Extrae el primer testcase para reutilizar

  # for frase_actual in frases:
  #   frase_actual= frase_actual. rstrip("\n") ## Quita el retorno de carra de cada frase.
  #   nuevoTestCase = copy.deepcopy(TestCaseModelo) ## Ojo al copiar un diccionario o lista
  #   nuevoTestCase['Input'][0]['Input'] = frase_actual ## Reemplaza la frase en el testcase_modelo recurrente
  #   jsonModelo['TestCases'].append(nuevoTestCase) ## Agrega un nuevo test_case a la lista de testcases

  # jsonModelo['TestCases'].pop(0) ## Se elimina el 1er test case que es que se usó de modelo.
  # udt.SaveTargetFile(jsonModelo,"salida.json")

  # print("Generados",len(jsonModelo['TestCases']),"test")
  # print("Actualizar",len(jsonModelo['TestCases']))

