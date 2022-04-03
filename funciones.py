''' 
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del
curso (convocatoria ordinaria).
Escribir un programa que contenga las siguientes funciones:
'''
'''
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y 
añada a cada diccionario un nuevo par con la nota final del curso. 
El peso de cada parcial de teoría en la nota final es de un 
30% mientras que el peso del examen de prácticas es de un 40%.
'''

import csv
#import sys  sys.getdefaultencoding() nos dice en que formato está
import operator
lista = []
'''
Primer función que devuelve una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y 
la asistencia de un alumno
'''
def informacion(lista): 
    with open ('calificaciones.csv') as file:
        leer = csv.DictReader(file, delimiter = ';') #delimiter, para indicar los separadores
        #leer es un objeto de la clase DictReader
        ordenar = sorted (leer, key=operator.itemgetter('Apellidos')) #ordenamos en función de los apellidos
        for i in ordenar:
            lista.append(i)
        
        return lista

informacion(lista)
# separamos en diccionarios
for x in range(len(lista)):
    print(lista[x])
