                #Funciones
#Función simple
def mi_funcion(num1,num2):
    print('La suma es:', num1+num2)

mi_funcion (3,4)


#Funcion que almacena parametros en una tupla
def mi_funtupla (*tupla):
    print ('La tupla contiene: ')
    for dato in tupla:
        print (" ",dato, end="")

mi_funtupla ('gato',33,'perro', True)
print()



#Función que almacena los parametros en un diccionario
def mi_fundicc (** diccionario):
    print (diccionario["llave"])

mi_fundicc (llave="Esto está en un diccionario")



#Fucnión que regresa un valor
def mi_funcion_regresa(num1,num2):
    return  num1+num2

resultado= mi_funcion_regresa (15,32)
print ('La suma es:',resultado)



#Función que regresa muliples valores en forma de tupla
def multiples ():
    return ('Hola', 25, True)

resultado=multiples()               
string,numero,booleano = multiples()
print(resultado)
print(string,numero,booleano)


#Almacenar una función en un varialble
variable = mi_funcion
result= variable(5,2)
print(result)


