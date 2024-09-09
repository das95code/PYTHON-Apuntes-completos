# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:36:11 2021

@author: david
"""

#En este apartado vamos a ver algunas de las funcionalidades que nos aporta Pandas para trabajar con DataFrame's.
#Para todos los ejemplos isguientes vamos a utilizar el sistema de valoración y recomendación de MovieLens, que contiene información de 
#películas, usuarios y sus votos.

#(descargar datos de MovieLens para 100k de usuarios)

#Con Pandas podemos leer los data set a partir de diferentes formatos (txt, csv, json, sql, html....)
#Cada formato tiene sus parámetros de lectura.
#Nosotros usaremos el genérico, "pd.read_table():

        #pd.read_table(dir_fichero, engine="python", sep=";", header=True|False, names=[lista con nombre columnas])
        
        #Siendo:
            #dir_fichero: fichero a leer
            #engine : (en nuestro caso, siempre python)
            #sep: el separador que queremos utilizar
            #header: ¿tiene cabecera? (nombre de columas)
            #names: en caso de que no tenga cabecera, pasarle a names el nombre de las columnas deseadas.
            
#Sabiendo esto, vamos a leer los datos descargados de MovieLens:

import pandas as pd
#tabla = pd.read_table("d:/usuarios/Users/DavidAlcázarSánchez/Documents/ml-latest-small/ml-latest-small/links.csv", engine="python", sep=",")
#Como el header es verdadero (la tabla tiene header), no ponemos ni header ni name.


#MERGEO DE DATAFRAMES:
#Con pandas podemos mergear datos siempre y cuando sea posible. Es como el Join de base de datos. 
#Podemos ver un ejemplo de forma muy intuitiva con el data set de MovieLens que descargamos previamente.
#Vamos a mergear los fichers "movies" y "ratings" a partir del "movie_id":
    
movies = pd.read_table("C:/Users/david/Documents/ml-latest-small/ml-latest-small/movies.csv", engine="python",sep=",")

ratings = pd.read_table("C:/Users/david/Documents/ml-latest-small/ml-latest-small/ratings.csv", engine="python",sep=",")

#Unimos las tables por el campo en común "movies_id"
merger_rating_movies = pd.merge(movies, ratings)

#Podemos mergear también la tabla links:

links = pd.read_table("C:/Users/david/Documents/ml-latest-small/ml-latest-small/links.csv", engine="python", sep=",")

merger_ratingmovieslinks = pd.merge(pd.merge(movies, ratings), links)


#¿Queremos ver, por ejemplo, la información de la posición 10000? Podemos hacerlo de la siguiente forma:
    
info10000 = merger_ratingmovieslinks.loc[10000]
print(info10000)


#GROUPBY
#Con groupby podremos agregar datos a nuestos dataframes, hacer operaciones en base a esas agregaciones como sumas, medias, desviaciones
#típicas, etc...
#Para operar con GroupBy es necesario importar la librería numpy.

import numpy as np

#Para ver un ejemplo de la operación GroupBy, vamos a unir primero las tres fuentes de datos (movies, ratings y links) y los vamos a agrupar
#por el título de la película (mediante un conteo del número de tuplas). Posteriormente haremos una ordenación de mayor a menor
#para ver las 10 más votadas. Lo haremos de la siguiente manera:
    
numberRatings = merger_ratingmovieslinks.copy()
numberRatings = numberRatings.groupby('title').size().sort_values(ascending=False)
print("Películas con más votos: \n%s" % numberRatings[:10]) 

#También podemos agrupar por título e identificador de la película, y en este caso calcularemos la media de los votos por película con el 
#método mean():
    
avgRatings = merger_ratingmovieslinks.copy()
avgRatings = avgRatings.groupby(["movieId", "title"]).mean()
print("Películas con la media de votos más alta: \n%s" % avgRatings[:10])

#En este caso hemos indicado que nos muestre el valor medio del campo "rating", pero al aplicar el método "mean()" en el DataFrame nos ha 
#calculado todas las medias de todas las columnas que tienen datos numéricos.


#Ahora seguiremos agrupando por título e identificador, pero además vamos a hacer varios cálculos simultáneos que le indicaremos con una 
#lista que le pasamos al método "agg()":
    
dataRatings = merger_ratingmovieslinks.copy()
dataRatings = dataRatings.groupby(["movieId", "title"])["rating"].agg(["mean", "sum", "count", "std"])
print("Datos del rating: \n%s" % dataRatings[:10])

#Al metodo "agg()" le podemos pasar también funciones declaradas por nosotros mismos, como en el siguiente caso en el que hacemos una función
#para calcular la media de los votos y, para comprobar que es correcto, indicamos también que nos calcule la media).

myAvg = merger_ratingmovieslinks.copy()
myAvg = myAvg.groupby(["movieId", "title"])["rating"].agg(SUM = np.sum, COUNT = np.size, AVG = np.mean, myAVG = lambda x: x.sum() / float(x.count()))
print("Media de votos: \n%s" % myAvg[:10])

#Por último vamos a agrupar por título e identificador y valmos a calcular el número de votos recibidos por película, calculamos
#la nota media y por último ordenamos las películas por el número de votos para poder ver la nota media de las películas más votadas:
    
sortRatingField = merger_ratingmovieslinks.copy()
sortRatingField = sortRatingField.groupby(["movieId", "title"])["rating"].agg(COUNT = np.size, myAVG = lambda x: x.sum()/ float(x.count())).sort_values("COUNT", ascending = False)
print("Mi informacion ordenada: \n%s" % sortRatingField[:15])

#np.size es una función para calcular el tamaño de una serie. 
#np.sum es una función para calcular el sumatorio total de una serie.
#la funcion DataFrame.std() calcula la desviación de columnas.