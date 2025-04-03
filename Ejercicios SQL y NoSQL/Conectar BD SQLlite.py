import sqlite3

# Conectar a la base de datos (si no existe, se creará automáticamente)
conexion = sqlite3.connect("mi_base_de_datos.db")

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

print("Conexión establecida correctamente")