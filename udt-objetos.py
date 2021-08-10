import os
import json
import jmespath

qry_input = "frases.txt" # Archivo con las frases origen

os.system ("clear")

class EstructuraUDT():
  'Clase principal.'
  def __init__(self):
    'Inicializa la clase'
    print("Nombre: ",__name__)

  def PressEnter(self):
    '''Solo pausa hasta que se presione enter'''
    input("Presione Enter para continuar...")

  def AbreArchivoOrigen(self,sourcefile):
    aux = open(sourcefile, "r")
    return(aux)

  def LeeJsonModelo(self,param1):
    '''Lee archivo json pasado por parámetro
    y devuelve lo leido en un objeto'''
    with open(param1, "r") as read_file:
      docJson = json.load(read_file)
    return(docJson)

  def GrabaJsonSalida(self,param1):
    '''Graba a archivo json
    objeto pasado por parámetro'''
    with open("data_dump.json", "w") as write_file: # Escribe en archivo json indentado
      json.dump(param1, write_file, ensure_ascii= False, indent=2)
    # return(docJson)

if __name__ == '__main__':
  udt = EstructuraUDT()
  frases = udt.AbreArchivoOrigen(qry_input)

  jsonModelo = udt.LeeJsonModelo("jsonModeloCortoMPC.json")
  for frase_actual in frases:
    frase_actual= frase_actual. rstrip("\n")
    print(frase_actual)

  # acond_expected = jsonModelo
  # acond_expected = acond_expected.replace('FraseModelo','frase_actual')


  print("\nTodo el json: ",jsonModelo)
  print("todo el json: ", type(jsonModelo))
  # jsonModelo['TestCases'][0]['Input'][0]['Input'] = frase_actual
  # print("Frase extraida: ",a)
  nuevoTestCase = jsonModelo['TestCases'][0]
  print("\nnuevoTestCase: ",nuevoTestCase)
  print(type(nuevoTestCase))


  testCasesActuales = jsonModelo['TestCases']
  print("\n los test Cases: ",testCasesActuales)
  print(type(testCasesActuales))

  jsonModelo['TestCases'].append(nuevoTestCase)
  print("\n json Modelo Final: ",jsonModelo)

  udt.GrabaJsonSalida(jsonModelo)

  # lst_resultado.append(param1) ## agrega item a un a lista
  # dic_resultado.update(param1) ## agregar item a un dicc


  # # Extrae plantilla TestCases
  # aux0 = jmespath.search('TestCases[].Input[]', jsonModelo)

  # print("tipo dato list TestCases.Input: ",type(jsonModelo))
  # aux = jsonModelo[0]
  # print("tipo dato dict TestCases.Input: ",type(aux))
  # print("TestCases.Input: ",aux)
  # print(aux['Input'])
  # aux2 = jmespath.search('[].Input[]', jsonModelo)
  # print("aux2",aux2)
  # print("Con Json Py",.Input[])

  print("\nTerminado normalente")
