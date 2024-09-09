# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:26:21 2021

@author: david
"""

#Haciendo un pequeño repaso a lo que vimos en Python IV (variables).....
#Los valores (números, cadenas, listas, etc) se almacenan en OBJETOS.
#Los objetos pueden ser inmutables (no pueden cambiar su valor):  Números, cadenas o tuplas.
#O pueden ser mutables (pueden cambiar su valor): Listas o diccionarios.
#Las variables son ETIQUETAS que SEÑALAN a esos OBJETOS.

#Al asignar una variable por primera vez en Python:
    #-Crea el objeto que contiene el valor (si aún no existe).
    #-Crea la variable.
    #-Asocia la variable al objeto, y a partir de ahora señala lo que contiene (señala a su valor).
    
#MODIFICAR VARIABLES
#Cuando asignamos un nuevo valor a una variable pueden pasar tres cosas con los objetos que señala asignados:
    #1.- Que el objeto sea inmutable:
        #En este caso la variable se asocia a un objeto distinto que contiene el nuevo valor.
        #Por ejemplo:
a = 10
print(a)
a = 20   #-> La variable "a" ahora señala a un nuevo objeto que contiene el valor 20.
print(a)

    #2.- Objeto mutable que no se modifica:
        #La variable se asocia a un objeto distinto que contiene el nuevo valor.
        #Ejemplo:
            
a = [10, 11]
print(a)
a = [20, 21] #->Asociamos la variable "a" a una lista diferente a la anterior.
print(a)

    #3. Objeto mutable que se modifica.
    #La variable se asocia al mismo objeto, y es el propio objeto el que se modifica.
    #Ejemplo
    
a = [10, 11]
print(a)
a[0] = 20 #->Modificamos los valores de la misma lista, por lo que el objeto cambia.
a[1] = 21
print(a)

#Al modificar una variable, se pueden modificar otras. Sucede cuando se modifica el objeto y hay otras variables que
#hacen referencia al mismo objeto.
#Pongamos varios ejemplos:
    
    #En un objeto inmutable:
a = 10
b = a
print ((a, b))
a = 20
print ((a, b)) #->Como hemos dicho que "b" apunta a lo que vale "a" cuando "a" señalaba al valor 10, "b" apuntará
                 #al valor "10" aunque "a" ahora señale a otro valor, puesto que un entero es inmutable.
                 
    #En un objeto mutable que no se modifica:
a = [20, 14, 10]
b = a
print ((a, b))
a = [15, 16, 17]
print ((a, b)) #->En este caso sucede lo mismo, "b" apuntará al valor que apuntaba "a" en el momento de su asignación.
                 #"b" seguirá apuntando al mismo valor aunque "a" ahora apunte a otro objeto diferente.

    #En un objeto mutable que se modifica:
a = [20, 14, 10]
b = a
print((a, b))
a[0] = 2      #->"b" señala el mismo objeto que "a". Si esta vez mutamos el objeto al que está señalando "a", también
a[1] = 3         #lo hará para "b" si también lo está señalando.  
a[2] = 4
print((a, b))

                 
#MODIFICAR VARIABLES Y OBJETOS MUTABLES
#Los objetos inmutables no se pueden modificar de ninguna manera. Al modificar la variable, asociamos la variable
#a un nuevo objeto.
#Los objetos mutables SI se pueden modificar. Al asociar una variable a un objeto mutable, podremos modificar el 
#objeto en algunos casos, pero en otros no.

#Modificar variables que no modifican listas:
    #El operador + no modifica el objeto. 
    #Ejemplo

a = [1, 2, 3]
b = a
a = a + [4] #-> No modificamos la lista. Creamos una lista nueva con un campo extra, y "a" ahora señala a esa nueva lista
print ((a, b))

#Modificar variables que modifican listas:
    #El operador += SÍ modifica el objeto.
    
a = [1, 2, 3]
b = a
a += [4] #-> El operador += AÑADE a la lista, no crea una nueva.
print ((a, b))

    #La función append() también modifica el objeto.
   
a = [1, 2, 3]
b = a
a.append(4) #-> Append es una función para añadir a una lista, y sí modifica un objeto.
print ((a, b))

    #Modificar un valor de una lista también modifica el objeto.
        
a = [1, 2, 3]
b = a
a[0]= 17 #-> Modificamos un valor de un campo de la lista.
print ((a, b))
    
    #Modificar el valor de una sublista también modifica el objeto.
        
a = [1, 2, 3]
b = a
a[1:1] = [80] #-> Estamos añadiendo el valor 80 a la posición 1 de la lista, el segundo campo.
print ((a, b))

#COPIAR UNA LISTA
#Para copiar una lista, debemos utilizar la notación de sublistas. Así conseguimos objetos independientes
#y aunque modifiquemos el objeto para "a", se mantendrá sin cambios para "b".

a = [1, 2, 3]
b = a[:] #-> "b" no apunta a la lista de a, si no a una copia que contiene todo el recorrido de la lista.
a[1:1] = [80] #-> Modificamos el objeto original.
print ((a, b)) #-> Aunque modifiquemos el objeto, para "b" no cambia porque "b" apunta a una copia.