# =================================# =================================
# Inmaculada Perea Fernández
# =================================# =================================

# ejercicios-03-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 3: Introducción a Python
# =================================

# Para casa ejercicios del 2, 3, 5, 6 para el día 10/11

# -----------
# EJERCICIO 2
# -----------


# Definir una función mi_grep(cadena,fichero) similar al comando grep de unix
# (sin uso de patrones). Es decir, escribe por pantalla las líneas de fichero
# en las que ocurre cadena (junto con el número de línea).

# Por ejemplo, si buscamos la cadena "función" en un fichero similar a éste,
# las prímeras líneas de la salida podrían ser similares a éstas: 


# >>> mi_grep("función","ejercicios-03-ipppd.py")
# Línea 12: # Definir una función codifica_descodifica(fichero1,fichero2) que codifique un
#                         ^^^^^^^
# Línea 32: # Indicación: La función chr(n) obtiene el carácter cuyo código
#                            ^^^^^^^
# Línea 33: # es el número "n". A la inversa, la función ord(c) devuelve el código del
#                                                ^^^^^^^
# Línea 47: # Definir una función mi_grep(cadena,fichero) similar al comando grep de unix
#                         ^^^^^^^
# ....
#  
#
# ---------------------------------------------------------------------------

def mi_grep(cadena,fichero):
    nlinea=0
    try:
        f=open(fichero, 'r', encoding='utf8')  
        for line in f:
            nlinea+=1
            if cadena in line:
                print("Línea {0}: {1}".format(nlinea, line))
        f.close()
    except:
        print("No es posible abrir el fichero " + fichero)
    


# -----------
# EJERCICIO 3
# -----------

# El método de búsqueda dicotómica de una raíz de una función en un intervalo
# (es decir, un valor donde la función se anula) consiste en:

# Supongamos que tenemos una función f definida en un intervalo [a,b] (tal que
# f(a) y f(b) tienen distinto signo) y un número épsilon (margen de error).
# Sea c=(a+b)/2.

# - Si b - a<épsilon, devolvemos c.

# - Si f(c)=0, c es la raíz buscada y devolvemos c.

# - Si f(a) y f(c) tienen distinto signo, repetir el proceso en el
#   intervalo [a,c].

# - Si f(b) y f(c) tienen distinto signo, repetir el proceso en el
#   intervalo [c,b].

# Definir un procedimiento DICOTOMIA que recibiendo como entrada una función f
# (con un argumento, numérico), y tres números a, b y épsilon tales que a<b, épsilon>0 y
# f(a) de distinto signo que f(b), busque una raíz de la función f en el
# intervalo [a,b] con un error máximo de épsilon.

# Ejemplos:
# Para obtener una aproximación de la raíz cuadrada de 2:
# >>> dicotomía(lambda x: (x**2)-2, 1, 3, 0.000000001)
# 1.4142135619185865
# Para obtener una aproximación del número pi:
# >>> import math
# >>> dicotomía(math.sin, 2, 5, 0.000000001)
# 3.141592653817497
# ------------------------------------------------------------------------------

def dicotomía(f, a, b, e):
    c=(a+b)/2
    if b-a < e:
        return c
    elif(f(c)==0):
        return c
    elif (f(a)>0 and f(c)<0) or (f(a)<0 and f(c)>0):
        return (dicotomía(f, a, c, e))
    elif (f(b)>0 and f(c)<0) or (f(b)<0 and f(c)>0):
        return (dicotomía(f, c, b, e))
        
    

# -----------
# EJERCICIO 5
# -----------


# (J. Zelle) Supongamos que queremos simular la trayectoria de un proyectil
# que se dispara en un punto dado a una determinada altura inicial. El disparo
# se realiza hacia adelante con una velocidad inicial y con un determinado
# ángulo. Inicialmente el proyectial avanzará subiendo pero por la fuerza de
# la gravedad en un momento dado empezará a bajar hasta que aterrice. Por
# simplificar, supondremos que no existe rozamiento ni resistencia del viento.

# Diseñar una clase Proyectil que sirva representar el estado del proyectil en
# un instante de tiempo dado. Para ello, necsitamos al menos los siguientes
# atributos de datos:
# - Distancia recorrida (en horizontal)
# - Altura
# - Velocidad horizontal
# - Velocidad vertical

