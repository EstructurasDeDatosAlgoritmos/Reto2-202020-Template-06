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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de peliculas
    Crea una lista vacia para guardar todos los libros
    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion
    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'moviesIds': None,
               "companies":None,
               "director":None,
               "genres": None,
               "countries": None}
    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['companies'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.7,
                                   comparefunction=compareCompaniesByName)
    catalog['directors'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    catalog['countries'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareCountriesByName)
    catalog['genres'] = mp.newMap(200,
                                maptype = 'PROBING',
                                loadfactor = 0.4,
                                comparefunction = compareGenresByName)
    
    catalog['moviesIds'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.7,
                                   comparefunction=compareMapMoviesIds)
    return catalog

# requisito 1

def newProduction_company(name):
    """
    Crea una nueva estructura para modelar las peliculas de una compañia
    y su promedio de ratings
    """
    company = {'name': "", "movies": None,  "average_rating": 0}    
    company['name'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareMapMoviesIds)
    return company

def addMovieCompany(catalog, company_name, movie):
    """
    Esta función adiciona una pelicula a la lista de peliculas publicadas
    por una compañia.
    Cuando se adiciona la pelicula se actualiza el promedio de dicha compañia
    """
    companies = catalog['companies']
    existauthor = mp.contains(companies, company_name)
    if existauthor:
        entry = mp.get(companies, company_name)
        company = me.getValue(entry)
    else:
        company = newProduction_company(company_name)
        mp.put(companies, company_name, company)
    lt.addLast(company['movies'], movie)

    company_avg = company['average_rating']
    movie_avg = movie['vote_average']
    if (company_avg == 0.0):
        company['average_rating'] = float(movie_avg)
    else:
        company['average_rating'] = (company_avg + float(movie_avg)) / 2


# requisito 2

def newDirector(name):
    """
    Crea una nueva estructura para modelar las peliculas de una compañia
    y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "average_rating": 0}    
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKED', compareMapMoviesIds)
    return director

def addMovieDirector(catalog, director_name, movie):
    """
    Esta función adiciona una pelicula a la lista de peliculas publicados
    por un director.
    Cuando se adiciona la pelicula se actualiza el promedio de dicho director
    """
    directors = catalog['directors']
    existauthor = mp.contains(directors, director_name)
    if existauthor:
        entry = mp.get(directors, director_name)
        director = me.getValue(entry)
    else:
        director = newDirector(director_name)
        mp.put(directors, director_name, director)
    lt.addLast(director['movies'], movie)

    director_avg = director['average_rating']
    movie_avg=movie["vote_average"]
    if (director_avg == 0.0):
        director['average_rating'] = float(movie_avg)
    else:
        director['average_rating'] = (director_avg + float(movie_avg)) / 2
#requisito 6
def newGenres(name):
    genres = {'name': "", 'movies': None, "average_count": 0}
    genres['name'] = name
    genres['movies'] = lt.newList('SINGLE_LINKED', compareMapMoviesIds)
    return genres

def addMovieGenres(catalog, genres_name, movie):
    genre = catalog['genres']
    existgenre = mp.contains(genre, genres_name)
    if existgenre:
        entry = mp.get(genre, genres_name)
        genres = me.getValue(entry)
    else:
        genres =newGenres(genres_name)
        mp.put(genre, genres_name, genres)
    lt.addLast(genres['movies'], movie)

    genre_cou = genres['average_count']
    movie_avg = movie['vote_count']
    if (genre_cou == 0.0):
        genres['average_count'] = float(movie_avg)
    else:
        genres['average_count'] = (genre_cou + float(movie_avg))/2

#requisito 5
def newCountry(name):
    """
    Crea una nueva estructura para modelar las peliculas de un pais
    y su promedio de ratings
    """
    country = {'name': "", "movies": None,  "average_rating": 0}    
    country['name'] = name
    country['movies'] = lt.newList('SINGLE_LINKED', compareMapMoviesIds)
    return country

def addMovieCountry(catalog, country_name, movie):
    """
    Esta función adiciona una pelicula a la lista de peliculas publicados
    por un director.
    Cuando se adiciona la pelicula se actualiza el promedio de dicho director
    """
    countries = catalog['countries']
    existcountry = mp.contains(countries, country_name)
    if existcountry:
        entry = mp.get(countries, country_name)
        country = me.getValue(entry)
    else:
        country = newCountry(country_name)
        mp.put(countries, country_name, country)
    lt.addLast(country['movies'], movie)

    country_avg = country['average_rating']
    movie_avg=movie["vote_average"]
    if (country_avg == 0.0):
        country['average_rating'] = float(movie_avg)
    else:
        country['average_rating'] = (country_avg + float(movie_avg)) / 2




# Funciones para agregar informacion al catalogo
def addMovie(catalog, Movie):
    """
    Esta funcion adiciona una pelicula a la lista de peliculas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['movies'], Movie)
    
    mp.put(catalog['moviesIds'], Movie["id"], Movie)


# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])

def getMoviesByCompany(catalog, company_name):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    company = mp.get(catalog['companies'], company_name)
    if company:
        return me.getValue(company)
    return None

def getMoviesByDirector(catalog, director_name):
    """
    Retorna un director con sus libropeliculass a partir del nombre del director
    """
    director = mp.get(catalog['directors'], director_name)
    if director:
        return me.getValue(director)
    return None

def getMoviesByGenres(catalog, genres_name):
    genre = mp.get(catalog['genres'], genres_name)
    if genre:
        return me.getValue(genre)
    return None

def getMoviesByCountry(catalog, country_name):
    """
    Retorna un pais con sus peliculas a partir del nombre del pais
    """
    country = mp.get(catalog['countries'], country_name)
    if country:
        return me.getValue(country)
    return None
# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareCompaniesByName(keyname, company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    comentry = me.getKey(company)
    if (keyname == comentry):
        return 0
    elif (keyname > comentry):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    dicentry = me.getKey(director)
    if (keyname == dicentry):
        return 0
    elif (keyname > dicentry):
        return 1
    else:
        return -1

def compareGenresByName(keyname, genres):
    gentry = me.getKey(genres)
    if (keyname == gentry):
        return 0
    elif (keyname > gentry):
        return 1
    else:
        return -1

def compareCountriesByName(keyname, country):
    """
    Compara dos nombres de paises. El primero es una cadena
    y el segundo un entry de un map
    """
    counentry = me.getKey(country)
    if (keyname == counentry):
        return 0
    elif (keyname > counentry):
        return 1
    else:
        return -1
