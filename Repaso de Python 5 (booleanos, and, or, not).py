# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:46:33 2021

@author: david
"""

#BOOLEANOS 
#Las variables booleanas solo pueden tomar dos valores, true y false.
#En Python, cualquier variable puede considerarse como una variable booleana.
#Los elementos vacíos o nulos se consideran false, y el resto se consideran true.
#Mediante la función integrada bool() podemos comprobar si una variable se considera true o false.

bool(0) #->Es nulo, dará false
bool("") #->Está vacío, dará false
bool([]) #->Elemento vacío; false.
bool(25) #->True
bool("Moñeco") #->True
bool((17,24)) #->True

#OPERADORES LÓGICOS
#Sirven para trabajar con valores booleanos:
    #AND: Es el "y" en lógica. Devuelve true solamente si sus dos operadores son true.
    #OR: Es el "o" en lógica. Devuelve true si se cumple que alguno de sus dos operadores sean true.
    #NOT: Es una negación. Da como resultado true solo si su argumento es false.
    
#Podemos realizar operaciones compuestas con los operadores.
#Se recomienda el uso de paréntesis para asegurar el orden deseado.
#No obstante el orden de prioridad es el siguiente
    # NOT > AND > OR

#Las comparaciones también dan como resultado booleanos.
# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que
# == Igual que
# != Distinto que

#Notese que comparar "==" no es lo mismo que asignar "="
#En Python se permite el encadenado de comparaciones, y el resultado será true SOLO si todas la comparaciones son true.