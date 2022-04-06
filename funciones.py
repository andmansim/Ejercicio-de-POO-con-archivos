import csv
#import sys  sys.getdefaultencoding() nos dice en que formato está
import operator

lista = []


#Primer función que devuelve una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y 
#la asistencia de un alumno
def informacion(lista): 
    with open ('calificaciones.csv') as file:
        leer = csv.DictReader(file, delimiter = ';') #delimiter, para indicar los separadores
        #leer es un objeto de la clase DictReader
        ordenar = sorted (leer, key=operator.itemgetter('Apellidos')) #ordenamos en función de los apellidos
        for i in ordenar:
            lista.append(i)
        
        return lista

informacion(lista)

#función que añade a cada diccionario un nuevo par con la nota final del curso 
def ponderaciones(lista):
    for j in lista:
        p1 = j.get('Parcial1')
        p2 = j.get('Parcial2')
        practicas = j.get('Practicas')
        
        #trasformamos espacio en blanco y cambiamos comas por puntos
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
        
        #trasformamos espacio en blanco y cambiamos comas por puntos  
        if p1 == '' :
            j['Parcial1'] = '0.0'
            p1 = j['Parcial1']
        else:
            p1 = p1.replace(',', '.')
            j['Parcial1'] = p1
            
        if p2 == '' :
            j['Parcial2'] = '0.0'
            p2 = j['Parcial2']
        else:
            p2 = p2.replace(',', '.')
            j['Parcial2'] = p2
            
        if practicas == '':
            j['Practicas'] = '0.0'
            practicas = j['Practicas']
        else: 
            practicas = practicas.replace(',', '.')
            j['Practicas'] = practicas
        #calculamos la nota con la ponderación
        j['Nota final'] = float(p1) * 0.3 + float(p2) * 0.3 + float(practicas) * 0.4

ponderaciones(lista)
aprobados = []  
suspensos = []
#Tercera función que devuelve una lista con los aprobados y los suspensos     
def aprobado(lista, aprobados, suspensos):
    for p in lista:
        asistencia = p['Asistencia']
        #añadimos a las listas suspensos o aprobados
        if asistencia < '75%' and asistencia != '100%':
            suspensos.append(p['Nombre'] + ' ' + p['Apellidos'])
        else:
            if p['Nota final'] >= 5.0:
                aprobados.append(p['Nombre'] + ' ' + p['Apellidos'])
            else:
                o1 =  p['Ordinario1']
                o2 =  p['Ordinario2']
                o = p['OrdinarioPracticas']
                nota_f_ordinaria = float(o1) * 0.3 + float(o2) * 0.3 + float(o) * 0.4
                if nota_f_ordinaria >= 5.0:
                    aprobados.append(p['Nombre'] + ' ' + p['Apellidos'])
                else:
                    suspensos.append(p['Nombre'] + ' ' + p['Apellidos'])
    return aprobados, suspensos

aprobado(lista, aprobados, suspensos )

# separamos en diccionarios
for x in range(len(lista)):
    print(lista[x])
    
print("La lista de aprobados es la siguiente:")
print(aprobados)
print("La lista de suspensos es la siguiente:")
print(suspensos)