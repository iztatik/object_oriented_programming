 # Los métodos mágicos __str__ y __repr__ permiten imprimir un string asosiado a un objeto


#Caso 1: Imprimir un objeto sin definir __str__ o __repr__
# Al imprimir obtenemos nombre de la clase y posición hexadecimal de memoria
class humano:
    def __init__(self,nombre=None, edad=18):
        self.nombre = nombre
        self.edad=edad

my_human = humano()

print('')
print('CASO 1: Impresion por default: <Name + HEX direction>')
print(my_human)
print('')


#Caso 2: Imprimir un objeto con __str__  usando str()
#  __str__ da una representación INFORMAL, i.e. que solo será leida por el usuario humano
class humano:
    def __init__(self,nombre=None, edad=18):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre} es un humano de {self.edad} años'

my_human = humano('Alberto', 26)
print('CASO 2: Impresion con __str__ + str()')
print(str(my_human))
print('')


#Caso 3: Imprimir un objeto con __str__  usando str()
#  __repr__ da una representación FORMAL,
# i.e. que tiene la sintaxis adecuada para ser evaluada (convertida a código interpretable) por la función eval(). 
# No es texto hecho para ser amigable con el usuario. 

class humano:
    def __init__(self,nombre=None,edad=0):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f'humano({self.nombre !r}, {self.edad})'

# NOTE: Emplear !r para indicar que la variable del argumento es un string

my_human = humano('Alberto',26)
print('CASO 3: Impresión con __repr__ + repr()')
print(repr(my_human))
print('')

# Podemos crear un segundo objeto identico a my_human si evaluamos su __repr__ con eval
my_human2 = eval(repr(my_human))
print('Creamos un segundo objeto identico al primero mediante eval(repr())')
print(repr(my_human2))
print('')
