                        #List Comprehension

#Permite crear una lista y agregar sus elementos a la misma con un mínimo de pasos

#Llenado "clásico" de una lista
lista1 =[ ] #Creamios lista vacía
for valor in range(0,21): #Lenamos lista
    lista1.append(valor)
print (lista1)
    
#Llenado con list comprehension con ciclo
lista2 = [valor for valor in range(0,21)] # [1.variable a agregar + 2.ciclo for,while,etc]
print (lista2)

#Llenado con list comprehension con ciclo y condicional
lista2 = [valor for valor in range(0,21) if valor % 2==0] # [1.variable a agregar + 2.ciclo for(while) + 3.Condicional para agregar]
print (lista2)

#Usar comprehension en Tupla
tupla= tuple((valor for valor in range (0,21) if valor%2!=0)) #Solo se convierte a tuple con tuple
print (tupla)

#Usar comprehension en Diccionario
diccionario = { llave:valor for llave,valor in enumerate (lista1)}
print (diccionario)
