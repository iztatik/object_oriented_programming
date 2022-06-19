                #FUNCIONES ANIDADAS


#Función anidada básica
def division (x,y):
    def validacion ():                   #Función anidada
        return (x!=0 and y!=0)

    if(validacion()):
        return x/y
    else:
        return ('Valores inapropiados')

print(division (45,-5))
print()

#Función closures (fucniones que crean funciones)
def crear(a,b):
    def sumar():
        return a+b
    return sumar

nueva_funcion1 = crear(5,9)
nueva_funcion2 = crear(1,7)
print (nueva_funcion1())
print (nueva_funcion2())
print()


#Función que recibe como parametro otra función

def recibe (func):
    print(func())

recibe (nueva_funcion1)
