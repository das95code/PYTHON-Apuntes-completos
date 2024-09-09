# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:27:29 2021

@author: david
"""
#TUPLAS

#En Python una tupla es un conjunto ordenado e INMUTABLE de elementos de diferente tipo.
#Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas.

ejemplo_de_tupla = (14, 17, "patata frita")

#Con la función len(), podemos devolver el número de elementos que contiene una tupla:
    
len(ejemplo_de_tupla)

#Una tupla puede no contener ningún elemento, y ser una tupla vacía.

tupla_vacía = ()
len(tupla_vacía)

#OPERACIONES CON TUPLAS
#Podemos referirnos a los elementos de las tuplas de forma individual indicando su posición entre corchetes.
#Las tuplas son inmutables, pero se pueden concatenar dando como resultado una nueva tupla distinta.
#Por ejemplo:
    
tupla1 = (14, 27, 18, "Grande, Ramón")
tupla2 = (7, 10, 14, "Gracias Nestor Perez")
tupla_concatenada = tupla1 + tupla2
                        
print(tupla_concatenada)


#______________________________________________________________________________________________________________

#LISTAS

#Las listas son elementos mucho más flexibles que las tuplas, y se pueden manipular de muchas formas.
#Se delimitan por corchetes "[]" y los elementos se separan por comas.
#Pueden contener elementos de cualquier tipo, números, cadenas de texto... incluso mezclados entre sí.

lista_de_ejemplo = [1, "Alfonso", "ir a comprar pan", 3, "Domingo"]

#Una lista puede contener más listas, y de hecho tener muchos niveles de anidamiento.

lista_de_listas = [["Paco", 17, 1995],["Jesús", 8, 1987],["Manolo, 24, 1973"]]
#La variable hace referencia a todo el contenido de la lista.

#Pueden existir listas vacías para, por ejemplo, rellenarlas más tarde.
lista_vacía = []

#Y una lista puede contener una variable.
#Vamos a llenar la lista vacía anterior con las distintas tuplas que hemos puesto de ejemplo en este resumen:

lista_vacía = [ejemplo_de_tupla, tupla_vacía, tupla1, tupla2, tupla_concatenada]
print(lista_vacía)

#Como siempre, debemos tener cuidado al modificar una variable que se ha utilizado para definir otras variables
#porque esto puede afectar al resto de variables, dependiendo si son mutables o no.

#Ejemplo no mutables:
    
nombre = "Pepe"
edad = 25
lista_Pepe = [nombre, edad]
nombre = "Juan"       #----> Aunque cambiemos la variable nombre a "Juan", la lista quedó definida antes
                            #por un objeto no mutable, por lo que no cambiará.
print (lista_Pepe)

#Ejemplo mutables:
nombres = ["Paco", "Pepe", "Antonio"]
edades = [25, 14, 20]
lista_total = [nombres, edades]
nombres += ["María Teresa de los Ángeles"] #-> En este caso al ser una lista un objeto mutable, afectará el cambio.
print(lista_total)

#Se puede acceder a cualquier elemento de una lista escribiendo la posición en la que se encuentra entre corchetes.
#Hay que tener en cuenta que la primera posición de la lista es la posición 0.
#Podemos concatenar dos o más listas de la misma forma que con las tuplas, con la operación suma.

lista_concatenada = nombres + edades
print(lista_concatenada)

#Como vimos antes, podemos añadir elementos a una lista con "+="

nombres += ["Perico de los palotes"]
print(nombres)

#Podemos manipular elementos individuales de una lista si especificamos su posición:

nombres[3] = "Rodrigo"
print(nombres)

#MANIPULAR SUBLISTAS
#De una lista podremos extraer sublistas utilizando la notación "nombredelalista[inicio:limite]"
#Inicio y límite funcionan de la misma forma que range(inicio,limite), que veremos más adelante.
#Por ejemplo:
print(nombres[0:3]) #->Si el inicio o el final coincide con el de la lista, como es el caso, no hace falta 
                        #que escribamos el "0" o el final, pudiendo escribir [:3], [3:] o [:] que pintara toda la lista.

#Utilizando las sublistas, podemos modificar uno o más elementos, o incluso insertar o eliminarlos.

nombres = ["Paco", "Pepe", "Manolo", "Rubén", "Carmen", "Sofía"]
nombres[:3] = ["Conejo"]  #--> Se sustituye la sublista con los 4 primeros campos por "Conejo"
print(nombres)

nombres[4:4] = ["Añadido"] #--> Inserta un nuevo valor en la lista, "añadido", justo al final de la misma.
print(nombres)

nombres[0:5] = [] #--> Borrará todo el contenido de la lista, dejándola vacía.
print(nombres)   

#Podemos utilizar valores fuera de rango en los corchetes que Python interpretará como extremos de la lista.

#PALABRA RESERVADA DEL
#Con la palabra reservada "del", podremos borrar campos de la lista o incluso la lista entera.
nombres = ["Paco", "Pepe", "Manolo", "Rubén", "Carmen", "Sofía"]
del nombres[4]
print(nombres)
del nombres
#print(nombres) #-->Da error porque no existe la variable.


#COPIAR UNA LISTA
#Como comentamos antes, las listas son mutables, y si queremos copiar una variable que contiene una lista
 #para no perder su valor, y modificamos la variable original, la copia que contiene la lista también se verá modificada
#No obstante, utilizando la notación de sublistas podremos evitar este problema, ya que se guardan en espacios de 
 #la memoria diferentes.
 
lista1 = ["A","B","C"]
lista2 = lista1[:] #---> Copiamos la lista1 mediante notación de sublistas
lista1 = ["A","B"]
print(lista1, lista2) #--->Comprobamos que efectivamente hemos guardado la lista1 original.


#RECORRER UNA LISTA
#VOLVEREMOS A ESTE PUNTO CUANDO DEMOS EL BUCLE FOR!!!!
#REVISAR EL DOCUMENTO "REPASO DE PYTHON VII (ESTRUCTURAS DE CONTROL, FOR Y WHILE)"

#Podemos recorrer una lista de principio a fin de dos formas distintas:
    
    #Con un bucle for normal y corriente que recorra la lista:
lista = ["Paco", "Pepe", "Alfonso", "Luciano", "Keko", "Anxo", "Adri"]
for i in lista:
    print(i)
print("Fin del programa")

    #Con un bucle for donde la variable "i" recorra el rango de la longitud de la lista:
for i in range(len(lista)):
    print(lista[i]) #-> Lo tenemos que escribir de esta forma porque si pusiesemos solo print(i), escribiría LA POSICION
print("Fin del programa")

#La primera forma de recorrer la lista es más sencilla, pero solo permite recorrer la lista de principio a fin
#y utilizar los valores de la lista. La segunda forma es más complicada, pero permite más flexibilidad.
#Por ejemplo, con range(len(lista)) podemos recorrer la lista al revés:
    
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
print("Fin del programa")

#Podemos también modificar los elementos de una lista:

for i in range(len(lista)):
    lista[i] = "Desconocido"
    print(lista)
print("Fin del programa")

#Podemos eliminar elementos de una lista:
    #Para ello, vamos a recorrer la lista al revés, ya que si la recorremos de principio a fin, al eliminar un valor
    #de la lista, esta se va acortando y cuando intenta acceder a los últimos valores dará un error de índice
    #fuera de rango. Sin embargo, recorriendo la lista en orden inverso, de forma que aunque la lista se acorte, 
    #los valores que aún no se han recorrido sigan existiendo.

for i in range(len(lista)-1, -1, -1):
    del lista[i]
    print(lista)
print("Fin del programa")

#Saber si un valor etá o no está en una lista:
    #Para saber si un valor está en la lista utilizamos el operador "in", devolviendo true si está y false si no está.
    #En el siguiente ejemplo comprobaremos si una persona está autorizada o no (si aparece en la lista).

personas_autorizadas = ["Paco", "Ramón", "Anxo", "Keko", "María del Carmen", "Adri"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
    print("Está autorizado, puede pasar.")
else:
    print("No está autorizado para pasar.")
    
    #También podemos utilizar, de manera inversa, "not in" para saber si un valor no está en la lista.
    #En este caso devolvería true si NO está en la lista, y false si sí lo está.

#____________________________________________________________________________________________________________________
#RANGOS
#El elemento range es una lista INMUTABLE de números enteros en sucesión aritmética.
#Al ser inmutables, no se pueden modificar.
#En una sucesión aritmética, la diferencia entre dos términos consecutivos es siempre la misma.
#Podemos crear un range con uno, dos o tres argumentos numéricos.

#El range() con un solo argumento se escribe range(n), y crea una lista inmutable de n números enteros que empieza en 0 
#y acaba en n-1.
#Para poder ver los valores que adquiere el range, es necesario convertirlo a lista mediante la función list().
#Veamos un ejemplo:
    
list(range(7)) #-> Se pintará una lista con los valores desde 0 hasta 7-1, o sea, 6

#Si n no es un número positivo, se crea un rango vacío (lista vacía).

list(range(-2))

#El range() con dos argumentos se escribe range(m, n), y crea una lista inmutable de enteros consecutivos que
#empiezan en m y terminan en n-1. 
#Por ejemplo:
    
list(range(2, 15)) #-> Pintará una lista desde el 2 hasta el 14.

#De nuevo, si le damos a n un valor menor que el valor de m, saldrá un rango vacío (lista vacía).

list(range(15, 2)) #-> Rango vacío.

#El range() con tres argumentos se escribe range (m, n, p), la "m" indica el valor inicial del rango,
#la "n" indica el valor final (no lo alcanzaremos nunca) y la "p" indica el paso (la cantidad que se avanza cada vez)
#Ejemplo:

list(range(2, 10, 2)) #-> Pintará números desde el 2 hasta el 9 de dos en dos. (Solo los pares.)

#Si escribimos solo dos argumentos, "p" vale por defecto 1.
#Si escribimos solo un argumento, "p" vale por defecto 1 y "m" vale por defecto 0.
#Solo podemos escribir ranges con argumentos enteros, nucna decimales.


#CONCATENAR LOS RANGE
#Un elemento range como tal no se puede concatenar con otro, pero sí podemos concatenarlos si previamente los
#convertimos en listas. El resultado será una lista que no podemos convertir al tipo range().

list(range (2, 15)) + list(range(2, 10, 2)) #-> Concaternará las dos listas.

#LA FUNCIÓN LEN()
#La función len() devuelve la longitud de una cadena de caracteres o el número de elementos de una lista.
#Su argumento es la lista o cadena que queremos "medir".
#Por ejemplo:
    
len("Hola grupo feliz hagolui soy Vanesa.") #-> Medirá la cadena de caracteres.
len([15, 14, 13, 12, 11, 10, 9, 8]) #-> Medirá el número de valores de la lista.
len(range(3, 100, 7)) #-> Medirá la cantidad de números enteros que compongan el rango asignado. 

#El valor devuelto de la función len() se puede utilizar como parámetro del range():
list(range(len(["Paco", "Pepe", "Montse", "Jesus", "Abelardo", "José Tomás"])))