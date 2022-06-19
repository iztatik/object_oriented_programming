# Los métodos de clase son métos que se pueden invocar sin necesidad se crear instancias de cierta clase

# Se decoran con @classmethod e invocan al constructor de la clase mediante 'cls' para pasarle los argumentos del constructor


class pastel:
    def __init__(self, ingredientes=None):
        self.ingredientes = ingredientes

    def __str__(self):
        return f'El pastel es de: {self.ingredientes}'
    
    @classmethod
    def pastel_chocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])

    @classmethod
    def pastel_limon(cls):
        return cls(['harina', 'leche', 'limón']) 

print(str(pastel.pastel_chocolate()))



# Los métodos estáticos son aquellos que no pueden acceder ni modificar los atributos y otros métodos de la clase
# Se pueden invocar sin instanciar la clase, i.e. crear un objeto
# No se les pasa el argumento self
#  Se crean con el decorador @staticmethod

class carro:
    def __init__ (self, color='Rojo', modelo=2020):
        self.color = color
        self.modelo = modelo

    @staticmethod
    def arrancar(velocidad):
        return f'El auto a arrancado a {velocidad} km/h'

# Se puede invocar SIN instanciar
print(carro.arrancar(25))

# Se puede invocar instanciando
jetta = carro('Negro', 2003)
print(jetta.arrancar(20))
