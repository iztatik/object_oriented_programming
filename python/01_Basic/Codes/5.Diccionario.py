                    #DICCIONARIOS

#Permiten alacenar cualquier tipo de dato sin el sistema indexado de las listas y tuplas, sustituyendeolo por una llave/clave (que debe ser un tipo de dato inmutable)

#Declarar un diccionario {llave:dato}
dicc={'a':55, 1: 3.14, (25,12):True}
print(dicc)

#Agregar elementos al diccionario
dicc["c"]=False 
print(dicc)

#actualizar datos del diccionario
dicc["a"]=33
print(dicc)

#obtener un dato del diccionario invocandoclo con su clave
dato=dicc['a']
print(dato)

#obtener un dato, si el dato no existe regresar un valor predeterminado nombre.get(llave, valor a regresar si no se encuentra)
dato = dicc.get('z', False)
print(dato)

#Eliminar datos del diccionario
del dicc[(25,12)]
print(dicc)

#Obtener las llaves del diccionario
llaves=dicc.keys()
print(llaves)

#Obtener las llaves del diccionario y convertirlas en una lista (tupa/tuple)
llaves= list(dicc.keys())
print(llaves)

#Obtener los valores del diccionario y convertirlas en una lista (tupa/tuple)
valores= list(dicc.values())
print(valores)

#Unir 2 diccionarios
dicc2={'r':'agregado',33:3.3}
dicc.update(dicc2)
print (dicc)


#Obtener el índice de posición junto a su valor correspondiente cuando se itera sobre una secuencia .
for i, v in enumerate(['a', 'b', 'd']):
    print(i, v)
