''' 
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del
curso (convocatoria ordinaria).
Escribir un programa que contenga las siguientes funciones:

Una función que reciba el fichero de calificaciones 
y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y 
la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
'''
import csv
import sys  #sys.getdefaultencoding() nos dice en que formato está
lista = []
'''
Primer función que devuelve una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y 
la asistencia de un alumno
'''
def informacion(lista): 
    with open ('calificaciones.csv') as file:
        leer = csv.DictReader(file, delimiter = ';') #delimiter, para indicar los separadores
        #leer es un objeto de la clase DictReader
        '''for i in leer:
            print(i['Apellidos'])'''
        for i in leer:
            lista.append(i)
        print(lista)
    return lista

informacion(lista)
print(lista)