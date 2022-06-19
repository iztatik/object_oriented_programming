# Un iterable es una estructura que puede ser iterada n veces 
# Las listas[], tuplas(), y strings son ejemplos de iterables

iterable = 'Hola mundo'

print('Esto es un iterable: ', repr(iterable))
for i in iterable:
    print(i)

# Los iteradores son objetos que solo pueden iterarse una vez mediante la función next()

iterador = iter(iterable)

print('\nEsto es un iterador hecho desde un iterable: ', iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))

# Si se desborda el iterable usando de más la función next() se genera un error

# Se pueden crear iteradores mediante un GENERADOR usando yield en lugar de return en una función

def f_iterador(rango):
    for i in range(rango):
        yield i

iterador = f_iterador(5);

print('Esto es un iterador hecho con Generador: ', iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))



