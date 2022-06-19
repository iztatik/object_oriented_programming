# Existen 2 tipos de errores en python: De sintáxis y excepciones
# Al conjunto de excepciones que Python maneja se les conoce como "Excepciones integradas"

# Las palabras reservadas empleadas para tratar excepciones son:
# try.- ejecuta una sección comprobando que no se presente una excepción
# except.- define un segmento que se ejecuta al presentarse una excepción
# else.- si no se presentó excepción se ejecuta esta sección
# finally.- Se ejecuta siempre, se halla o no presentado exepción
# raise.- lanza "manualmente" una excepción

try:
    while True:
        print("Ingrese dos números para dividir")
        a = int(input('Primer número: '))
        b = int(input('Segundo número: '))
        print('El resultado es:', a/b)

except KeyboardInterrupt:
    print('El programa se detuvo por interrupción de teclado')
except TypeError:
    print('Ha introducido datos no numéricos')
except ZeroDivisionError:
    print('Se ha realizado una división entre 0')
except :
    print('Error no considerado')
else:
    print('No se generaron excepciones')
finally:
    print('El programa ha finalizado')   
