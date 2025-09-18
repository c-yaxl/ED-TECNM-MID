import numpy as np
import random
#Creamos un diccionario para almacenar los registros de los estudiantes
registros = {}
n=1
#Inicializamos una matriz vacía para almacenar las calificaciones
matriz_final = np.array([])
#Generamos las calificaciones aleatorias
for i in range(2000):
    #Asignamos un ID único a cada estudiante
    id = n+i
    #Inicializamos una lista vacía para almacenar las calificaciones del estudiante
    registros[id] = []
    print(f"ID de Estudiante: {id}")
    #Generamos las calificaciones aleatorias
    for i in range(6):
        calificacion = random.uniform(5.0, 10.0)
        registros[id].append(calificacion)
        fila = np.array([calificacion])
        if matriz_final.size == 0:
            matriz_final = np.array([fila])
        else:
            matriz_final = np.vstack([matriz_final, fila])
        print(fila)
print(matriz_final)

#Buscamos la calificación de un estudiante por su ID y materia
id_buscar = int(input("Ingrese el ID del estudiante a buscar: "))
materia = int(input("Ingrese la materia del estudiante a buscar calificacion: "))
#Verificamos si el ID existe en los registros
if id_buscar in registros:
    #Buscamos la calificación de la materia
    print(f"La calificacion es de: {registros[id_buscar][materia-1]}")
else:
    print("Estudiante no encontrado.")
        