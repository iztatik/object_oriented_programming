                                                        #METODOS DE FORMATO

#Permiten modificar el formato de un String entre mayúsculas y minúsculas

parte1="Hola"
parte2="Mundo"
cadena="Carlos Alberto Sanchez Delgado"
cadena1="carlos alberto sanchez delgado"

#Convertir un string a solo mayúculas
print(cadena1.upper())

#Convertir un string a solo minúsculas
print(cadena.lower())

#Convertir las letras iniciales de cada palabra  a mayusculas (Título)
print(cadena1.title())

#Unir 2 Strings
print ("{a} {b}".format(a=parte1,b=parte2))
