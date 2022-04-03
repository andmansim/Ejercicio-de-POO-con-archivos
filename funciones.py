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
    
def ponderaciones(lista):
    for j in lista:
        p1 = j.get('Parcial1')
        p2 = j.get('Parcial2')
        practicas = j.get('Practicas')
        if p1 == '' or p2 == '' or practicas == '':
            p1 = 0
            p2 = 0
            practicas = 0
        c1 = ',' in p1
        c2 = ',' in p2
        c = ',' in practicas
        if c1 == True or c2 == True or c == True:
            c1.replace(',', '.')
            c2.replace(',', '.')
            c.replace(',', '.')
        j['Nota final'] = float(p1) * 0.3 + float(p2) * 0.3 + float(practicas) * 0.4
        print(j)

ponderaciones(lista)