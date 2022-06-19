# 1.- filter() permite discriminar los valores de un conjunto (iterable) basdo en una funcion condicional

# Función condicional que discrimina si un numero es par
def positivo(i):
    if i > 0:
        return True
    else:
        return False


lista = [l for l in range(-7,7)]
print('')
print('La lista original es: ',lista)
print('')

# La funcion filter genera un objeto que recibe como argumentos la funcion condicional y la lista
# Filter itera automaticamente la lista en la función
filtro = filter(positivo, lista)
print('La función filter() devuelve el objeto: ', filtro)

# Es necesario convertir el objeto a una lista para ver su contenido
print('Convertido a lista contiene (positivos): ', list(filtro))
print('')


# 2.- map() permite aplicar una operacion a todos los elementos de una lista basado en una función
# Funciona casi igual que la funcion filter()
# Esta funcion puede ser un lamda

mult = lambda i: i*2

# map() itera automáticamente la lista en la fucnión y genera un objeto
mapeo = map(mult, lista)
print('map() devuelve el objeto: ', mapeo)

# si lo convertimos a lista para ver resultado
print('Convertido contiene (x2): ', list(mapeo))
print('')

 





