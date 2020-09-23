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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
from time import process_time 
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

Castingfile = 'Data/MoviesCastingRaw-small.csv'
Detailsfile = 'Data/SmallMoviesDetailsCleaned.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printCompanyData(company):
    """
    Imprime los libros de un autor determinado
    """
    if company:
        print('Compañia encontrado: ' + company_name['name'])
        print('Promedio: ' + str(company['average_rating']))
        print('Total de peliculas: ' + str(lt.size(company['movies'])))
        iterator = it.newIterator(company['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro la compañia')

def printDirectorData(director):
    """
    Imprime las peliculas de un director determinado
    """
    if director:
        print('director encontrado: ' + director['name'])
        print('Promedio: ' + str(director['average_rating']))
        print('Total de peliculas: ' + str(lt.size(director['movies'])))
        iterator = it.newIterator(director['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro el director')

def printCountryData(country):
    """
    Imprime las peliculas de un director determinado
    """
    if country:
        print('pais encontrado: ' + country['name'])
        print('Promedio: ' + str(country['average_rating']))
        print('Total de peliculas: ' + str(lt.size(country['movies'])))
        iterator = it.newIterator(country['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title']+"año de produccion: "+movie['release_date'])
            print("Director: "+movie["director_name"]\n)
    else:
        print('No se encontro el director')

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar Datos")
    print("3- Descubrir productoras de cine")
    print("4- Conocer a un director")
    print("5- Conocer a un actor ")
    print("6- Entender un género cinematográfico")
    print("7-  Encontrar películas por país")
    print("0- Salir")


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        lista_unida=controller.loadData(cont, Detailsfile, Castingfile)
        controller.funciones(cont,lista_unida)
        print('Peliculas cargadas: ' + str(controller.moviesSize(cont)))
        #print("Detalles de la primera y ultima pelicula: \n" + controller.firstANDlast_details(cont))
           

    elif int(inputs[0]) == 3:
        t1_start = process_time() #Inicio de cronometro
        company_name=input("ingrese el nombre de la productora: \n")
        company_info=controller.getMoviesByCompany(cont,company_name)
        printCompanyData(company_info)

    elif int(inputs[0]) == 4:
        director_name=input("ingrese el nombre del director que desea conocer:\n")
        director_info=controller.getMoviesByDirector(cont,director_name)
        printDirectorData(director_info)
 

    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        country_name=input("ingrese el nombre del pais que desea conocer:\n ")
        country_info=controller.getMoviesByCountry(cont,country_name)
        printCountryData(country_info)
    else:
        print ("Muchas gracias. ")
        sys.exit(0)
sys.exit(0)
