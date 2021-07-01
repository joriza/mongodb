# Varios ejemplos de lectura, escritura y manipulación de archivos con datos formato json
# Fuente: https://realpython.com/python-json/
# https://www.datacamp.com/community/tutorials/introduction-mongodb-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9041014&gclid=CjwKCAjwrPCGBhALEiwAUl9X009AOO_QZ53u_cprzCuXWt-ZcpWilxGJVhQVmSVPRurEoAHO-3gXqxoCdx0QAvD_BwE
# Consultar mongo engine
# jmespath para python
import os
os.system ("clear")

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# Escribe en archivo json string
with open("data_file.json", "w") as write_file:
  json.dump(data, write_file)
# Escribe en archivo json indentado
with open("data_file2.json", "w") as write_file:
  json.dump(data, write_file,indent=2)

json_string = json.dumps(data, indent=2)
print("\ndata: ",data)
print("\njson indentado: ",json_string)

json_string2 = json.dumps(data, separators=(',', '= '),indent=2)
print("\njson separado con =",json_string2)

# Lee archivo python y lo imprime
with open("data_file.json", "r") as read_file:
  data2 = json.load(read_file)
print("\ndata leido, mostrado como string: ",data2)
data22 = json.dumps(data, indent=2)
print("\ndata leido, mostrado mostrado indentado: ",data22)

# # Prueba con un archivo de UDT
# with open("ums.json", "r") as read_file:
#    data5 = json.load(read_file)
# print("\nums como string: ",data5)
# data23 = json.dumps(data5, indent=4)
# print("\nums indentado: ",data23)


