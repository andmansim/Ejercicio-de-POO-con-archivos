''' 
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del
curso (convocatoria ordinaria).
Escribir un programa que contenga las siguientes funciones:
'''
'''
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y 
devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, 
la nota de los exámenes parciales y de prácticas mayor o igual que 4 y 
la nota final mayor o igual que 5.
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

'''# separamos en diccionarios
for x in range(len(lista)):
    print(lista[x])'''

#función que añade a cada diccionario un nuevo par con la nota final del curso 
def ponderaciones(lista):
    for j in lista:
        p1 = j.get('Parcial1')
        p2 = j.get('Parcial2')
        practicas = j.get('Practicas')

        if j['Ordinario1'] == "":
            j['Ordinario1'] = '0.0'
        else: 
            j['Ordinario1'] = j['Ordinario1'].replace(',', '.')
        if j['Ordinario2'] == "":
            j['Ordinario2'] = '0.0'
        else:
            j['Ordinario2'] = j['Ordinario2'].replace(',', '.')
        if j['OrdinarioPracticas'] == "":
            j['OrdinarioPracticas'] = '0.0'
        else: 
            j['OrdinarioPracticas'] = j['OrdinarioPracticas'].replace(',', '.')
            
        if p1 == '' :
            j['Parcial1'] = '0.0'
            p1 = j['Ordinario1']
        else:
            p1 = p1.replace(',', '.')
            j['Parcial1'] = p1
            if float(p1) <= 4.0:
                p1 = j['Ordinario1']
        if p2 == '' :
            j['Parcial2'] = '0.0'
            p2 = j['Ordinario2']
        else:
            p2 = p2.replace(',', '.')
            j['Parcial2'] = p2
            if float(p2) <= 4.0:
                p2 = j['Ordinario2']
        if practicas == '':
            practicas = j['OrdinarioPracticas']
            j['Practicas'] = '0.0'
        else: 
            practicas = practicas.replace(',', '.')
            j['Practicas'] = practicas
            if float(practicas) <= 4.0:
                practicas = j['OrdinarioPracticas']
        

        
    
        
        j['Nota final'] = float(p1) * 0.3 + float(p2) * 0.3 + float(practicas) * 0.4
        

ponderaciones(lista)
# separamos en diccionarios
for x in range(len(lista)):
    print(lista[x])