# =================================# =================================
# Inmaculada Perea Fernández
# =================================# =================================

# ejercicios-02-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 2: Introducción a Python
# ====================================================================


# PARA CASA: 5, 7, 8, 9, 10 (APARTADO 2), 13



# -----------
# EJERCICIO 5
# -----------
#
# 
# Antiguamente, cuando las impresoras eran matriciales y se compartían en un
# centro de trabajo, era normal que cada trabajo de impresión llevara una
# portada con dígitos de gran tamaño que indicaba el número del trabajo de
# impresión. Estos dígitos estaban dibujados mediante algún carácter simple. 

# Por ejemplo, lo que sigue es el número 0123456789 dibujado con asteriscos:

#   ***    *   ***   ***     *   *****  ***  *****  ***   ****  
#  *   *  **  *   * *   *   **   *     *         * *   * *   *
# *     *  *  *  *      *  * *   *     *        *  *   * *   *
# *     *  *    *     **  *  *    ***  ****    *    ***   ****
# *     *  *   *        * ******     * *   *  *    *   *     *
#  *   *   *  *     *   *    *   *   * *   * *     *   *     *
#   ***   *** *****  ***     *    ***   ***  *      ***      *

# Definir una función dígitos_grandes(x) que recibiendo un número entero
# positivo, lo escriba por pantalla usando dígitos grandes. Por ejemplo:


# >>> dígitos_grandes(8)
#   *** 
#  *   *
#  *   *
#   *** 
#  *   *
#  *   *
#   *** 
# >>> dígitos_grandes(4)
#     *  
#    **  
#   * *  
#  *  *  
#  ******
#     *  
#     *  

# INDICACIÓN:

# Puede ser de utilidad tener definidas las siguientes listas, que almacenan
# las distintas líneas que sirven para dibujar cada dígito grande:
 
cero = ["  ***  ", 
        " *   * ", 
        "*     *", 
        "*     *", 
        "*     *", 
        " *   * ", 
        "  ***  "]

uno = [" * ", 
       "** ", 
       " * ", 
       " * ", 
       " * ", 
       " * ", 
       "***"]

dos = [" *** ", 
       "*   *", 
       "*  * ", 
       "  *  ", 
       " *   ", 
       "*    ", 
       "*****"]

tres = [" *** ", 
        "*   *", 
        "    *", 
        "  ** ", 
        "    *", 
        "*   *", 
        " *** "]

cuatro = ["   *  ", 
          "  **  ", 
          " * *  ", 
          "*  *  ", 
          "******", 
          "   *  ", 
          "   *  "]

cinco = ["*****", 
         "*    ", 
         "*    ", 
         " *** ", 
         "    *", 
         "*   *", 
         " *** "]

seis = [" *** ", 
        "*    ", 
        "*    ", 
        "**** ", 
        "*   *", 
        "*   *", 
        " *** "]

siete = ["*****", 
         "    *", 
         "   * ", 
         "  *  ", 
         " *   ", 
         "*    ", 
         "*    "]

ocho = [" *** ", 
        "*   *", 
        "*   *", 
        " *** ", 
        "*   *", 
        "*   *", 
        " *** "]

nueve = [" ****", 
         "*   *", 
         "*   *", 
         " ****", 
         "    *", 
         "    *", 
         "    *"]


# ---------------------------------------------------------------------------

def digitos_grandes(n):
    s=str(n)
    numeros = {"0":cero, "1":uno, "2":dos, "3":tres, "4":cuatro, "5":cinco, "6":seis, "7":siete, "8":ocho, "9":nueve}
    for i in range(0,7):
        result =""
        for c in s:
            result+=numeros[c][i] + "  "
        print(result)




# -----------
# EJERCICIO 7
# -----------


# Definir la siguiente función usando comprensión. Dadas dos listas de la
# misma longitud, devolver un diccionario que tiene como claves las posiciones
# en las que coinciden los elementos de ambas listas, y como valor de esas
# claves, el elemento coincidente.

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}


def dic_posiciones_coincidentes(l, m):
    return({i:x for i, x in enumerate(l) for j, y in enumerate(m) if i==j and x==y})


def dic_posiciones_coincidentes_opcion2(l, m):
    return({i:x for (i,x), (j,y) in zip (enumerate(l), enumerate(m)) if i==j and x==y})
    
    
# -----------
# EJERCICIO 8
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros 
# entre 0 y 50. 
# Definir una función histograma_horizontal(d), que recibiendo un diccionario 
# de ese tipo, escribe un histograma de barras horizontales asociado, 
# como se ilustra en el siguiente ejemplo:  

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------


def histograma_horizontal(d):
    for a in sorted(d):
        result=a+":  "
        for _ in range(d[a]):
            result+="*"
        print(result)





