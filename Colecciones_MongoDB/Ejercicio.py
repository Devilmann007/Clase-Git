# Importar libreria pymongo.
from pymongo import MongoClient

# Conectar con MongoDB.
client = MongoClient("mongodb://localhost:27017/")
db = client["Examen_final"]

# Crear colecciones.
clientes = db["Clientes"]

# Insertar documentos en la coleccion Clientes.
clientes.insert_many([
    {"Nombre": "Esteban", "Cuidad": "Mosquera", "Compras": 22},
    {"Nombre": "Juan", "Cuidad": "Cali", "Compras": 5},
    {"Nombre": "Alejandra", "Cuidad": "Funza", "Compras": 1}])

# Escribir consulta que devuelva los clientes que han realizado mas de 2 compras.
clientes_consulta1 = clientes.find({"Compras":{"$gt": 2}})

# Imprimir resultado de la consulta.
for cliente in clientes_consulta1:
    print(cliente)