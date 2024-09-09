# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:40:21 2021

@author: david
"""

#FUNCIONES
#Una función se utiliza principalmente para reutilizar código ya escrito y volver a ejecutar un bloque o una operación
#sin tener que volver a escribir esa parte del código.
    #Las funciones (o subrutinas) tienen muchas ventajas:
        #Ahorran trabajo, facilitan el mantenimiento, simplifican el código y facilitan la creación de programas.

#Si una función se va a utilizar en un solo programa, se puede definir en el propio programa.
#Si una función se piensa utilizar en varios programas, se puede incluir en un fichero aparte que se puede importar en cada
#programa. Este fichero se conoce como librería.        
#En Python, se utiliza el término función para referirse a las subrutinas y módulo para referirse a las librerías.

#CREAR FUNCIONES
#Una función se puede definir en cualquier punto del programa, siguiendo el siguiente procedimiento.
    
    #1ª línea: Contendrá la palabra def, seguido del nombre de la función y los paréntesis.
                #Se aconseja que el nombre de la función se ajuste a la nomenclatura estándar de Python.
                #Los paréntesis podrán contener argumentos utilizados que se encuentren fuera de la función.
    
    #2ª línea y en adelante: Las instrucciones de la función, con al menos un sangrado más que el de la primera línea.
    
    #Por comodidad, al final de la función se suele utilizar la palabra reservada "return", aunque no es obligatorio.
    #Para poder utilizar una función, antes debe haberse definido o importado. Por norma general, y si es dentro del
    #propio programa, las funciones se definen arriba del todo, antes del código.
    
    #Ejemplo de función:
        
#def funcion_pintar_numeros_pares(x): #->La función trabaja con un argumento "x" que se encuentra fuera de la función.


def funcion_pintar_numeros_pares (x):  #-> Primero definimos la función.
    contador = 0    #-> El cuerpo de la función debe ir con al menos un tab de sangrado respecto a la primera línea.
    while contador < x:
        for num in range(1, (x*2 +1)):
            if num % 2 == 0:
                print (num, "es un número par.")
                contador = contador + 1


x = int(input("Escribe la cantidad de números pares desde 0 hasta n que quieres pintar: "))        
#Para hacer la función más heterogénea, todo lo que pueda interferir en el uso de la función por otros programas 
#lo sacaraemos de la función (siempre que este paso sea posible). En este caso sacaremos el input para pedir números.

funcion_pintar_numeros_pares(x) #-> Llamamos a la función.

print("Esos son los", x, "primeros números pares.") #-> El print final también lo sacamos de la función.


#VARIABLES EN FUNCIONES
#Si la función que pegamos en un programa utiliza alguna variable auxiliar para algún cálculo intermedio 
#(véase un contador, un acumulador o una simple variable auxiliar para almacenar un dato) y resulta que ya teníamos
#en nuestro programa fuera de la función una variable con ese nombre, la variable de la función podría modificar el valor
#de la variable del programa y, con ello, el buen funcionamiento del programa.
#Para resolver esto, Python permite que la variable exista solo dentro de la función, por lo que hablamos de programación
#a varios niveles. El nivel principal sería nuestro programa, y los niveles más bajos las funciones, 
#las funciones dentro de funciones, etc...
#No obstante, a veces nos interesará que las funciones modifiquen nuestras variables del programa.
#Para ello, el lenguaje de programación actuará de la siguiente manera:
    
    #Cada variable pertenece a un ámbito determinado: programa principal o función.
    #Las variables son completamente inaccesibles en los ámbitos superiores al ámbito al que pertenecen.
    #Las variables pueden ser accesibles (o no) en ámbitos inferiores al que pertenecesn.
    #En cada función, las variables pueden ser LOCALES o LIBRES.
    
#Variables locales:
    #Si no se han declarado no locales o globales, las variables de una función serán locales y solo existen en la
    #propia función. Por ejemplo:
        
def funcion():
    a = 2
    print(a)
    return 

a = 5
funcion()
print(a)  #-> La variable "a" del programa no se ve afectada por la variable "a" de la función.

    #De la misma manera, las variables locales no pueden ser accesibles desde niveles superiores, veamos ejemplo:

def funcion2():
    b = 5
    return
        
funcion2() 
print(b)  #-> No nos deja acceder a la variable de la función, y no se puede pintar porque no está declarada en nuestro
            #programa.
            
#Variables libres globales y no locales:
    #Si a una variable no se le asigna valor en una función, Python la considera variable libre y busca su valor en
    #los niveles superiores del programa, escalando desde el inmediatamente superior al principal. Si a la variable se le
    #asigna un valor en un nivel intermedio entre el programa y la función se considera no local. Si encuentra dicha
    #variable en el programa principal, se considera variable global.
    #Ejemplo de variable global:
        
def funcion3():
    print(c)  #->Al no tener valor dentro de la función, tomará su valor del programa principal y lo considerará
    return      #variable libre global.

c = 8
funcion3()
print(c)


#ARGUMENTOS Y DEVOLUCIÓN DE VALORES
#Las funciones en Python admiten argumentos en su llamada y permiten devolver valores.
#Estas posibilidades permiten crear funciones más útiles y reutilizables.
#Los argumentos permiten enviar valores externos a la función con los que trabajar. Ejemplo:
    
def media_de_numeros(x,y): #->Definimos nuestra función con dos argumentos, x e y.
    media = (x + y) / 2
    print(f"La media de {x} y de {y} es: {media}")
    return
    
numero1 = 5
numero2 = 6
media_de_numeros(numero1, numero2) #->Cuando llamemos a la función, colocamos los argumentos que queramos usar
print("Programa terminado")          #en el lugar que ocupan "x" e "y".

#No obstante, esta función puede ser aún más flexible. Si extraemos de la función el print media, podremos utilizar
#la función en otras operaciones que requieran la media, pero no su print. Quedaría de la siguiente manera:
    
def media_de_numeros(x,y): #->Definimos nuestra función con dos argumentos, x e y.
    resultado = (x + y) / 2
    
    return (resultado)
    
numero1 = 5
numero2 = 6
media = media_de_numeros(numero1, numero2) #->Nuestra variable media será el resultado del return de la función.
print(f"La media de {numero1} y de {numero2} es: {media}") #-> Extraemos el print y lo adaptamos a nuestro programa.
print("Programa terminado")          

#Y aún con esas, la función puede ser todavía más polivalente. Ahora mismo admite dos argumentos. Hagamos que pueda
#admitir una cantidad indeterminada de valores.

def calcula_media(*args): #-> Escribiendo "*args" como argumento, admitiremos todos los valores que queramos meter.
    total = 0
    for i in args: #-> Con un bucle for, recorreremos todo el valor de args desde 1 hasta args.
        total += i #-> Y sumamos el total a nuestro contador.
        resultado = total / len(args)
    return resultado

a, b, c = 3, 5, 10
media = calcula_media(a, b, c)
print(f"La media de {a}, {b} y {c} es: {media}")
print("Programa terminado")

    