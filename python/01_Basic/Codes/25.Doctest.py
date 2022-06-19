# Los doctest permiten hacer pruebas de scritorio para funciones y clases
# Se definen entre la documentación empleando >>> """ """
# Se activan mediante el método testmod() en el módulo doctest
# Al lanzar el programa se debe incluir -v: python  ejemplo.py -v

import doctest

"""
Archivo que realiza operaciones básicas
"""

class operar:
    """
    Esta clase permite hacer operaciones básicas entre 2 números como:
    Suma, resta y  multiplicación
    """

    def suma(self, a, b):
        """ 
        Esta funcion suma 2 números 
        
        >>> operar().suma(1,2)
        3
        """
        return a+b

    def resta(self, a, b):
        """ 
        Esta función resta 2 números
        
        >>> operar().resta(4,2)
        3
        """
        return a-b

    def mult(self, a, b):
        """ 
        Esta función multiplica 2 números 
        
        >>> operar().mult(3,3)
        9
        """
        return a*b




if __name__ == '__main__':


    doctest.testmod()
