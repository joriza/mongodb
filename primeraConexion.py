# Para ejecutar Mongo en Docker
# docker run -d -p 27017:27017 --name mydatabase mongo:4.2

import pymongo

from pymongo import MongoClient

# conexión
client = MongoClient('localhost',27017,username="root",password="root")
db = client.mitienda

# colección
cuentas = db.usuarios

resultado = db.usuarios.find()

# Imprime las bases de datos existentes
print(client.list_database_names())
