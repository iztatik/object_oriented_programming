# El encapsulamiento impide que el usuario pueda leer, modificar o borrar loas atributos o métodos de una clase

# Los atributos o clases se encapsulan con un __ antes de su nombre

class empleado:
    def __init__(self,nombre=None, salario=0):
        self.__nombre = nombre
        self.__salario = salario

trabajador = empleado('Juan',2000)

# La única forma de acceder a los atributos es con la siguiente sintaxis
print('')
print(f'{trabajador._empleado__nombre} es un empleado que gana ${trabajador._empleado__salario}')
print('')

# Para evitar esta sintaxis se pueden emplear los metodos get(), set() y del()

class empleado:
    def __init__(self,nombre=None, salario=0):
        self.__nombre = nombre
        self.__salario = salario

    def getnombre(self):
        return self.__nombre

    def setnombre(self, name):
        self.__nombre = name


trabajador = empleado('Juan',2000)

print(f'El trabajador se llama {trabajador.getnombre()}')
trabajador.setnombre('Pepe')
print('El nuevo nombre del trabajador es: ',trabajador.getnombre())
print('')


# Las propiedades permiten administrar el encapsulamiento, permitiendo acceder a los métodos get,set,del como si se accediera al atributo

# Se emplea la función property(fget=get...,fset=set...,fdel=del...,doc='')  y las funciones get,set,del deben también encapsularse

# El siguiente ejemplo encapsula una función y la hace de solo lectura

class empleado:
    def __init__(self,nombre=None, salario=0):
        self.__nombre = nombre
        self.__salario = salario

    def __getnombre(self):
        return self.__nombre

    def setnombre(self, name):
        self.__nombre = name

    nombre = property(fget=__getnombre, doc=('Atributo de solo lectura'))


trabajador = empleado('Juan',2000)

print(f'El trabajador se llama {trabajador.nombre}')
print('')

help(trabajador)
print('')


