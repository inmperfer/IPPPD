#*************************************************************************
# Inmaculada Perea Fernández
#
#*************************************************************************
# -*- coding: utf-8 -*-
# Ejercicios de repaso de NumPy
# - Siguen la misma estructura que los ejemplos de código que tenemos
# disponibles en las transparencias.
# - Las soluciones se pueden enviar usando este mismo archivo, ya que es un
# archivo python listo para ser ejecutado en nuestro entorno.
# - Os recuerdo mi correo para cualquier duda y para el envío de las
# soluciones:
# gmunoz4@us.es

# Importación de la librería numpy
import numpy as np

##
# Ejercicio 1
##
# a) Crea un objeto ndarray con números del 0 al 9. El tipo de los datos es
# tipo entero de 32 de bits (int32).
arr1 = np.arange(10, dtype=np.int32)

# b) Una vez tenemos nuestro ndarray, le cambiamos el tipo a float64.
arr1 = arr1.astype(np.float64)

# c) Ahora, necesitamos crear un ndarray con todos sus elementos igual a 1 del
# mismo tamaño que el array creado anteriormente.
arr2 = np.ones((arr1.shape), dtype=arr1.dtype)

# d) La última operación es sumar los arrays creados.
arr1 + arr2




##
# Ejercicio 2
##
# a) Creamos un objeto ndarray con números del 0 al 20. El tipo de los datos
# es tipo float64.
arr3 = np.arange(21, dtype=np.float64)

# b) Necesitamos aplicar las siguientes funciones unarias a nuestro array:
#   - Calcular la raíz cuadrada de cada elemento
np.sqrt(arr3)

#   - Calcular el cuadrado de cada elemento
arr3**2

#   - Preguntaremos si los elementos de nuestro array son números o no
np.isnan(arr3)

# c) Necesitamos aplicar las siguientes funciones binarias a nuestro array.
# Para ello crearemos otro objeto ndarray con sus elementos igual a 1 y del
# mismo tamaño que el anterior:
arr4 = np.ones(arr3.shape, dtype=arr3.dtype)

#   - Sumaremos los elementos de ambos arrays
arr3 + arr4

#   - Multiplicaremos los elementos de ambos arrays
arr3 * arr4

#   - Sumaremos uno al array con todos sus elementos igual a 1.
sum_one = 1 + arr4

#   - Elevaremos los elementos del primer array a los elementos de este nuevo
#     array.
arr3 ** sum_one





##
# Ejercicio 3
##
# a) Creamos un objeto ndarray con números del 0 al 10. El tipo de los datos
# es tipo float64.
arr5 = np.arange(11, dtype=np.float64)

# b) Calcularemos la media de los elementos de nuestro array de dos maneras:
#    - Usando el método que nos ofrece nuestro array
arr5.mean(dtype=np.float64)

#    - Usando el método que nos ofrece la librería numpy
np.mean(arr5, dtype=np.float64)

# c) Calcularemos ahora la suma acumulada de todos los elementos de nuestro
# array.
np.cumsum(arr5)

# d) Crearemos a continuación un array con los valores:
values = ['Python', 'R', 'datos', 'R', 'ciencia', 'libreria', 'Python']

#   - Aplicar una función para eliminar elementos duplicados
values=np.unique(values) # las devuelve ordenadas por orden alfabético
values


#   - Comprobar si los elementos de nuestro array existen en este otro array:
new_values = ['Python', 'R']

np.in1d(values, new_values)





##
# Ejercicio 4
##
# a) En este ejercicio trabajaremos con las distintas formas de indexación que
# numpy nos ofrece. Comenzamos creando un array con elementos del 0 al 8.
arr6 = np.arange(9)


# b) Mostraremos el valor del elemento en la posición 3. Seguidamente
# modificaremos los valores desde la posición 4 a la 6 con el valor 20.
arr6[3]
arr6[4:7]=20


# c) Modificamos nuestro array para que sea una matriz 3 x 3. Mostramos los
# valores accediendo a la segunda fila y hasta la segunda columna.
arr6 = arr6.reshape(3,3)



# d) En este apartado haremos uso del array:
science = np.array(['Python', 'R', 'datos', 'R', 'ciencia', 'libreria', 'Python', 'Python', 'R'])

# Mostramos los valores de nuestro array que en 'values' son igual a 'Python'.
# El array a usar debe ser el del apartado a).
np.arange(9)[np.where(science == 'Python')[0]]

