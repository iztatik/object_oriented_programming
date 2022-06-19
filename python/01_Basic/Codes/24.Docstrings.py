# Los docstrings permiten documentar objetos y funciones
# Se definen entre 3 comillas """ Docstring """
# Se invocan con la funcion help y el nombre del objeto help(objeto)
"""
Archivo que realiza operaciones básicas
"""

class operar:
    """
    Esta clase permite hacer operaciones básicas entre 2 números como:
    Suma, resta y  multiplicación
    """

    def suma(self, a, b):
        """ Esta funcion suma 2 números"""
        return a+b

    def resta(self, a, b):
        """ Esta función resta 2 números"""
        return a-b

    def mult(self, a, b):
        """ Esta función multiplica 2 números"""
        return a*b




if __name__ == '__main__':
    my_op = operar()

    if input('Desea invocar la documentación s/n: ')=='s':
        help(operar)
    else:
        pass

    a = int(input('Introduzca el primer número: '))
    b = int(input('Introduzca el segundo número: '))

    print('La suma es: ',my_op.suma(a,b))
    print('La resta es: ',my_op.resta(a,b))
    print('La multiplicación es: ',my_op.mult(a,b))