# Además, incluir los siguientes tres métodos:
# - actualiza(t): actualiza la posición y la velocidad del proyectil tras t
#   segundos
# - obtén_posx(): devuelve la distancia horizontal recorrida 
# - obtén_posy(): devuelve la distancia vertical recorrida 

# Una vez definida la clase Proyectil, usarla para definir una función 
#    aterriza(altura, velocidad, ángulo, intervalo)
# que imprimirá por pantalla las distintas posiciones por las que pasa un
# proyectil que se ha disparado con una velocidad, un ángulo (en grados) 
# y una áltura inicial dada. Se mostrará la posición del proyectil 
# en cada intervalo de tiempo, hasta que aterriza.
# Además se mostrará la altura máxima que ha alcanzado, cuántos intervalos de
# tiempo ha tardado en aterrizar y el alcance que ha tenido 

# Indicaciones:

# - Si el proyectil tiene una velocidad inicial v y se lanza con un ángulo
#   theta, las componentes horizontal y vertical de la velocidad inicial son
#   v*cos(theta) y v*sen(theta), respectivamente.
# - La componente horizontal de la velocidad, en ausencia de rozamiento 
#   y viento, podemos suponer que permanece constante.
# - La componente vertical de la velocidad cambia de la siguiente manera
#   tras un instante t: si vy0 es la velocidad vertical al inicio del
#   intervalo, entonces al final del intervalo tiene una velocidad 
#   vy1=vy0-9.8*t, debido a la gravedad de la tierra.
# - En ese caso, si el proyectil se encuentra a una altura h0, tras un
#   intervalo t de tiempo se encontrará a una altura h1=h0 + vm*t, donde vm es la
#   media entre las anteriores vy0 y vy1. 

# Ejemplo:

# >>> aterriza(30,45,20,0.01)
# Proyectil en posición(0.0,30.0)
# Proyectil en posición(0.4,30.2)
# Proyectil en posición(0.8,30.3)
# Proyectil en posición(1.3,30.5)
# Proyectil en posición(1.7,30.6)
# Proyectil en posición(2.1,30.8)
# Proyectil en posición(2.5,30.9)
#           ·······
# ·······SALIDA OMITIDA ·······
#           ·······
# Proyectil en posición(187.3,2.0)
# Proyectil en posición(187.8,1.7)
# Proyectil en posición(188.2,1.5)
# Proyectil en posición(188.6,1.2)
# Proyectil en posición(189.0,0.9)
# Proyectil en posición(189.4,0.6)
# Proyectil en posición(189.9,0.3)
# Proyectil en posición(190.3,0.0)

# Tras 451 intervalos de 0.01 segundos (4.51 segundos) el proyectil ha aterrizado.
# Ha recorrido una distancia de 190.7 metros
# Ha alcanzado una altura máxima de 42.1 metros
# -----------------------------------------------------------------------------

import math

def seno(grados):
    return math.sin(math.radians(grados))
    
def coseno(grados):
    return math.cos(math.radians(grados))

class Proyectil (object):
    def __init__(self, h0, theta, v0):
        self.h0=h0
        self.theta=theta
        self.v0=v0
        self.hmax=h0
        self.altura=h0
        self.distancia_recorrida=0.0
        self.velocidad_horizontal=v0*coseno(theta) # Constante, no hay rozamiento
        self.velocidad_vertical=v0*seno(theta)
             

    def __repr__(self):
        return ("(x= {}, y={})".format(self.distancia_recorrida, self.altura))
        

    def __str__(self):
        return ("(x= {}, y={})".format(self.distancia_recorrida, self.altura))
    
    # Actualiza la posición y la velocidad del proyectil tras t segundos
    def actualiza(self, t):
        Vy0=self.velocidad_vertical   # velocidad vertical al inicio del intervalo
        self.velocidad_vertical-= 9.8*t 
        Vm=(Vy0+self.velocidad_vertical)/2.0   # media de las velocidades del intervalo
        self.altura+=Vm*t
        self.distancia_recorrida+=self.velocidad_horizontal*t
        if self.altura>self.hmax:
            self.hmax=self.altura
    
    # Devuelve la distancia horizontal recorrida
    def obtén_posx(self):
        return round(self.distancia_recorrida,1)
        
    # Devuelve la distancia vertical recorrida
    def obtén_posy(self):
        return round(self.altura,1)
  
    # Devuelve la altura máxima alcanzada
    def obtén_hmax(self):
        return round(self.hmax,1)

