# -*- coding: utf-8 -*-
from string import Template
import csv
import os
import json
# import nestedlookup
###############################################################################
# El script extrae del archivo entrada.csv las frases y el Expected Json Result
# generando un archivo salida.json, válido para ser ejecutado con terrier upload
# Archivos necesarios.
# arma_upload_test.py, que exista entrada.csv
# En la carpeta source deben estar las plantillas necesarias, acondicionadas para cada dominio, ya que no son todas iguales.
# Los otros archivos son prescindibles, se pueden eliminar
# -----------------------------------------------------------------------------
# carpeta source: contiene las plantillan necesarias
#   En plantilla cabecera se deben colocar los dominios a utilizar
# archivo de entrada = entrada.csv
#   formato csv delimitado por tabuladores
#   Debe contener la primer fila con el nombre de los campos.
#   En el ejemplo está tomado de un kpi del cliente.
#   Nombre de los campos indispensables
#     Query         = Frase a testear (sin comillas)
#     Expected Json Result = Resultado esperado (debe contener las llaves de apertura y cierre)
# archivo de salida = salida.json
#   Ahora no se debe eliminar manualmente la ultima coma
#   graba 2 archivos de salida para poder comparar luego de regenerar.
# archivo de errores = json_invalido.txt
#   aqui registra los numereros de consulta y las frases que tienen expected mal conformados.
# Se puede ejecutar con:
# time te run-uploaded-domain-tests -regenerate salida.json
# time te run-uploaded-domain-tests -regenerate salida.json | tee $jorge/test_results/udt_ums_kpi$(date +%F_%H%M).txt
###############################################################################

# Funcion que valida objeto json
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

# Variables de configuración
sigla_dom = "rcl" # Sigla del dominio
sigla_dom_acond = "_" + sigla_dom # Sigla del dominio acondicionada.
sigla_dom_acond = sigla_dom_acond + "_psa" # Se agrega si es para psa, puede tener cambios.


# variables de trabajo
source_f = "entrada" # archivo .csv con las frases a procesar
target_f = "salida" # archivo .csv con las frases a procesar
error = "Frases con Expected mal conformados\n"
reg_tot=reg_ok=reg_err=0

#######################################################################################################################

# Limpiar pantalla
os.system ("clear")

# Abre las plantillas y las guarda en variables para trabajarlas
with open("./source/plantilla_input"+sigla_dom_acond+".json") as raw_f:
  pl_input = raw_f.read()
with open("./source/plantilla_cabecera"+sigla_dom_acond+".json") as raw_f:
  pl_cabecera = raw_f.read()
with open("./source/plantilla_metadata"+sigla_dom_acond+".json") as raw_f:
  pl_metadata = raw_f.read()
with open("./source/plantilla_pie"+sigla_dom_acond+".json") as raw_f:
  pl_pie = raw_f.read()

temp = pl_cabecera #agrega cabecera
temp = temp + pl_metadata #agrega plantilla metadata.
# Abre archvio csv y lo recorre
with open('./'+source_f+".csv") as csvfile:
  reader = csv.DictReader(csvfile,delimiter='\t')
  for row in reader:
    if reg_tot > 0:
      temp = temp  + "\t\t\t\t\t,\n" #agrega una coma , para separar los test. Al comienzo del segundo test y en los siguientes.
    reg_tot+=1
    json_valido = json_validator(row['Expected Json Result']) # Verifica que el Expected esté bien conformado
    if json_valido: # Sustituir campos de la plantilla input por datos de las variables
      reg_ok+=1
      t = Template(pl_input)
      ### Se debe acondicionar el Expected Result, porque no viene exactamente como lo muestra el udt
      # acond_expected=row['Expected Json Result']
      # acond_expected = acond_expected.replace('{"AllResults":[{','[{"ServerResponse":{')
      # acond_expected = acond_expected.rstrip('}]}\n') # Al replace no se le puede colocar caracteres no visibles."
      ### Probando otro acondicionamiento
      acond_expected=row['Expected Json Result']
      if sigla_dom == "csh":
        acond_expected = acond_expected.replace('"AllResults":[{','"ServerResponse":{')
        acond_expected = acond_expected.replace('}]}','}}')
      else: # acondicionando Expected de forma general
        acond_expected = acond_expected.replace('AllResults','ServerResponse')
        acond_expected = acond_expected.replace('[','')
        acond_expected = acond_expected.replace(']','')
      #
      s = t.safe_substitute(frase=row['Query'], expected=acond_expected, qry_nro=row['Query#'], level=row['Level'])
      temp = temp + s #agrega input reemplazado
    else: # registra frases con errores
      reg_err+=1
      error = error + row['Query#'] + " " + row['Query'] + " " + row['Expected Json Result']

temp = temp + pl_pie #agrega pie

# Graba en archivos los resultados
with open ("./error_json_invalido.txt", "w") as pre_proc_f: # Graba en archivo las frases que contienen expected mal conformados
  pre_proc_f.write(error)
with open ("./"+target_f+".json", "w") as pre_proc_f: # Graba el resultado a un archivo
  pre_proc_f.write(temp)
with open ("./"+target_f+".json", "w") as pre_proc_f: # Graba 2 veces para no perder el original al ejecutar el regenerate
  pre_proc_f.write(temp)

# Resumen de lo realizado
print(f"Totales: {reg_tot}")
print(f"Proces.: {reg_ok}")
print(f"Errores: {reg_err}")
print("Archivo resultante: salida.json")

