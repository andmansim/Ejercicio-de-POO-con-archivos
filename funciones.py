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
with open ('calificaciones.csv', a = " ") as file:
    leer = csv.read([file])
    lista = list(leer)
print(lista)
