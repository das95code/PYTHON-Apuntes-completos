# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:03:05 2021

@author: david
"""

# En Python, podemos comparar las variables con "etiquetas" que señalan hacia una información, no la contienen.
# Mediante el operador "=" lo que hacemos es una ASIGNACIÓN: le asignamos una información a una variable, que lo señala.
# Las variables siempre deben aparecer al principio del "=", y a su derecha, lo que contienen.
# A una variable le podemos asignar números de cualquier tipo, cadenas de texto, conjunto de números o texto
        #u otras estructuras más complicadas como diccionarios, etc...

x = 15 #-> x señala a un número entero
y = "Paco" #-> y señala a una cadena de caracteres
z = [1,2,3,4,5] #-> z señala a una lista

# La info que señalan las variables se guardan en objetos, y según la información que contengan, hay 2 tipos de objetos.
# Los objetos inmutables son objetos que no se pueden modificar (números, cadenas o tuplas).
# Los objetos mutables son objetos que sí se pueden modificar (listas, diccionarios).

#Por economía del lenguaje, sí que utilizamos la expresión "guardar un valor en una variable",
    #aunque realmente esto no sea así y lo que haga sea "señalar a un objeto que contiene un valor".
    
#La instrucción "del" borra completamente una variable.

x = 15
del x

#Los nombres de las variables no puede incluir espacios en blanco. Por convenio, se utilizan minúsculas y "_" para espacios
#Tampoco se recomienda utilizar "ñ" o cualquier otro caracter que no esté en el alfabeto inglés.
#Python distingue entre mayusculas y minusculas. Hay que tener esto en cuenta a la hora de referenciar variables.

anio_de_nacimiento = 1995

#UTILIZACION DE VARIABLES
#Cuando hemos creado una variable, la podemos utilizar para hacer cálculos o para definir nuevas variables:
    
horas  = int(input("Introduzca las horas que desea convertir a segundos: "))
minutos = 60 * horas
segundos = 60 * minutos
print (f"{horas} horas son {minutos} minutos, o también {segundos} segundos.")

#Teniendo en cuenta que las variables son etiquietas que SEÑALAN objetos y no los contienen,
#podemos redefinir una variable a partir del propio valor que está señalando, por ejemplo:
    
a = 1
a = a + 10
print(a)

#Tenemos que tener en cuenta que al modificar el valor al que señala una variable, el valor anterior se pierde.

#Podemos también operar con dos variables

peras = 20
manzanas = 30
frutas = peras + manzanas
print (frutas)

#Si se trata de objetos inmutables, el resto de variables implicadas no resultan afectadas al modificar una variable.

a = 10
b = a
print ((b,a))
a = 30
print ((b,a))

#Si se trata de objetos mutables, el resto de variables implicadas SÍ resultan afectadas
a = [5,10,15,20,25]
b = a
print(a,b)
a[0] = 7
print (a,b)

#ASIGNACIONES AUMENTADAS EN LAS VARIABLES
#Podemos utilizar la asignación aumentada para modificar variables a partir de su propio valor.
#Solo para objetos MUTABLES.
#Aquí tenemos una lista de equivalencias

# a += b      -> equivale a    a = a + b
# a -= b      -> equivale a    a = a - b
# a *= b      -> equivale a    a = a * b
# a /= b      -> equivale a    a = a / b
# a **= b     -> equivale a    a = a ** b
# a //= b     -> equivale a    a = a // b
# a %= b      -> equivale a    a = a % b

#En Python no podemos utilizar el incremento (a++) o (a--) que sí existe en otros lenguajes.