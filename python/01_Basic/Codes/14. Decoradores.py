                    #Decoradores

#Permite agregar mayor funcionalidad a una función
#Son funciónes que reciben como parametros una función y con ello crean una nueva fucnión
#A,B,C son funciones:
#A recibe como parámetro a B y crea a C

#Decorador
def decorador(func):            #A
    def nueva_funcion(*args):
        print('Parte del decorador que antecede a la función base');
        r=func(*args)
        print('Parte del decorador que sigue a la función base')
        print()
        return r
    return nueva_funcion        #C


#Función base 1
@decorador                 #Decoramos nuestra funcion base con @decorador
def saluda():                   #B
    print('Hola, esta es la función base1')

saluda()


#Función base 2
@decorador
def suma (a,b):
    res=10+3
    print('Función base2 : Suma=')
    return res

print (suma(3,5))
print()

#############################################################################
                #Decorador que recibe parámetros

def decorador_fun(caso):
    def _decorador_fun(fun):
        def nueva_fun():
            print ('Antes de la función base')
            if (caso):
                print ('Será el caso 1')
            else:
                print ('Será el caso 2')
            fun()
            print('Después de la función base')
        return nueva_fun
    return _decorador_fun


#función base 1

@decorador_fun(True)
def F1 ():
    print ('Efectivamente es el caso 1')
     
#función base 2
@decorador_fun(False)
def F2 ():
    print ('Efectivamente es el caso 2')
                 

F2()
