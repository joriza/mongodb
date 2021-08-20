# Para ejecutar Mongo en Docker
# docker run -d -p 27017:27017 --name mydatabase mongo:4.2
# docker run --rm -d -p 27017:27017 --name mongo mongo:4.2
# docker start mydatabase
# hasta que recuerde mejor el uso de docker, para poder usar nuevamente el contenedor
# Primero se debe borrar el contenedor con el comando
# docker rm <nombre>

import os
import pymongo
from pymongo import MongoClient
os.system ("clear")

# conexión
client = MongoClient('localhost',27017,username="root",password="root")
#crear una base vacía, #Si existe la abre
db = client['pru']
# crea una colección ,si existe la usa
col = db['col']
# Imprime las bases de datos existentes
print(client.list_database_names())
# Imprime las colecciones de esas bases
print(db.list_collection_names())

#Recuento de documentos
cant = col.count_documents({})
print("cantidad de registros:", cant)

#Recorrer todos los documentos
for documento in col.find({}):
    print(documento)

print("coleccion en crudo:\n",col)

registro = {"nombre":"jorge","intereses":["dato1","dato2"]}

col.insert_one(registro)