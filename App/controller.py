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
    t1_start = process_time()
    loadDetails(catalog, Detailsfile)
    loadCasting(catalog, Castingfile)
    t1_stop = process_time()
    print ("Tiempo de ejecución: ",t1_stop-t1_start, " segundos.")
    
def loadDetails(catalog, Detailsfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    moviesfile = cf.data_dir + Detailsfile
    input_file = csv.DictReader(open(Detailsfile, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        model.addMovie(catalog, movie)
        companies = movie['production_companies'].split(",")  # Se obtienen los autores
        for company in companies:
            model.addMovieCompany(catalog, company.strip(), movie)
        

def loadCasting(catalog, Castingfile):
    pass

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
    Retorna los libros de un autor
    """
    companyinfo = model.getMoviesByCompany(catalog, company_name)
    return companyinfo
