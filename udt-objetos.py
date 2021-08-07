import os

qry_input = "frases.txt" # Archivo con las frases origen

class EstructuraUDT():
  'Clase principal.'
  def __init__(self):
    'Inicializa la clase'
    print("clase Prueba")

  def AbreArchivoOrigen(self,sourcefile):
    with open(sourcefile, "r") as frases:
      for frase_actual in frases:
        print(frase_actual)


if __name__ == '__main__':
  udt = EstructuraUDT()
  udt.AbreArchivoOrigen(qry_input)
  print("Terminado normalente")