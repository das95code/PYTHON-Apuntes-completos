# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:20:28 2021

@author: david
"""

#SENTENCIAS IF/ELIF/ELSE

#If, elif y else condicionan la ejecución de uno o varios bloques de sentencias si se cumplen una o varias condiciones.
#La sentencia IF se traduce como "si", y permite que el programa ejecute las instrucciones SI se cumple esa condición.
#La sentencia se evalúa siempre. Si el resultado es true, se ejecuta, si es false, se salta al siguiente bloque sin ejecutar

#Utilizamos ELIF como if consecutivo a ifs anteriores. Si la instrucción no cumple la condición del primer if, 
#salta al siguiente bloque y se comprueba con las nuevas condiciones que reclama el nuevo elif.

#Finalmente, ELSE se traduce como "si no". Indica el procedimiento a seguir si no se cumples las condiciones de los if/elif.

#Ejemplo de cadena de sentencias IF/ELIF/ELSE:
    
numero_pedido = int(input("Escribe un número del 1 al 20: "))

if numero_pedido > 0 and numero_pedido <= 10:    #-> Si no se cumple la condición 1, pasará al elif.
    print ("El número que has escrito está en el primer grupo.")
elif numero_pedido >10 and numero_pedido <=20:   #-> Si no se cumple la condición 2, pasará al else.
    print ("El número que has escrito está en el segundo grupo.")
else:   #-> Lo que hay en el else sucederá siempre y cuando la instrucción no cumpla los requisitos de los "if/elif".
    print ("El número que has escrito está fuera de rango.")
    
#__________________________________________________________________________________________________________________________

#ESTRUCTURAS DE CONTROL, ITERACIONES Y BUCLES

#BUCLE FOR
#Un bucle sirve para repetir un bloque de instrucciones.
#El bucle FOR repite el bloque un número predeterminado de veces, cada repetición se llama iteración.
#La sintaxis de un bucle for es la siguiente:
            
        #for variable in elementoiterable(lista, cadena, range, etc):
                #cuerpo del bucle

#No es necesario (aunque es posible) utilizar una variable definida anteriormente entre el "for" y el "in".
#El cuerpo del bucle se ejecutará tantas veces como valores tenga el elemento iterable.
#Pongamos un ejemplo:
    
lista_numeros = [1,2,3,4,5,6,7]

for valor in lista_numeros:  #--> Siendo valor cada uno de los valores de la lista
    print(valor) #--> Por cada valor en la lista, pintame el valor.
print("\nFinal") #--> Un print "final" fuera del bucle para comprobar que hemos terminado.
    
#Si la lista estuviera vacía, el bucle no se ejecuta ninguna vez.
#Si la variable de control no se va a utilizar en el cuerpo del bucle, podemos utilizar "_" como nombre
    #de esta forma indicamos a la persona que lea nuestro código que no se va a utilizar dicha variable.
#Como norma general, se suele utilizar la "i" como variable de control.

#Podemos utilizar una cadena de caracteres en vez de una lista, en cuyo caso la variable "i" recorrerá cada caracter:

for i in "HOLAMUNDO":
    print(f"¡Dame una {i}!")
print ("¡HOLA MUNDO!")

#Siempre que sea posible, debemos utilizar la función range(). De hecho, es la única manera de recorrer elementos int.
for i in range(10):
    print(i)
print("\nFinal")

#CONTADOR EN BUCLE FOR
#Se trata de una variable creada específicamente para llevar la cuenta del número de veces que se 
#ha cumplido una condición. Pongamos un pequeño programa de ejemplo:
    
cuenta = 0  #----> Nuestra variable contador
for i in range(1,6): #--> Si no marcamos el 1, nos cuenta el 0.
    if i%2 == 0:
        cuenta += 1
        print(f"{i} es un número par.")
print(f"Desde el 1 hasta el 6 hay {cuenta} números pares.")

#En este caso el contador se modifica cada vez que se cumple la condición del if.
#Debe haber una variable externa al bucle y declarada antes que actúe como contador.

#ACUMULADOR EN BUCLE FOR
#Es una variable que acumula el resultado de una operación. Pongamos un ejemplo:

suma = 0
for i in range (1,6):
    suma = suma + i
print(f"La suma de los números de 1 a 5 es {suma}")

#El acumulador se modifica en cada ciclo completo del for.
#Debe haber una variable externa al bucle y declarada antes que actúe como acumulador.


#ANIDAMIENTOS CON BUCLE FOR
#Un anidamiento es un bucle for metido dentro de otro bucle for, y puede haber varios niveles de anidamiento.
#Es recomendable que las variables ("i") de los bucles anidados no coincidan para evitar ambiguedades.

#Hay de dos tipos, variables independientes y variables dependientes:
    #Las variables son INDEPENDIENTES cuando los valores que toma la variable del bucle interno no dependen
    #del valor de la variable de control del bucle externo. Por ejemplo:
        
for i in [0,1,2]: 
    for j in [0,1]:
        print(f"La i vale {i} y la j vale {j}.") #-> El bucle externo se ejecuta tres veces.
                                                 #-> El bucle interno se ejecuta dos veces por cada vez que se
                                                    #ejecuta el bucle externo.
                                                    
    #Siempre que sea posible, se recomienda utilizar el range() para este tipo de bucles.
    #Tenemos que prestar atención al sangrado de las líneas para indicar a qué bloque demos cada instrucción que demos.
    #La costumbre más extendida es llamar "i" a la variable del bucle externo y "j" a la del bucle interno.
    
    #Las variables son DEPENDIENTES cuando los valores que toma la variable de control interno
    #dependen del valor de la variable de control externo. Por ejemplo:
        
for i in [1,2,3]:
    for j in range(i):
        print(f"La i vale {i} y la j vale {j}") #-> Por cada movimiento de i en la lista, j recorrerá la lista desde
                                                #-> el principio hasta la posición en la que se encuentre i en ese ciclo
                                                
                                            
#_____________________________________________________________________________________________________________________
#BUCLE WHILE
#El bucle while permite repetir la ejecución de un conjunto de instrucciones mientras se cumpla una condición (sea true)
#Su sintaxis es de la siguiente manera:
 
       #while condición:
           #cuerpo del bucle    
           
#Dentro de un bucle while, se evalúa la condición. Si el resultado es true, se ejecuta la instrucción, y se vuelve a
#evaluar y a ejecutar hasta que el resultado sea false. Si nunca sucede esto, hablamos de un bucle infinito.
#El bucle while también posee variables de control, pero hay que declararlas antes del bucle y modificarlas dentro.
#Por ejemplo

i = 0  #-> Nuestra variable de control, un contador.
while i <= 10:
    print(i)
    i += 1 #->Realizamos un incremento al contador para que el bucle acabe en algún momento.
print("Fin del programa")

#Los bucles while se pueden utilizar, por ejemplo, para pedir un input hasta que el usuario lo haga correctamente.
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")

#Debemos tener cuidado con los bucles infinitos. Normalmente se dan porque las condiciones del bucle no son las
#mejor requeridas. Para cortar un bucle infinito en consola, podemos pulsar el botón stop o el comando "Ctrl + C"