# ------------
# EJERCICIO 9
# ------------
# Con la misma entrada que el ejercicio anterior, definir una función
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical. 

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *         
#           *         
#           *         
#           *         
#           *         
#         * * *       
#         * * *       
#         * * *       
#       * * * *       
#       * * * *       
#       * * * *       
#     * * * * * *     
#     * * * * * *     
#   * * * * * * * *   
#   * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * * * 
# * * * * * * * * * * 
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------


def histograma_vertical(d):
    line_number=max(d.values())
    pline=""
    while line_number>0:
        for k in sorted(d):
            if(d[k]>=line_number):
                pline+="* "
            else:
                pline+="  "
        print(pline)
        line_number-=1
        pline=""
    # contenido de la ultima fila
    for letter in sorted(d):
        pline+=letter + " "
    print(pline)








# ------------
# EJERCICIO 10
# ------------
#
# 
# Supongamos que tenemos almacenada, usando diccionario, la información sobre
# el grupo de los alumnos de un curso. Para ello, usamos como clave el nombre
# de los alumnos de un grupo y como valor el grupo que tienen asignado. 





# 2) Definir una función nuevo_alumno(dict_n,dict_g,nombre,grupo) tal que
# supuesto que dict_n y dict_g son dos variables conteniendo respectivamente
# el grupo de cada alumno y los alumnos de cada grupo, introduce un nuevo
# alumno con su nombre y grupo, modificando adecuadamente tanto dict_n como
# dict_g. Si el alumno ya está en los diccionarios, modificar el dato
# existente (en ese caso, si además el grupo que se quiere asignar no coincide
# que el que ya tiene se mostrará un mensaje de advertencia). Si se asigna un
# grupo que no está dado de alta, la correspondiente entrada se debe añadir al
# diccionario de grupos.

# Ejemplos:

# >>> nuevo_alumno(alum,grupos,"Bernardo","G3")
# Nog actualizado. El alumno Bernardo ya está dado de alta en el grupo G3
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G3'}
# >>> nuevo_alumno(alum,grupos,"Bernardo","G1")
# El alumno Bernardo ya está dado de alta. Se cambia al grupo G1
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G3': ['Rocío'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín', 'Bernardo']}
# >>> nuevo_alumno(alum,grupos,"Ana","G3")
# Nuevo alumno Ana. Incluido en el grupo G3
# >>> nuevo_alumno(alum,grupos,"Juan","G4")
# El alumno Juan ya está dado de alta. Se cambia al grupo G4
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G4', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G4': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Joaquín', 'Bernardo']}
# --------------------------------------------------------------------------

# grupo	nombre
#   0	        0
#   0	        1
#   1	        0
#   1	        1



def nuevo_alumno(dict_n,dict_g,nombre,grupo):
    # No existe grupo ni alumno
    if(grupo not in dict_g and nombre not in dict_n): 
        dict_g[grupo]=[nombre]
        dict_n[nombre]=grupo
        print("Nuevo alumno " + nombre + " asignado al grupo " + grupo)
    
    # No existe grupo, si existe el alumno
    elif (grupo not in dict_g and nombre in dict_n):
        dict_g[dict_n[nombre]].remove(nombre)
        dict_g[grupo]=[nombre]
        dict_n[nombre]=grupo
        print("El alumno " + nombre + " se cambia al grupo " + grupo)
    
    # Exite grupo, no exixte alumno
    elif (grupo in dict_g and nombre not in dict_n):         
        dict_g[grupo].append(nombre)
        dict_n[nombre]=grupo
        print("Nuevo alumno " + nombre + " asignado al grupo " + grupo)
    
    # Existe grupo y alumno
    elif (grupo in dict_g and nombre in dict_n):
        # El alumno está asignado ya al grupo de entrada
        if(dict_n[nombre]==grupo):
            print("El alumno " + nombre + " ya pertenece al grupo " + grupo)
        # El alumno esta asignado a un grupo distinto de entrada
        else:
            dict_g[dict_n[nombre]].remove(nombre)
            dict_g[grupo].append(nombre)
            dict_n[nombre]=grupo
            print("El alumno " + nombre + " se cambia al grupo " + grupo)
        





# ------------
# EJERCICIO 13
# ------------
#
# 
# Definir la función mezcla(l1,l2) que recibe como argumentos dos listas
# numéricas ordenadas de menor a mayor y devuelve la mezcla ordenada de dichas
# listas.  Por ejemplo: 

# >>> mezcla([3,7,8,11,13],[1,4,9,10])
# [1, 3, 4, 7, 8, 9, 10, 11, 13]
# --------------------------------------------------------------------

def mezcla(l,m):
    result=[]
    for x in l:
        if(x not in result):
            result.append(x)
    for y in m:
        if (y not in result):
            result.append(y)
    return(sorted(result))


