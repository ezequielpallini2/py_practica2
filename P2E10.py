#Importo el módulo string para poder trabajar con el string de nombres
import string

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


#Creo una lista por comprensión a partir del string "Nombres", guardando en esa lista solo los elementos 
# que contengan caracteres coherentes para la información que queremos procesar y dejando todos los nombres con el mismo formato
nombres_lista = [nombre.title() for nombre in nombres.strip().split("'") if all(letra.isalnum() for letra in nombre) and nombre != ""]

#Creo un diccionario por comprensión guardando ambas notas de las alumnos en una lista, y a su vez asignando esa lista a el nombre 
#utilizando el metodo enumerate()
diccionario = {nombre : [notas_1[i], notas_2[i]] for i, nombre in enumerate(nombres_lista)}
print("Alumos y notas: ")
for alumno in diccionario: 
    print(alumno, ":", diccionario[alumno])

#Creo otro diccionario por comprensión para almacenar los promedios, utilizando también el método enumerate
promedios = {nombre : ((notas_1[i] + notas_2[i]) / 2) for i, nombre in enumerate(nombres_lista)}
for promedio in promedios: 
    print(promedio, ":",  promedios[promedio])

#Calculo el promedio general, dividiendo la suma de los valores de mi diccionario "promedios" por la cantidad de elementos de éste. 
promedio_general = sum(promedios.values()) / len(promedios)
print("El promedio general del curso es:", round(promedio_general,2))

#Busco al estudiante con mejor promedio, utilizando la función max sobre mi diccionario de promedios.
clave_max, valor_max = max(promedios.items(), key=lambda x: x[1])
print('El estudiante con mayor promedio es:', clave_max)

#Busco al estudiante con la peor nota, aplicando una función lambda que devuelva el mínimo de cada alumno
#Y así poder encontrar el mínimo general y a que clave pertenece.
clave_min, valor_min = min(diccionario.items(), key=lambda x: min(x[1]))
print('El estudiante con menor nota es:', clave_min)
