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

  def ReadSourceDataFile(self,sourcefile):
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
    with open(filename, "w") as output_file: # Escribe en archivo json indentado
      json.dump(object, output_file, ensure_ascii= False, indent=2)
    # return(docJson)

if __name__ == '__main__':
  udt = UDTstructure()
  csvfile = udt.ReadSourceDataFile("frasesPSA_MPC.csv")
  data = csv.DictReader(csvfile,delimiter='\t')
  jsonModelo = udt.OpenSourceJsonFile("jsonModeloMPC_PSA.json")
  TestCaseModelo = jsonModelo['TestCases'][0]  ## Extrae el primer testcase para reutilizar
  # jsonModelo['TestCases'].clear() ## Elimina los test cases del json modelo.

  for row in data:
    print(row['Query'])
    print(row['Expected Json Result'])

  udt.SaveTargetFile(jsonModelo,"salida.json")
