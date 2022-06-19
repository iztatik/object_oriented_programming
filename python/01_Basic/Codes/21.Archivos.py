# Creamos una instancia de archivo
fichero = open('archivo.txt','a+')

# Escribimos en el archivo
texto = '\nEsta linea se ha agregado'
fichero.write(texto) 

# Leemos desde el inicio (seek(0)) el archivo, almacenamos su contenido y lo imprimimos
fichero.seek(0)
data = fichero.read()
print(data)

# Cerramos el archivo
fichero.close()
