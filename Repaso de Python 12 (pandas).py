# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:40:51 2021

@author: david
"""

#PANDAS
#Pandas es una librería de python destinada al análisis de datos.
#Proporciona una estructura de datos flexibles, y permite trabajar con ellos de forma muy eficiente.
#Dentro de los Pandas podemos encontrar las siguientes estructuras de datos:
        #SERIES: Son arrays unidimensionales con indexacion (índices etiquetados). Se pueden generar a partir de dicccionarios o de listas.
        #DATAFRAME: Son estructuras de datos similares a las tablas de bases de datos relacionales (como SQL).
        #PANEL, PANEL4D Y PANELND: Permiten trabajar con estructueras en más dimensiones. Son complejos y no los vamos a ver.
#Para operar con Pandas, debemos instalar las librerías Pandas y numpy (desde la consola de comandos)        

#Antes de operar con Pandas, lo primero que debemos hacer es importar su librería.

import pandas as pd


#SERIES 
#Vamos a definir una serie. Para definir una serie, tenemos que utilizar la siguiente sintaxis:
    
           #serie = pd.Series(data,index=index)
           
#En el primer parámetro, "data", le indicaremos los datos del array.
#En el segundo parámetro, "=index", introduciremos los datos que cumplirán la función de índice.

#Vamos a crear una serie con los datos de la alineación de la selección española de futbol del mundial de 2010.

seleccion_española = pd.Series(
    ["Casillas", "Ramos", "Piqué", "Puyol", "Capdevila", "Xabi Alonso", "Busquets", "Xavi Hernández", "Pedrito", "Iniesta", "Villa"],
    index = [1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7])

print("Spanish Football Players: \n%s" % seleccion_española) #-> Con esto le metemos un título a la serie.

#Si no indicasemos los índices, por defecto se aplicarían índices desde el 0 hasta el rango que tenga la lista de datos.

#También podemos construir una serie a partir de un diccionario. Si la creamos a partir de un diccionario, los índices por defecto serán
#las claves:
    
diccionario_seleccion_española = {1: "Casillas", 15: "Ramos", 3: "Piqué", 5: "Puyol", 11: "Capdevila", 14: "Xabi Alonso", 16: "Busquets", 8: "Xavi Hernández", 18: "Pedrito", 6: "Iniesta", 7: "Villa"}
seleccion2_española = pd.Series(diccionario_seleccion_española)

print("Spanish Football Players (diccionario): \n%s" % seleccion2_española)


#DATAFRAMES
#Un DataFrame es una estructura de datos similar a las tablas de base de datos relacionales, y se pueden hacer muchas operaciones conm ellos,
#como por ejemplo consultas.
#Podemos construir un DataFrame a partir de una lista, un diccionario, una serie o de otro DataFrame...
#Vamos a crear un DataFrame con los integrantes de la selección española de futbol:
    
seleccion_españolaDF = pd.DataFrame(
    {"nombre" : ["Casillas", "Ramos", "Piqué", "Puyol", "Capdevila", "Xabi Alonso","Busquets", "Xavi Hernandez", "Pedrito", "Iniesta", "Villa"],
     "posición": ["Portero", "Defensa derecho", "Defensa central", "Defensa central", "Defensa izquierdo", "Defensa mediocentro", "Defensa mediocentro", "Mediocentro", "Lateral izquierdo", "Lateral derecho", "Delantero centro"],
     "equipo": ["Real Madrid", "Real Madrid", "FC Barcelona", "FC Barcelona", "Villareal", "Real Madrid", "FC Barcelona", "FC Barcelona", "FC Barcelona", "FC Barcelona", "FC Barcelona"]
     }, columns = ["nombre", "posición", "equipo"],
    index = [1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7])

#Como se puede apreciar, el DataFrame se ha creado a partir de un diccionario que indica el nombre, la posición y el equipo de cada jugador.
#Debemos indicar también las columnas que queremos que tenga, así como el índice.

#Podemos insertar un  nuevo elemento en el DataFrame, a través del método loc():
seleccion_españolaDF.loc[10] = ["Cesc", "Delantero", "Arsenal"] #-> Le indicamos el índice y los valores que debe tomar en las columnas.