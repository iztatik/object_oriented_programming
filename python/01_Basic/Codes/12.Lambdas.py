                    #LAMBDAS (fuciones anónimas)

#Son una fusión de una macro de C y una función genérica, reultando en una fucnion en una linea
#Ejectuan acciones cortas y especificas(no ciclos)

sumador = lambda x,y : x + y
mayuscula = lambda x : x.upper()


resultado = sumador(5,3)
print (resultado)
resultado = mayuscula('Alberto')
print (resultado)
