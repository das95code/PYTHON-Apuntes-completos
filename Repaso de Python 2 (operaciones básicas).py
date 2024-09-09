# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:46:19 2021

@author: david
"""

# Para escribir un número decimal, separaremos la parte decimal de la entera por un "."
# Si ponemos un número con parte decimal 0, python lo interpretará como un float.

x = 7.0
y = 0.65334

# Las operaciones básicas son la suma, la resta, la multiplicación y la división.

x = 7+2
y = 4.5-3.2
z = 37*4.5
w = 52/3    #El resultado de la y y la w presenta errores de redondeo comunes en python al trabajar con binario.

print (f"El resultado de las operaciones son x = {x}, y = {y}, z = {z}, w = {w}")

#Dividir por cero genera un error. Las operaciones se ejecutan siguiendo la regla de prioridad matemática.
#Se pueden utilizar paréntesis para dar prioridad a ciertas operaciones.

x = 10/0 #-> Va a dar error.
y = 14*7+24*(27-15)/3

print (y)
print (x)

#Podemos calcular el cociente de una división con la doble barra "//".
#El cociente será siempre un número entero. Si estamos dividiendo números decimales, se representará como "X.0".

x = 14//2
print (f"El cociente de la división 14 entre 2 será {x}")

#El resto de una división se calcula con "%". El resultado puede tener entero o decimal.
#Se puede utilizar, por ejemplo, para saber si un número es par o impar.

x = 16%2
print (f"El resto de la división 16 entre 2 será {x}, por tanto, 16 es un número par.")

#La función integrada divmod(x,y) devolverá una tupla formada por el cociente y el resto de la divisón de x entre y.

z= divmod(14, 2)
print (z)

#Las potencias se calculan con el operador "**", y tienen prioridad sobre multiplicaciones y divisiones.
#Si utilizamos exponentes negativos o decimales, podremos calcular también raíces n-esimas.

x = 14**7
y = 81**0.5 #-> Calculamos la raíz cuadrada de 81.

print (x)
print (y)

#Podemos utilizar la función pow(x,y)  para calcular también funciones y raíces

x = pow(14, 2)
y = pow(49, 0.5)

print (x)
print (y)


#REDONDEO
#Para redondear un número podemos utilizar la función integrada round(). Se redondeará al entero más próximo.
#Solo debemos redondear un número en el momento de mostrarlo por pantalla, no si vamos a seguir operando con él.

x = round(273.531412531241234434)
print (x)

#Podemos utilizar la función round con dos argumentos round(x,y). Se redondeará el primer argumento a la posición
#que marca el segundo argumento.

x = round(273.2131234512352344141, 5)
print (x)

#Si el segundo argumento es un cero, redondeará, de la misma forma que si no escribiésemos segundo argumento, al entero
#más próximo.
#Si el segundo argumento es negativo, redondeará a las decenas, centenas, etc...

x = round(273.213152341412343124, 0)
y = round(273.35125435412614356241, 2)
print(x)
print(y)


#OTRAS FUNCIONES INTEGRADAS
#Podemos mostrar el valor absoluto de un número (el número sin signo) con la función abs().

print(abs(7))
print(abs(-12))

#Con la función integrada max() calcularemos el valor máximo de un conjunto de valores.
#Esto se puede aplicar a cadenas de caracteres, cuyo valor máximo se corresponderá al último valor en orden alfabético.
#Los caracteres acentuados tienen "mayor valor" que los caracteres normales, y van después.

print(max(14,15,16,20,1,3,5))
print(max("Pepe", "Roberto", "Angelines", "Mamerto", "Álvaro"))

#La funcion sum() calcula la suma de un conjunto de valores.
#Debe ser un conjunto de datos ITERABLE. (tupla, rango, lista, conjunto o diccionario.)
print(sum((1,2,3,4,5,6))) #-> tupla
print(sum([1,2,3,4,5,6])) #-> lista
print(sum(range(6)))      #-> conjunto (rango)
print(sum({1,2,3,4,5,6,})) #-> diccionario

#Con la función integrada sorted() podemos ordenar un conjunto de valores. También debe ser un conjunto ITERABLE.
#Con esta función, devolveremos el conjunto de datos ordenado.
#La función devolverá una LISTA con los valores ordenados.

print(sorted((21,12,34,54,12,44,4)))