def aterriza(altura, velocidad, angulo, intervalo):
    n_intervalos=0
    new_proyectil=Proyectil(altura, angulo, velocidad)
    while new_proyectil.obtén_posy()>=0:
        print("Proyectil en posición({0}, {1})".format(new_proyectil.obtén_posx(), new_proyectil.obtén_posy()))
        new_proyectil.actualiza(intervalo)
        n_intervalos+=1
    print("\n\nTras {0} intervalos de {1} segundos ({2} segundos) el proyectil ha aterrizado.".format(n_intervalos, intervalo, n_intervalos*intervalo))
    print("Ha recorrido una distancia de {0} metros".format(new_proyectil.obtén_posx()))
    print("Ha alcanzado una altura máxima de {0} metros".format(new_proyectil.obtén_hmax()))
        



# -----------
# EJERCICIO 6
# -----------

# Apartado 6.1
# ------------

# Supongamos que queremos gestionar los alumnos de una titulación, con las
# asignaturas en las que están matriculados, y las notas que tienen. Para
# ello, se pide implementar una clase Alumno, con las siguintes
# características: 

# - El constructor de la clase recibe como argumentos el nombre del alumno y
#   una lista de las asignaturas que matricula inicialmente (sin nota). Por
#   simplificar, supondremos que el nombre es un string con un nombre de pila
#   y dos apellidos, y que la asignatura viene dada por sus siglas. Se supone
#   que ni el nombre de pila ni los apellidos son compuestos.

# - El nombre debe ser un atributo de datos de la clase. Además, incluir cualquier 
#   atributo que pudiera ser necesario para mantener la información sobre las 
#   asignaturas en las que está matriculado el alumno, y la nota, si la tuviera 
#   (si aún no tiene nota de una asignatura, asignar el valor "-")

# - Los métodos de la clase son los siguientes:
#    * Método __repr__, que devuelve simplemente el nombre del alumno
#    * Método pon_nota, que recibe una asignatura y una nota, y anota
#      al alumno la nota de esa asignatura. Si el alumno no está matriculado
#      en esa asignatura, el método debe devolver la excepción 
#      AsignaturaNoMatriculada, que se define más abajo.
#    * Método consulta_nota, que recibe una asignatura y devuelve la nota que
#      ese alumno tiene en la asigntura. Si el alumno no está matriculado
#      en esa asignatura, el método debe devolver la excepción 
#      AsignaturaNoMatriculada, que se define así:
#         class AsignaturaNoMatriculada(Exception):
#             pass
#    * Método añade_asignatura que recibe una asignatura, y añade esa
#      asignatura al alumno. Si la asignatura ya la tiene el alumno, no hacer
#      nada.
#    * Método asignaturas_matriculadas, que devuelve la lista de asignaturas
#      matriculadas del alumno
#    * Método media_expediente, que recibiendo el plan de estudios del alumno,
#      devuelve la nota media del alumno (ponderada por número de créditos de
#      cada asignatura). El plan de estudios es un diccionario cuyas claves
#      son todas las asignaturas, y el valor asociado a cada clave es el
#      número de creditos de la asignatura (ver ejemplo más abajo). Si una
#      asignatura no está matriculada o evaluada, se considera que está
#      puntuada con un cero.


# Ejemplos:

# >>> alumno1=Alumno("Antonio Ruiz Santos", ["DGPDS1","DGPDS2","IPPPD","FEST","AEM","APCD"])

# >>> alumno1.nombre
# 'Antonio Ruiz Santos'

# >>> alumno1 # Aquí se llamaría al método __repr__
# Antonio Ruiz Santos

# >>> alumno1.consulta_nota("IPPPD")
# '-'

# >>> alumno1.pon_nota("IPPPD",8.9)

# >>> alumno1.consulta_nota("IPPPD")
# 8.9

# >>> alumno1.consulta_nota("ML1")
# Traceback (most recent call last):

#   File "<ipython-input-41-33cce032017f>", line 1, in <module>
#     alumno1.consulta_nota("ML1")

#   File ".......", line 26, in consulta_nota
#     raise AsignaturaNoMatriculada("Asignatura no matriculada para este alumno")

