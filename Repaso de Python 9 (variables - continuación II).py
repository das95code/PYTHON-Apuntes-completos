# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:02:07 2021

@author: david
"""

#VARIABLES Y OBJETOS (continuación II)
#Este documento complementa a "Repaso de Python VIII (variables - continuación)

#OBJETOS
#En Python, cada dato que aparece en un programa es un objeto (número, cadena, lista...).
#Cada objeto tiene un identificador, un tipo y un alor.

#Identificador:
    #Cada objeto tiene un identificador único que se puede conocer mediante la función id():

id(5) #-> Identificador para el objeto número entero "5".
id(3.14) #-> Identificador para el objeto número decimal "3.14".
id("Hola") #-> Identificador para el objeto cadena de caracteres "Hola".
id([3,4,5]) #-> Identificador para el objeto lista "[3, 4, 5]".+

    #El identificador de un objeto es su posición en la memoria del PC.

#Tipo:
    #Cada objeto pertenece a un tipo de objeto. Se puede conocer mediante la función type():

type(5) #-> Nos indica que es un int (número entero).
type(3.14) #-> Nos indica que es un float (número decimal).
type("Pepe") #-> Nos indica que es un string (cadena de caracteres).
type([16,17]) #-> Nos indica que es un list (una lista).
type((5, 4)) #-> Nos indica que es un tuple (una tupla).

#Valor:
    #Se trata del propio dato que contiene el objeto. 
    

#CREAR Y DESTRUIR OBJETOS EN PYTHON
#Python crea los objetos a medida que los necesite y los destruye cuando ya no los necesita.
#El id puede cambiar al destruir y volver a crear un objeto.
#En el momento en el que una variable hace referencia a un objeto, ese objeto ya no se destruye.


#VARIABLES
#En Python las variables solo son referencias a objetos. Asemejamos la variable conm una etiqueta.
#Las variables también tienen identificador, tipo y valor, y coinciden con las del objeto al que hacen referencia.
#Cuando creamos una variable, se crea también un objeto que contiene la información, al que la variable señala.
#Cuando cambiamos el valor de una variable, en la mayoría de casos (siempre que no sea una mutación del objeto)
    #se creará un nuevo objeto al que la variable apuntará a partir de ese momento.
