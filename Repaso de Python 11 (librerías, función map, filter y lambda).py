# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:15:39 2021

@author: david
"""

#IMPORTAR LIBRERÍAS
#Podemos importar librerías escribiendo en una línea "import libreria", siendo librería el documento que queramos utilizar
#como tal o una librería ya creada para Python.
#Por ejemplo, si queremos calcular el área de un círculo, tendremos que importar la libería "math".
#Es preferible que las librerías se importen al principio de todo el documento, incluso antes de las funciones que vamos 
#a declarar.

#Ejemplo:

import math

def area_circulo(radio):
    return math.pi * radio ** 2  #-> Para llamar a una función localizada en una libería, utilizamos la sintaxis
                                     #nombredelalibrería.nombredelafunción, previamente importada la librería.   
radio = int(input("Introduce un radio para calcular el área del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo de radio {radio} es de {round(area, 3)}")


#LA FUNCIÓN MAP()
#La función map() se utiliza cuando queremos aplicar una función en cada elemento de una lista.
#La sintaxis de la función map es map(nombredelafunción, listaalaquequeremosaplicarlafunción)
#Con la función map recorreremos cada elemento de la lista y le aplicaremos la función deseada.
#Utilizaremos como ejemplo la función del área del círculo para una lista de radios:
    
import math  #-> El error sale porque importamos la librería en el ejemplo anterior.

def area_circulo(radio):
    return math.pi * radio ** 2 #-> Creamos nuestra función...

#El programa consistirá en calcular el área para una cantidad de círculos introducida por el usuario,
#con los radios también introducidos por el usuario.                                     

cantidad_de_circulos = int(input("Introduce la cantidad de círculos con la que quieres operar: "))
lista_de_radios = []  #-> Lista vacía que usaremos más tarde.
for i in range(1, cantidad_de_circulos +1):       #->Para cada valor de i en el rango (1, número de círculos + 1)                
    radio = int(input("Introduce un radio para calcular el área del círculo: ")) 
    lista_de_radios.append(radio) #-> Rercordamos que la función append añadía valores a listas.
    
area = list(map(area_circulo, lista_de_radios)) #-> Creamos una lista con el resultado de aplicar, a través de la función
                                                  #map(), la función area_circulo a todos los radios dados.
                                                  
for i, j in zip(lista_de_radios, area):   #-> Con la función zip(), podremos recorrer dos listas AL MISMO TIEMPO.
    print(f"El área del círculo con radio {i} es de {j}")
    
    
#LA FUNCIÓN FILTER():
#Sirve para aplicar un filtro a una lista y devuelve un iterador con los elementos que superan el filtro.
#Pongamos un ejemplo, dada una lista de números, queremos filtrar los negativos.

def es_negativo(numero):
    return (numero < 0) #-> En esta función se devuelve TRUE siempre que el número sea menor que cero.

def es_positivo(numero):
    return (numero > 0) #-> Y en esta otra, devuelve TRUE cuando el número sea mayor que cero.

lista_numeros = [-1, 2, 4, -8, -3, 6, -7, 10]

#Si aplicamos la función map() con la función es_negativo() a la lista, nos devolverá true o false dependiendo de los
#resultados aplicados a cada número de la lista.

print(list(map(es_negativo, lista_numeros))) #-> Devuelve una lista con true o false en cada caso.

#Sin embargo, si aplicamos la función FILTER, nos devolverá una lista filtrada de los elementos que son negativos.

print(list(filter(es_negativo, lista_numeros))) #-> Devuelve una lista con los valores negativos.


#LA FUNCION REDUCE():
#La funcion reduce aplica una función a una lista de datos evaluando los elementos por pares.
#La primera vez, la función reduce se aplica al primer y segundo elemento de la lista...
#La segunda vez, se aplicará al conjunto del primer y segundo elemento con el tercer elemento, y así sucesivamente.
#El objetivo de la función reduce es reducir la lista a un solo elemento.
#Para utilizar la función reduce, debemos importarla antes de la librería (o importar la lirería completa) FUNCTOOLS, pues no se encuentra
#como función integrada en Python.
#Por ejemplo:
    
lista_de_elementos = [1, 7, 10, 6, 15, 20, 2, 4] #-> Tenemos una lista de elementos que queremos reducir.

from functools import reduce  #-> Podemos importar solo la funcion que deseemos de la libreria, no es necesario importar la libreria entera.

def suma(a, b): 
   suma = a + b
   return suma #-> Creamos nuestra función suma.

sumatorio = reduce(suma, lista_de_elementos) #->Aplicamos con reduce la función suma a todos los elementos de la lista.

print("El sumatorio de la lista", lista_de_elementos, "es", sumatorio)     


#LA FUNCION LAMBDA():
#La función lambda se utiliza para simplificar funciones simples a funciones anónimas de una sola línea, que podremos guardar en variables.
#Todas las funciones lambda se pueden expresar como funciones normales, pero no viceversa.
#La función lambda tiene la siguiente sintaxis:
    #variable donde vamos a guardar el return = lambda argumentos con los que vamos a operar : lo que devuelve
    #Siendo los dos puntos el equivalente al return.
    
#Ejemplo de función lambda:
    
def suma(a,b):
    suma = a + b
    return suma  #-> Esta función simple tiene una sola linea en el cuerpo (aparte del return) y suma dos argumentos dados.

#Escrita como función lambda, sería:
    
suma = lambda a, b : a + b   #-> Funcion lambda con dos argumentos que retorna la suma de los dos argumentos.

print(suma(51, 27)) # -> Ahora cada vez que queramos sumar dos argumentos, los colocamos como argumentos entre paréntesis tras suma, como
                        #si suma fuese la función.
                        





    
    