                    #Métodos de búsqueda


cadena = "Carlos Alberto Sánchez Delgado"

#Encontrar una palabra, regresa la posición de la ltra inicial de la palabra, si no la encuentra regresa -1
print(cadena.find("Sánchez"))
print(cadena.find("gato"))

#Contar el número de veces que se encuentra un caracter en un string
print(cadena.count("o"))

#Remplazar caracteres de la cadena
print(cadena.replace('a','o'))

#convertir un sting en una lista cada que encuentre un espacio
print(cadena.split(" "))
