"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
from time import process_time 
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it



"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    t1_start = process_time()
    catalog = model.newCatalog()
    t1_stop = process_time()
    print ("Tiempo de ejecución ",t1_stop-t1_start, " segundos.")
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, Detailsfile, Castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    list_unida=lt.newList("ARRAY_LIST",None)
    list_details=loadDetails(catalog, Detailsfile)
    list_casting=loadCasting(catalog, Castingfile)
    it1=it.newIterator(list_details)
    while it.hasNext(it1):
        movie=it.next(it1)
        model.addMovie(catalog,movie)
        it2=it.newIterator(list_casting)
        while it.hasNext(it2):
            peli=it.next(it2)
            if movie["id"]==peli["id"]:
                union={**movie,**peli}
                lt.addLast(list_unida,union)
                break
    return list_unida

def funciones(catalog,lista_unida):
    it1=it.newIterator(lista_unida)
    while it.hasNext(it1):
        movie=it.next(it1)
        model.addMovie(catalog,movie)
        companies=movie["production_companies"].split(",")
        for company in companies:
            model.addMovieCompany(catalog,company,movie)
        model.addMovieDirector(catalog,movie["director_name"],movie)

        model.addMovieActor(catalog,movie["actor1_name"],movie)
        model.addMovieActor(catalog,movie["actor2_name"],movie)
        model.addMovieActor(catalog,movie["actor3_name"],movie)
        model.addMovieActor(catalog,movie["actor4_name"],movie)
        model.addMovieActor(catalog,movie["actor5_name"],movie)
        #model.directoresDEactores(catalog)
        model.addMovieGenres(catalog,movie["genres"], movie)
        model.addMovieCountry(catalog,movie["production_countries"],movie)



def loadDetails(catalog, Detailsfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    list_Details=lt.newList("ARRAY_LIST",None)
    #Detailsfile = cf.data_dir + Detailsfile
    input_file = csv.DictReader(open(Detailsfile, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        lt.addLast(list_Details,movie)

    return list_Details
        

def loadCasting(catalog, Castingfile):
    list_Casting=lt.newList("ARRAY_LIST",None)
    #Castingfile = cf.data_dir + Castingfile
    input_file = csv.DictReader(open(Castingfile, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        lt.addLast(list_Casting,movie)
    return list_Casting
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def moviesSize(catalog):
    """Numero de peliculas leidas
    """
    return model.moviesSize(catalog)

def firstANDlast_details(catalog):
    """Detalles de la primera y ultima pelicula 
    """
    return model.getFirstAndLastDetails(catalog)

def getMoviesByCompany(catalog, company_name):
    """
    Retorna las peliculas de una compañia
    """
    companyinfo = model.getMoviesByCompany(catalog, company_name)
    return companyinfo

def getMoviesByDirector(catalog, director_name):
    """
    Retorna las peliculas de un director
    """
    directorinfo = model.getMoviesByDirector(catalog, director_name)
    return directorinfo
def getMoviesByCountry(catalog, country_name):
    """
    Retorna las peliculas de un pais
    """
    countryinfo = model.getMoviesByCountry(catalog, country_name)
    return countryinfo

def getMoviesByGenres(catalog, genres_name):
    genreinfo = model.getMoviesByGenres(catalog, genres_name)
    return genreinfo

def getMoviesByActor(catalog, actor_name):
    """
    Retorna las peliculas de un director
    """
    actorinfo = model.getMoviesByActor(catalog, actor_name)
    return actorinfo
"""
def getDir_Act(catalog):

    return model.getDir_Act(catalog)
"""

