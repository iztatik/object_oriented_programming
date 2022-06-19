                            #listas

#declara una lista (cualquier tipo de dato)
my_list=["lista", 3, 3.14, True]
print(my_list)


#Imprimir un elemento espesifico de la lista
print(my_list[2])

#Agregar elementas a la lista en la ULTIMA posición
my_list.append("Pedrito")
print(my_list)


#Agregar elementas a la lista en CUALQUIER posición
my_list.insert(1,"Juanito")
print(my_list)

#Eliminar elementos especificios de las listas
my_list.remove(3.14)
print (my_list)

#Extraer y eliminar el último elemento de la lista
ultimo = my_list.pop();
print (my_list)
print (ultimo)

#Ordenar una lista de números enteros acendentemente
numeros=[3,15,28,33,95,21,82]
numeros.sort()
print (numeros)

#Ordenar una lista de números enteros Descendente
numeros=[3,15,28,33,95,21,82]
numeros.sort(reverse=True)
print (numeros)

#UNIR una lista al final de la otra
numeros2=[22,23]
numeros.extend(numeros2)
print(numeros)

#AGREGAR (como otro elemento) una lista al final de otra (Una lista pude contener otras listas)
numeros2=[22,23]
numeros.append(numeros2)
print(numeros)
