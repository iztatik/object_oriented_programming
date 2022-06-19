                #TUPLAS
#Permiten almacenar distintos tipos de datos, sin que se puedan quitar o agregar elementos después de crearlas

my_tuple=("Alberto", 3.14, False,0.25, "perro")
print(my_tuple)

#Imprimir un dato especifico de la tupla
print(my_tuple[1])

#imprimir un rango de datos de la tupla
print(my_tuple[0:3])

#Convertir una lista a tupla y una tupla a lista
lista=[1,2,3,4,5]
tupla= tuple (lista)
lista2= list (tupla)
print (tupla)
print(lista2)
