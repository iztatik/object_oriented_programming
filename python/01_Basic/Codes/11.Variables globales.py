                            #Variables globales


                            #RESTRICCIONES

#No se puede modificar el valor de una varibaleglobal en una fucnión
def cambiar_N ():
    var_global='Cambia valor'

var_global= 'Hola'
print (var_global)
cambiar_N()
print (var_global)
print()


#Una variable local no modifica a una global aunque tengan el mismo nombre
def invertir(palabra):    #variable local         
    return palabra[::-1]

palabra = 'Alberto'         #Variable global
print (palabra)
print(invertir(palabra))
print (palabra)
print()


                        #SOLUCIONES

#Usar "global" para modificar una variable global en una función 
def  cambiar_Y ():
    global var_global
    var_global='ahora si cambia valor'

cambiar_Y()
print (var_global)
print()

#Usar "global" para declara una variable global dentro de una función

def declara():
    global nueva_global
    nueva_global='Variable global'

declara ()
print (nueva_global)
