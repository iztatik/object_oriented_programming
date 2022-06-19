import pickle

# Creamos un archivo binario
fichero = open('colores.pckl','wb')
lista_w = ['azul', 'verde', 'rojo']
pickle.dump(lista_w, fichero) # Serialización de la lista y grabación en archivo
fichero.close()


#Leemos el archivo binario 
fichero = open('colores.pckl','rb') #Deserialización y lectura
lista_r = pickle.load(fichero)
print(lista_r)
