                #Bucles con ciclo FOR

#Imprimir el contenido de una cadena
cadena = [1,2,"gato",True,5]
print("Cadena:")
for numero in  cadena:
    print(" ",numero,end="") # end="" evita que se genere salto de linea
    
print()                      #Imprime un salto de linea



#Imprimir el contenido de un string
my_string = 'Roco Bolt'
print('String:',my_string)
for cadena in my_string:
    print (cadena)


#Contador con ciclo For
x=30;
for i in range(30):
    for j in range(x):
        print ('*',end="")
    print()
    x=x-1
    
