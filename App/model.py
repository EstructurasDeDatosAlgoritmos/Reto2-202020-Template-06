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
               "companies":None}
    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['companies'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareCompaniesByName)
    catalog['moviesIds'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    return catalog


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
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
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

def getFirstAndLastDetails(catalog):
    lista_movies = catalog['movies']
    
    first = lt.firstElement(lista_movies)
    last = lt.lastElement(lista_movies)
    
    #Titulo
    f_name = first["original_title"]
    l_name = last["original_title"]
    
    #Fecha
    f_date = first["release_date"]
    l_date = last["release_date"]
    #Average
    f_average = first["vote_average"]
    l_average = last["vote_average"]
    #Count
    f_count = first["vote_count"]
    l_count = last["vote_count"]
    #Promedio
    f_promedio = float(f_average) / int(f_count)
    l_promedio = float(l_average) / int(l_count)
    #Language
    f_language = first["spoken_languages"]
    l_language = last["spoken_languages"]
    First = "\n" +"Primera pelicula:\n" + "Titulo:" + str(f_name) + "\n" + "Fecha:" + str(f_date) + "\n" + "Promedio:" + str(f_average) + "\n" + "Numero de votos:" + str(f_count) + "\n" + "Idioma:" + str(f_language) + "\n\n"
    Last = "\n" +"Ultima pelicula:\n" + "Titulo:" + str(l_name) + "\n" + "Fecha:" + str(l_date) + "\n" + "Promedio:" + str(l_average) + "\n" + "Numero de votos:" + str(l_count) + "\n" + "Idioma:" + str(l_language) + "\n\n"
    Details = First + Last
    return Details  

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

