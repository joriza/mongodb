# -*- coding: utf-8 -*-
from string import Template
import csv
import os
import json
# import nestedlookup
###############################################################################
# Toma las frases de un archivo de frases
# generando un archivo segun varibla salida_f, para ser ejecutado con terrier upload
# Archivos necesarios.
# Frases de entrada en textop plana segun variable qry_input
# y la carpeta source
# Los otros son prescindibles, se pueden eliminar
# -----------------------------------------------------------------------------
# carpeta source: contiene las plantillan necesarias
#   En plantilla cabecera se deben colocar los dominios a utilizar
# archivo de entrada = entrada.csv
#   formato csv delimitado por tabuladors
#   Debe contener la primer fila con el nombre de los campos.
#   En el ejemplo está tomado de un kpi del cliente.
#   Nombre de los campos indispensables
#     Query           = Frase a testear (sin comillas)
#     Expected Result = Resultado esperado (debe contener las llaves de apertura y cierre)
# archivo de salida = salida.json
#   se debe eliminar manualmente la ultima coma
#   graba 2 archivos de salida para poder comparar luego de regenerar.
# archivo de errores = json_invalido.txt
#   aqui registra los numereros de consulta y las frases que tienen expected mal conformados.
# Se puede ejecutar con:
# time te run-uploaded-domain-tests -regenerate salida.json
###############################################################################

# Funcion que valida objeto json
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

# Variables de definicion
sigla_dom = "mpc" # Sigla del dominio
sigla_dom = "_" + sigla_dom # Sigla del dominio acondicionada.

# Nombre de archivos
qry_input = "./entrada-udt"+sigla_dom+".txt" # Archivo con las frases origen
salida_f = "./udt-creados"+sigla_dom+".json" # Archivo resultante
salida2_f = "./udt-creados"+sigla_dom+"_bak"+".json" # Copia archivo resultante
expected_ph = "[]" # Variable que contiene la salida esperada

# variables de trabajo
cnt_tot=0 # Contador de frases procesadas
#######################################################################################################################

# Limpiar pantalla
os.system ("clear")


# Abre las plantillas y las guarda en variables para trabajarlas
with open("./source/plantilla_input"+sigla_dom+".json") as raw_f:
  pl_input = raw_f.read()
with open("./source/plantilla_cabecera"+sigla_dom+".json") as raw_f:
  pl_cabecera = raw_f.read()
with open("./source/plantilla_metadata"+sigla_dom+".json") as raw_f:
  pl_metadata = raw_f.read()
with open("./source/plantilla_pie"+sigla_dom+".json") as raw_f:
  pl_pie = raw_f.read()


temp = pl_cabecera #agrega plantilla cabecera
temp = temp + pl_metadata #agrega plantilla metadata
# Abre archvio txt con las frases y lo recorre
with open(qry_input, "r") as frases:
  for qry_act in frases:
    if cnt_tot > 0:
      temp = temp  + "\t\t\t\t\t,\n" #agrega , para separar los test, al inicio del segundo en adelante.
    cnt_tot+=1
    qry_act=qry_act.rstrip("\n") # Se quita enter del final de la frase.
    t = Template(pl_input)
    s = t.safe_substitute(frase=qry_act, expected=expected_ph)
    temp = temp + s #agrega estructura test de 1 frase

temp = temp + pl_pie #agrega plantilla pie.

with open (salida_f, "w") as pre_proc_f: # Graba archivo resultante.
  pre_proc_f.write(temp)
with open (salida2_f, "w") as pre_proc_f: # Graba 2 veces para no perder el original al ejecutar el regenerate
  pre_proc_f.write(temp)

print(f"Frases procesadas: {cnt_tot}")
print(f"Archivo generado: {salida_f }")

