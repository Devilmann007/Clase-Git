with open("datos.txt", "r") as archivo: # "r" abre el archivo en modo lectura                                        
    contenido = archivo.read()# Lee todo el contenido del archivo, with cierra el archivo automaticamente despues de usarlo 
    print(contenido)  # Muestra el contenido en la consola