# AsignaturaNoMatriculada: Asignatura no matriculada para este alumno

# >>> alumno1.añade_asignatura("ML1")

# >>> alumno1.consulta_nota("ML1")
# '-'

# >>> alumno1.pon_nota("ML1",6.3)

# >>> alumno1.consulta_nota("ML1")
# 6.3

# >>> alumno1.asignaturas_matriculadas()
# ['APCD', 'DGPDS1', 'ML1', 'IPPPD', 'DGPDS2', 'AEM', 'FEST']

plan_de_estudios_MDS={"DGPDS1":3,"DGPDS2":6,"IPPPD":4,"FEST":4,"AEM":6,"APCD":4,
                   "APBD":5,"ML1":5,"ML2":5,"TMO":4,"ICSR":3,"MDTE":3,"DSBI":3,
                   "PLNCD1":2,"PLNCD2":2,"VD":2,"VI":2,"TFM":6} 

# >>> alumno1.media_expediente(plan_de_estudios_MDS)
# 0.9724637681159419

# ------------------------------------------------------------

class AsignaturaNoMatriculada(Exception):
    pass

class Alumno (object):
    def __init__(self, nombre, asignaturas):
        self.nombre = nombre
        self.dictasig={x:"-" for x in asignaturas}

    def __repr__(self):
        return self.nombre
        
    def __eq__(self, otro):
        return (self.nombre == otro.nombre)

    def __str__(self):
        return self.nombre
    
    def asignaturas_matriculadas(self):
        return list(self.dictasig.keys())
        
    def pon_nota(self, asignatura, nota):
        if asignatura in self.dictasig:
            self.dictasig[asignatura]=nota
        else:
            raise AsignaturaNoMatriculada("Asignatura no matriculada para el alumno " + self.nombre)

    def añade_asignatura(self, asignatura):
        if asignatura not in self.dictasig:
            self.dictasig[asignatura]="-"
                 
    def consulta_nota(self, asignatura):
        if asignatura in self.dictasig:
            return self.dictasig[asignatura]
        else:
            raise AsignaturaNoMatriculada("Asignatura no matriculada para el alumno " + self.nombre)
       
    def media_expediente(self, plan_de_estudios):
        nota=0
        sum_cred=sum(list(plan_de_estudios.values()))
        for asig in plan_de_estudios:
            if ((asig in self.dictasig) and (self.dictasig[asig]!='-')):
                nota+=plan_de_estudios[asig]*self.dictasig[asig]
        return nota/sum_cred
            
    




# Apartado 6.2
# ------------


# Supongamos que tenemos un archivo de texto en los que cada línea corresponde
# a un alumno con sus asignaturas y notas, con el siguiente formato:

# NOMBRE APELLIDO1 APELLIDO2 A1 N1 A2 N2 .... An Nn

# Por ejemplo, podríamos tener un archivo alumno_notas.txt con las siguientes
# líneas:

# Juan Pérez Quirós DGPDS1 7.4 DGPDS2 8.4 IPPPD 9.1 FEST 7.5 AEM 6.2 APCD 8.2 APBD 5.3 ML1 8.8 ML2 7.5 TMO 8.7 ICSR 6.1 MDTE 7.3 DSBI 10.0 PLNCD1 5.0 PLNCD2 6.2 VD 6.4 VI 7.1 TFM 8.5
# María González Peña DGPDS1 5.4 DGPDS2 9.3 IPPPD 8.7 FEST 7.6 APCD 9.2 APBD 6.6 ML1 .8 ML2 7.7 TMO 5.2 MDTE 5.3 DSBI 8.2 PLNCD1 6.0 PLNCD2 9.2 VD 6.4 VI 7.1 
# Pedro Moncada Escobar DGPDS1 6.4 IPPPD 9.5 FEST 7.8 AEM 5.2 APCD 7.2 APBD 5.8 ML1 8.8 TMO 7.2 ICSR 8.8 DSBI 5.0 PLNCD1 7.0 VD 8.4 VI 6.1 
# Salvador Gutiérrez Sánchez DGPDS1 7.7 DGPDS2 8.0 IPPPD 7.3 FEST 7.9 AEM 8.2 APCD 8.6 APBD 5.3 TMO 5.2 ICSR 8.1 MDTE 5.3 PLNCD1 5.3 PLNCD2 7.5 VD 8.4
# Rocío Cotán Sánchez DGPDS2 8.2 FEST 7.1 APCD 6.2 ML1 5.8 ML2 7.9 TMO 5.2 ICSR 9.1 MDTE 6.3 DSBI 6.6 PLNCD1 5.6 PLNCD2 6.5 VI 6.1 TFM 9.5
# Gabriel Mejías Cifuentes DGPDS1 6.9 DGPDS2 7.3 IPPPD 9.0 FEST 6.5 AEM 6.5 APBD 5.7 ML1 7.8 ICSR 8.1 MDTE 5.3 PLNCD1 5.1 PLNCD2 8.0 
# Josefa Cabrera León DGPDS1 7.4 DGPDS2 8.4 IPPPD 9.1 FEST 7.5 

