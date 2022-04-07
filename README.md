# Ejercicio-de-POO-con-archivos

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Ejercicio-de-POO-con-archivos.git)
https://github.com/andmansim/Ejercicio-de-POO-con-archivos.git

He resuelto un ejercicio, el cual, consistía en manejar datos de un fichero csv y hacer una serie de funciones con ellos.

```
import funciones

if __name__ == '__main__':
    lista = []
    aprobados = []  
    suspensos = []
    
    funciones.informacion(lista)
    funciones.ponderaciones(lista)
    funciones.aprobado(lista, aprobados, suspensos )

    print("Notas de los estudiantes:")
    
    #separamos en diccionarios
    for x in range(len(lista)):
        print(lista[x])
        
    print("La lista de aprobados es la siguiente:")
    print(aprobados)
    print("La lista de suspensos es la siguiente:")
    print(suspensos)
```
