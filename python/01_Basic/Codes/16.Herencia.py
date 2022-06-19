# Herencia

class pokemon:
    def __init__(self,nombre,tipo):
         self.nombre=nombre
         self.tipo=tipo

    def descripcion(self):
        return '{} es un pokemon del tipo {}'.format(self.nombre, self.tipo)
         
    def ataque (self):
        return 'The pokemon has attacked'
    
class pikachu(pokemon):
    def ataque(self, ataque):
        return '{} tipo de ataque {}'.format(self.nombre,ataque)

class charmander(pokemon):
    def ataque(self, ataque):
        return '{} tipo de ataque {}'.format(self.nombre,ataque)


generic = pokemon('mio','cualquiera');
print(generic.ataque())


my_pokemon = pikachu('PikaPika', 'electrico')
print(my_pokemon.descripcion())
print(my_pokemon.ataque('impaktrueno'))