# Por simplificar, ni los nombres de pila ni los apellidos serán compuestos.

# Se pide definir una función lee_notas(archivo), que recibiendo el nombre del
# archivo, devuelva una lista de objetos de la clase Alumno, cada uno
# conteniendo toda la información de la correspondiente línea del archivo de
# texto. 

# Ejemplo:

# >>> lista_alumnos=lee_notas("alumno_notas.txt")

# >>> lista_alumnos
# [Juan Pérez Quirós,
#  María González Peña,
#  Pedro Moncada Escobar,
#  Salvador Gutiérrez Sánchez,
#  Rocío Cotán Sánchez,
#  Gabriel Mejías Cifuentes,
#  Josefa Cabrera León]

# >>> lista_alumnos[2].nombre
# 'Pedro Moncada Escobar'

# >>> lista_alumnos[2].consulta_nota("APCD")
# 7.2

# >>> lista_alumnos[2].consulta_nota("DSBI")
# 5.0

# >>> lista_alumnos[2].consulta_nota("TFM")
# Traceback (most recent call last):

#   File "<ipython-input-56-b068fc897dbd>", line 1, in <module>
#     lista_alumnos[2].consulta_nota("TFM")

#   File "......", line 26, in consulta_nota
#     raise AsignaturaNoMatriculada("Asignatura no matriculada para este alumno")

# AsignaturaNoMatriculada: Asignatura no matriculada para este alumno


# >>> lista_alumnos[3].asignaturas_matriculadas() 
# ['DGPDS1',
#  'PLNCD2',
#  'PLNCD1',
#  'ICSR',
#  'IPPPD',
#  'DGPDS2',
#  'AEM',
#  'VD',
#  'TMO',
#  'APCD',
#  'APBD',
#  'MDTE',
#  'FEST']

# ------------------------------------------------------------



def lee_notas(archivo):
    l_alumn=[]
    try:
        f=open(archivo, 'r')
        for line in f:
            nombre= ' '.join(line.split(' ')[0:3])
            info=line.split(' ')[3:]
            new_alumno=Alumno(nombre,[])
            i=0
            while i+1<len(info):
                new_alumno.añade_asignatura(info[i])
                new_alumno.pon_nota(info[i], float(info[i+1]))
                i+=2
            l_alumn.append(new_alumno)  
        f.close()
    except:
        print("Error al procesar el fichero " + archivo)
        
    return l_alumn







# Apartado 6.3
# ------------

# Definir una función mejor_expediente(lista_alumnos, plan_de_estudiso), que
# recibiendo como entrada:
#  - Una lista lista_de_alumnos de objetos de la clase Alumno
#  - Un diccionario plan_de_estudios, que asigna a cada asignatura del plan de
#    estudios su número de créditos. 
# devuelve el objeto de la clase Alumno (o lista de objetos, si hay más de uno), con la mejor
# nota media

# Ejemplo:

# >>> mejor_expediente(lista_alumnos,plan_de_estudios_MDS)
# Juan Pérez Quirós

# ------------------------------------------------------------

def mejor_expediente(lista_alumnos, plan_de_estudios):
    result=[]
    for alumn in lista_alumnos:
        if len(result)==0:
            result.append(alumn)
        elif (alumn.media_expediente(plan_de_estudios) > result[0].media_expediente(plan_de_estudios)):
            result.clear()
            result.append(alumn)
        elif(alumn.media_expediente(plan_de_estudios) == result[0].media_expediente(plan_de_estudios)):
            result.append(alumn)
    return result

        
        
