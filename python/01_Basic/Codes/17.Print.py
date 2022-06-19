# Existen 3 formas de "formatear un string para imprimirlo

#Forma 1: .format

name = 'Alberto'
print('Hola {}. ¿Cómo estás?'.format(name))


num1 = 3.1416
num2 = 7.8123
print('La suma de {} y {} es {}'.format(num1,num2,num1+num2))
print('La suma de {b:1.2f} y {a:1.2f} es {c:1.2f}'.format(a=num1,b=num2,c=num1+num2))


#Forma 2: uso de %s

print('Hola soy %s y tengo %s años'%('Alberto', 26))

#Forma 3: uso de f-string
name = 'Alberto'
edad = 26
formacion = 'Ingeniería'
print(f'Hola soy {name}, tengo {edad} y estoy instruido en {formacion}')
