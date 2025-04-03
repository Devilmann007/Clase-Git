import json

# Abrir y leer el archivo JSON
with open(r"C:\Users\Esteban Amaya\OneDrive\Documentos\Sena\Ficha 3066478 segundo trimestre\Ejercicios SQL y NoSQL\Datos.json", "r") as archivo:
    datos = json.load(archivo)  # Convierte el JSON en un diccionario

# Mostrar el contenido
print(datos)
#"r" abre el archivo en modo lectura
#se coloca r"C:\user" pues \U da un error de syntaxis \U se interpreta como un carácter Unicode especial.
