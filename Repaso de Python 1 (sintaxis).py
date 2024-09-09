# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:00:49 2021

@author: david
"""

#Esto es una serie de comandos sin relación entre sí para practicar lo que hemos estudiado hasta ahora

print ("Hola mundo")

variable = 18
print (variable)

#El área de un círculo

r = 5
area = 3.1416 * r **2
print (area)

#Las contrabarras \ sirven para continuar una línea en la siguiente de la siguiente forma

print ("Esta es una \
sola línea \
dividida en tres")

#Para generar una línea en blanco, se puede escribir una orden print() sin argumentos.
print("Hola")
print()
print("Adiós")

#Si no se quiere que Python añada un salto de línea al final de un print(), se debe añadir al final el argumento end="":
print("Hola", end=" ")
print("Adiós")

#Para meter comillas dentro de comillas, se introducen simples dentro de dobles o viceversa, o colocamos una barra delante de la comilla que queremos pintar.
print("Mi madre me dijo 'compra pan'")
print ("Mi madre me dijo \"compra pan\"")

#Introducir variables en el print

nombre = "Pepe"
edad = 25

print("Hola, me llamo", nombre, "y tengo", edad, "años.")

#Diferentes formas de usar el comando input y la cadena f

print("Hola, ¿como te llamas?")
nombre = input()
print ("¡Encantado de conocerte,", nombre, end="!")

print("Hola, ¿como te llamas? ", end="")         #PREGUNTAAAAAAR (¿por qué se hace el salto de línea?)
nombre = input()
print("¡Encantado de conocerte,", nombre, end="!")

nombre = input("Hola, ¿cómo te llamas?: ")
print(f"¡Encantado de conocerte {nombre}", end="!")      #Mismo resultado, pero tiramos menos líneas


nombre = input("Escribe tu nombre: ")
apellido1 = input("Escribe tu primer apellido: ")
apellido2 = input("Escribe tu segundo apellido: ")
print()
print()
print(f"Tu nombre completo es {nombre} {apellido1} {apellido2}.")

#Para que Python interprete el input como un número ENTERO y poder operar con él, debemos acompañar al input de la función int


evaluacion1 = int(input("Introduce la nota que sacaste en la primera evaluación: "))
evaluacion2 = int(input("Introduce la nota que sacaste en la segunda evaluación: "))
evaluacion3 = int(input("Introduce la nota que sacaste en la tercera evaluación: "))
notafinal = (evaluacion1 + evaluacion2 + evaluacion3)/3
print()
print()
print(f"La media de tus tres evaluaciones es de {notafinal}")

#Utilizaremos el comando float para que input acepte números con decimales. NO produce error si se escribe un número entero.

temperatura1 = float(input("Introduzca la temperatura corporal que tuvo a las 12:00: "))
temperatura2 = float(input("Introduzca la temperatura corporal que tuvo a las 16:00: "))
temperatura3 = float(input("Introduzca la temperatura corporal que tuvo a las 20:00: "))
tempmedia = (temperatura1 + temperatura2 + temperatura3)/3
print()
print()
print(f"Su temperatura corporal media ha sido de {tempmedia} grados")

#Me he quedado resumiendo en la página 65