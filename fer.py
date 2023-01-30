# Ejercicio 1: Mostrar la versión actual de Python instalada.
import sys
print(sys.version)
print(sys.version_info)


# Ejercicio 2: Exponer el uso básico de la función print.
print('Este es un ejemplo básico.')
print('Este es un ejemplo básico.', end='')
print('Este es un ejemplo básico.', end='')
print()
print('Python', 'es', 'tremendo!')
print('Python', 'es', 'tremendo!', sep='-')
print()
print('{} es {}'.format('Python', 'tremendo!'))
print()
numeros = [2, 3, 5, 7, 11]
print(numeros)
print()
capitales = {'Colombia': 'Bogotá', 'Perú': 'Lima'}
print(capitales)


# Ejercicio 3: Obtener la fecha y hora actuales en el sistema.
import datetime
ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
print(ahora.strftime('%d/%m/%Y %H:%M:%S')) # format  day month year   hour min second


# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres.
# Python => nohtyP
cadena = 'Python'
for i in range(len(cadena) - 1, -1, -1):
    print(cadena[i], end='')
print()
print(cadena[::-1])


# Ejercicio 6: Obtener un conjunto de números separados por coma y crear una lista.
# 2, 8, 9, 0, 1, 8
entrada = input('Escriba varios números separados por coma: ')
print(entrada)
print(type(entrada))
numeros = entrada.split(',')
print(type(numeros))
print(numeros)


# Ejercicio 7: Obtener la extensión de un archivo especificado por el usuario.
nombre_archivo = input('Ingrese el nombre del archivo: ')
# main.py
partes_nombre_archivo = nombre_archivo.split('.')
print(partes_nombre_archivo)
print(partes_nombre_archivo[-1])


# Ejercicio 8: Obtener el primer y último de una lista.
lenguajes = ['Python', 'C#', 'PHP', 'Java', 'JavaScript']
# Primer elemento: Python
# Último elemento: JavaScript
primer_elemento = lenguajes[0]
# ultimo_elemento = lenguajes[len(lenguajes) - 1]
ultimo_elemento = lenguajes[-1]
print(primer_elemento)
print(ultimo_elemento)


# Ejercicio 9: Mostrar la fecha de un evento almacenada en una tupla.
fecha_evento = (2023, 9, 14)
print(type(fecha_evento))
print(fecha_evento)
print('El evento programado será para la fecha:', fecha_evento)
print('El evento programado será para la fecha: %i/%i/%i' % fecha_evento)
agnio, mes, dia = fecha_evento
print('El evento programado será para la fecha: {}/{}/{}'.format(agnio, mes, dia))


# Ejercicio 10: Solicitar al usuario un número n y calcular n + nn + nnn
# n = 3 => 3 + 33 + 333 = 369
n = input('Escriba el valor de n: ')
nn = int('{}{}'.format(n, n))
nnn = int('%s%s%s' % (n, n, n))
n = int(n)
suma = n + nn + nnn
print(suma)
# 2 + 22 + 222 = 246


# Ejercicio 11: Obtener la documentación de funciones incorporadas.
from math import sin
from datetime import datetime
print(abs.__doc__)
print('-' * 50)
print(int.__doc__)
print('-' * 50)
print(sin.__doc__)
print('-' * 50)
print(datetime.now.__doc__)


# Ejercicio 12: Imprimir el calendario para un año y mes específicos.
import calendar
agnio = int(input('Escriba el año: '))
mes = int(input('Escriba el mes: '))
print(calendar.month(agnio, mes))


# Ejercicio 13: Crear una cadena de caracteres multilínea.
cadena = """Phyton es un lenguaje de programación indispensable para cualquier informático o aprendiz de desarrollo web.
 Constituye una base sólida para quienes deseen formarse en el área, porque se trata de un lenguaje dinámico que se
 implementa en una variedad de plataformas, por lo cual permite crear no solo sitios sino aplicaiciones en una amplia
 variedad de sistemas operativos como iOS, Android, Windows o Mac. Te contamos qué es y para qué sirve Phyton 
 ofreciéndote sus principales características."""
print(cadena)
cadena = "Phyton es un lenguaje de programación indispensable para cualquier informático o aprendiz de desarrollo web. Constituye una base sólida para quienes deseen formarse en el área, porque se trata de un lenguaje dinámico que se implementa en una variedad de plataformas, por lo cual permite crear no solo sitios sino aplicaiciones en una amplia variedad de sistemas operativos como iOS, Android, Windows o Mac. Te contamos qué es y para qué sirve Phyton ofreciéndote sus principales características."
print()
print(cadena)


# Ejercicio 14: Calcular la diferencia en días de dos fechas dadas.
from datetime import date
hoy = date(2019, 9, 16)
otra_fecha = date(2023, 2, 13)
delta = otra_fecha - hoy
print(delta)
print(delta.days)


# Ejercicio 15: Calcular el volumen de una esfera a partir del radio dado.
from math import pi
r = float(input('Escriba el radio de la esfera: '))
volumen = 4/3 * pi * r ** 3
print('El volumen de la esfera es {} unidades cúbicas'.format(volumen))


# Ejercicio 16: Crear una función para evaluar un número y realizar una operación.
# fn(n): si n <= 15 => 15 - n; (15 - n) * 2
def diferencia(n):
    """
    Calcula la diferencia del valor pasado como argumento.
    Se deben seguir dos reglas.
    """
    if n <= 15:
        return 15 - n
    else:
        return (15 - n) * 2
print(diferencia(17))
print(diferencia(3))


# Ejercicio 17: Crear una función para determinar si un número es cercano a 1000 o 2000.
def cercania(n):
    """
    Comprueba si un número dado es cercano a 1000 ó 2000.
    """
    return (abs(1000 - n) < 100) or (abs(2000 - n) < 100)
print(cercania(1000))
print(cercania(950))
print(cercania(200))
print()
print(cercania(2000))
print(cercania(1950))
print(cercania(3200))
 
 
 # Ejercicio 18: Calcular la suma de tres números, e incluir una condición de igualdad.
def sumar_numeros(a, b, c):
    """
    Calcula la suma de tres números. Si los tres números son iguales, la suma 
    se multiplica por 3.
    """
    suma = a + b + c
    if a == b and a == c:
        suma *= 3
    return suma
print(sumar_numeros(2, 2, 7))
print(sumar_numeros(2, 2, 2))


# Ejercicio 19: Comprobar si una cadena termina con la extensión .py, sino es así, agregar la extensión.
# main.py
# modulo => modulo.py
def validar_nombre_archivo(nombre_archivo):
    """
    Valida si un nombre de archivo tiene la extensión .py.
    Si el archivo no tiene la extensión, la agrega.
    """
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == '.py':
        return nombre_archivo
    return nombre_archivo + '.py'
print(validar_nombre_archivo('main.py'))
print(validar_nombre_archivo('modulo'))


# Ejercicio 20: Emular el funcionamiento del producto de cadenas.
def producto_cadena(cadena, repeticion):
    """
    Emula el funcionamiento del producto (*) de cadenas.
    """
    resultado = ""
    for i in range(repeticion):
        resultado += cadena
    return resultado
print('Python' * 3)
print(producto_cadena('Python', 3))


# Ejercicio 21: Generar los n primeros números pares positivos.
# k mod 2 == 0 => k es par
def generar_numeros_pares(n = 100):
    """
    Genera los n primeros números pares positivos.
    """
    pares = []
    contador = 0
    numero = 0
    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1
    return pares
n = int(input('Escriba la cantidad de números pares positivos a generar: '))
if n > 0:
    pares = generar_numeros_pares(n)
    print(pares)
    print('Cantidad de pares:', len(pares))
else:
    print('El número debe ser positivo.')


# Ejercicio 22: Crear una subcadena de n caracteres replicada n cantidad de veces.
# 'Python', n = 2 => 'Py'; 'PyPy'
def replicar_subcadena(cadena, n):
    n_caracteres = n
    if n_caracteres > len(cadena):
        n_caracteres = len(cadena)
    subcadena = cadena[:n_caracteres]
    resultado = ''
    for i in range(n):
        resultado += subcadena
    return resultado
print(replicar_subcadena('Python', 2))
print(replicar_subcadena('Python', 10))


# Ejercicio 23: Comprobar si un carácter dado es una vocal.
# c = 'i', ['a', 'e', 'i', 'o', 'u'] => True
# c = 'z', ['a', 'e', 'i', 'o', 'u'] => False
def es_vocal(c):
    """
    Comprueba si un carácter es una vocal
    """
    if len(c) == 1:
        vocales = 'aeiou'
        c = c.lower()
        return c in vocales
    else:
        return False
print(es_vocal('i'))
print(es_vocal('I'))
print(es_vocal('z'))
print(es_vocal('ae'))


# Ejercicio 24: Simular el funcionamiento del operador in.
# print(5 in [2, 3, 5, 7, 11])
# print('k' in 'Fork')
# print('i' in 'Fork')
def pertenece_a(lista, elemento):
    """
    Comprueba si un elemento está disponible en una lista.
    """
    for e in lista:
        if elemento == e:
            return True
    return False
print(pertenece_a([2, 3, 5, 7, 11], 5))
print(pertenece_a([2, 3, 5, 7, 11], 19))
print(pertenece_a('Fork', 'k'))
print(pertenece_a('Fork', 'i'))
print()
print(pertenece_a(['F', 'o', 'r', 'k'], 'k'))
print(pertenece_a(['F', 'o', 'r', 'k'], 'i'))
 
 
 # Ejercicio 25: Crear un histograma a partir de una lista de enteros.
# Análisis
# [2, 1, 5, 3]
# **
# *
# *****
# ***
def crear_histograma(lista, caracter='*'):
    for e in lista:
        print(caracter * e)
lista = [2, 1, 5, 3]
crear_histograma(lista)
print()
lista = [2, 7, 13, 11, 19]
crear_histograma(lista)


# Ejercicio 26: Emular el funcionamiento de join para concatenar una lista.
# numeros = [2, 3, 5, 7, 11]
# 235711
# print(''.join([str(n) for n in numeros]))
def concatenar_lista(lista):
    resultado = ''
    for n in lista:
        resultado += str(n)
    return resultado
numeros = [2, 3, 5, 7, 11]
print(concatenar_lista(numeros))


# Ejercicio 27: Generar un conjunto de números aleatorios y determinar cuáles son impares.
# k mod 2 == 1
from random import randint
numeros_aleatorios = [randint(1, 100) for _ in range(50)]
print(numeros_aleatorios)
numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios)
print()
print(list(numeros_impares))
print()
def encontrar_impares(lista):
    impares = []
    for n in lista:
        if n % 2 == 1:
            impares.append(n)
    return impares
print(encontrar_impares(numeros_aleatorios))


# Ejercicio 28: Calcular la diferencia de conjuntos con colores.
colores_lista_1 = ['Negro', 'Rojo', 'Verde', 'Blanco']
colores_lista_2 = ['Blanco', 'Azul', 'Verde', 'Gris', 'Amarillo', 'Verde']
# A, B; A - B; A / B
colores_conjunto_1 = set(colores_lista_1)
colores_conjunto_2 = set(colores_lista_2)
diferencia = colores_conjunto_1.difference(colores_conjunto_2)
print(diferencia)


# Ejercicio 29: Calcular el área de un triángulo.
base = None
altura = None
while True:
    try:
        base = float(input('Escriba la base del triángulo: '))
        break
    except:
        print('Debe escribir un número.')
while True:
    try:
        altura = float(input('Escriba la altura del triángulo: '))
        break
    except:
        print('Debe escribir un número.')
area = base * altura / 2
print('El área del triángulo es igual: {}'.format(area))


# Ejercicio 30: Calcular el máximo común divisor de dos números.
# MCD: El número más grande que divide dos números.
def mcd(x, y):
    mcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd
print(mcd(8, 4))
print(mcd(13, 7))
print(mcd(29, 19))
print(mcd(17, 12))
print(mcd(4, 2))


# Ejercicio 31: Calcular el mínimo común múltiplo de dos números.
# MCM: Es el número positivo más pequeño que es múltiplo de dos números.
def mcm(x, y):
    z = max(x, y)
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1
print(mcm(2, 4))
print(mcm(32, 13))
print(mcm(17, 15))


# Ejercicio 32: Calcular la suma de tres números si todos son diferentes, en caso contrario la suma será 0.
def sumar(x, y, z):
    """
    Suma tres números. Si al menos dos números son iguales, la suma será 0.
    """
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z
print(sumar(2, 5, 3))
print(sumar(2, 5, 2))
print(sumar(5, 5, 2))
print(sumar(11, 7, 5))


# Ejercicio 33: Sumar dos números. Si la suma está entre 10 y 30, retornar 30.
def sumar(x, y):
    """
    Suma dos números. Si la suma se halla entre 10 y 30, se retorna 30.
    """
    suma = x + y
    if suma in range(10, 30 + 1):
        return 30
    else:
        return suma
print(sumar(7, 3))
print(sumar(7, 23))
print(sumar(12, 17))
print(sumar(23, 17))


# Ejercicio 34: Validar Dos Números. Si son iguales o la suma o el valor absoluto son 5.
def validar_numeros(x, y):
    """
    Evalúa dos números. Si son iguales o la suma o el valor absoluto son 5.
    """
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False
print(validar_numeros(3, 3))
print(validar_numeros(5, 7))
print(validar_numeros(16, 11))
print(validar_numeros(4, 1))


# Ejercicio 35: Crear una función únicamente para sumar números enteros.
def sumar(x, y):
    """
    Suma dos números. Valida que estos números sean enteros.
    """
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros.')
try:
    print(sumar(2, 3))
    print(sumar(2, '3'))
except TypeError as e:
    print(e)
    
    # Ejercicio 36: Crear una clase para representar los datos de una persona.
class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre, self.edad, self.correo)
edward = Persona('Edward', '33', 'edward@mail.co')
print(edward)


# Ejercicio 37: Crear una jerarquía de herencia básica.
# Persona <- Estudiante
class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera
german = Estudiante('123', 'Germán', 'german@mail.co', '987', 'Computación')
print(isinstance(german, Estudiante))
print(isinstance(german, Persona))


# Ejercicio 38: Resolver la expresión algebraica (x + y) * (x + y).
# (x + y) * (x + y) = x^2 + 2xy + y^2
# (2 + 3) * (2 + 3) = 5 * 5 = 25
def evaluar_expresion(x, y):
    """
    Resuelve la expresión algebraica (x + y) * (x + y).
    """
    return x**2 + 2 * x * y + y**2
x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))
print(evaluar_expresion(x, y))


# Ejercicio 39: Calcular el valor futuro para una cantidad, interés, y número de años específicos.
def valor_futuro(vp, i, n):
    """
    Calcula el valor futuro.
    """
    return vp * (1 + i) ** n
valor_presente = 10000
interes = 3.5
periodos = 7
print(valor_futuro(valor_presente,  interes/100, periodos))


# Ejercicio 40: Calcular la distancia entre dos puntos cartesianos.
# P1(x1, y1), P2(x2, y2)
from math import sqrt
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def calcular_distancia(p1, p2):
    """
    Calcula la distancia entre dos puntos.
    """
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
punto1 = Punto(3, 2)
punto2 = Punto(-3, -5)
print(calcular_distancia(punto1, punto2))


# Ejercicio 41: Comprobar si un archivo existe.
import os
nombre_archivo = 'archivo.txt'
print(os.path.isfile(nombre_archivo))


# Ejercicio 42: Encontrar la arquitectura computacional del shell.
import struct
print(struct.calcsize('P') * 8)


# Ejercicio 43: Encontrar el nombre del SO, el nombre y la versión de la plataforma.
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


# Ejercicio 44: Localizar la ruta de los site-packages de la instancia de Python.
import site
print(site.getsitepackages())


# Ejercicio 45: Ejecutar un comando externo por medio de la función call.
from subprocess import call
print(call(['ping', 'google.com']))


# Ejercicio 46: Encontrar la ruta del script actual en ejecución.
import os
print(os.path.realpath(__file__))


# Ejercicio 47: Averiguar la cantidad de CPUs disponibles en el sistema.
import multiprocessing
print(multiprocessing.cpu_count())


# Ejercicio 48: Convertir una cadena de caracteres a entero y real.
# int(), float()
cadena = '3.1415'
entero = int(cadena.split('.')[0])
print(entero)
real = float(cadena)
print(real)


# Ejercicio 49: Mostrar los archivos de un directorio específico.
from os import listdir
from os.path import isfile, join
ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'
def listar_directorio(ruta):
    """
    Lista el contenido de archivos de un directorio específico.
    """
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivos
listado_archivos = listar_directorio(ruta)
print(listado_archivos)
print(len(listado_archivos))


# Ejercicio 50: Modificar el comportamiento de impresión de la función print.
print('Python es tremendo', end='')
print()
for i in range(10):
    print('*', end='')
print()
print('Python', 'es', 'tremendo', sep='-')


# Ejercicio 51: Crear una tupla nombrada para representar un punto en el plano.
from collections import namedtuple
from math import sqrt
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
Punto = namedtuple('Punto', ['x', 'y'])
punto_1 = Punto(2, 3)
punto_2 = Punto(-3, -5)
print(punto_1)
print(punto_2)
def calcular_distancia(punto_1, punto_2):
    return sqrt((punto_1.x - punto_2.x)**2 + (punto_1.y - punto_2.y)**2)
print(calcular_distancia(punto_1, punto_2))


# Ejercicio 52: Imprimir en la salida estándar de errores.
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr)
eprint('Este es un mensaje de error')


# Ejercicio 53: Consultar las variables de entorno del sistema.
import os
print(os.environ['HOME'])
print('*' * 50)
print(os.environ['PATH'])
print('*' * 50)
print(os.environ)


# Ejercicio 54: Obtener el nombre de usuario actual.
import getpass
print(getpass.getuser())


# Ejercicio 55: Convertir un número binario en entero.
cadena = '1001'
entero = int(cadena, base=2)
print(entero)
# 1001 => 1*10^3 + 0*10^2 + 0*10^1 + 1*10^0 = 8 + 0 + 0 + 1 = 9


# Ejercicio 56: Obtener el tamaño de la ventana de la terminal.
import fcntl, termios, struct
def calcular_tamagnio_terminal():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th
print(calcular_tamagnio_terminal())


# Ejercicio 57: Medir el tiempo de ejecución de un método.
import time
def sumar_rango(n):
    t_0 = time.time()
    suma = 0
    for i in range(1, n + 1):
        suma += i
    t_1 = time.time()
    return suma, t_1 - t_0
n = 100000
print(sumar_rango(n))
n = 1000000
print(sumar_rango(n))


# Ejercicio 58: Calcular la suma de los primeros n números enteros.
# Usando la fórmula de Gauss: n * (n + 1) / 2
n = 10
suma = n * (n + 1)/2
print(suma)
print()
# Usando un ciclo:
suma = 0
for i in range(1, n + 1):
    suma += i
print(suma)
print()
# Usar la función sum:
suma = sum(range(1, n + 1))
print(suma)


# Ejercicio 59: Calcular la estatura (dada en pies y pulgadas) en centímetros.
# 1 ft = 30.48 cm
# 1 " = 2.54 cm
print('Escriba su estatura (ft y pulgadas): ')
pies = float(input('Pies: '))
pulgadas = float(input('Pulgadas: '))
cm = pies * 30.48
cm += pulgadas * 2.54
print('Su estatura es: {} cm'.format(cm))


# Ejercicio 60: Calcular la longitud de la hipotenusa de un triángulo rectángulo.
from math import sqrt
ab = float(input('Escriba el valor de la longitud del vértice AB: '))
bc = float(input('Escriba el valor de la longitud del vértice BC: '))
hipotenusa = sqrt(ab**2 + bc**2)
print('La longitud de la hipotenusa es: {}'.format(hipotenusa))


# Ejercicio 61: Convertir todas las unidades de tiempo en segundos.
dias = int(input('Escriba la cantidad de días: '))
horas = int(input('Escriba la cantidad de horas: '))
minutos = int(input('Escriba la cantidad de minutos: '))
segundos = int(input('Escriba la cantidad de segundos: '))
segundos += dias * 24 * 60 * 60
segundos += horas * 60 * 60
segundos += minutos * 60
print('La cantidad de segundos es igual: {}'.format(segundos))


# Ejercicio 62: Obtener la ruta absoluta de un archivo.
from os import path
nombre_archivo = 'archivo.txt'
print(path.abspath(nombre_archivo))


# Ejercicio 63: Comprobar si el nombre de un archivo corresponde con una ruta absoluta.
from os import path
nombre_archivo_1 = 'archivo.txt'
nombre_archivo_2 = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\archivo.txt'
print(path.isabs(nombre_archivo_1))
print(path.isabs(nombre_archivo_2))
print(__file__)
print(path.isabs(__file__))


# Ejercicio 64: Consultar la fecha de creación y modificación de un archivo.
import os.path, time
nombre_archivo = 'archivo.txt'
print('Fecha creación: {}'.format(time.ctime(os.path.getctime(nombre_archivo))))
print('Fecha modificación: {}'.format(time.ctime(os.path.getmtime(nombre_archivo))))


# Ejercicio 65: Convertir segundos en días, horas, minutos y segundos.
segundos = int(input('Escriba la cantidad de segundos: '))
dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60
print('Días: {} - Horas: {} - Minutos: {} - Segundos: {}'.format(dias, horas, minutos, segundos))


# Ejercicio 66: Calcular el índice de masa corporal (IMC).
def imc(estatura, peso):
    """
    Calcula el índice de masa corporal.
    """
    return peso / estatura**2
peso = float(input('Escriba su peso (Kg): '))
estatura = float(input('Escriba su estatura (m): '))
indice = imc(estatura, peso)
print('Su IMC es: {}'.format(indice))


# Ejercicio 67: Convertir kilopascales (kPa) en presión psi, mmHg, y atm.
def conversion_kilopascales(kpa):
    """
    Conversión de unidades de presión.
    """
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325
    return psi, mmhg, atm
kilopascales = float(input('Escriba la presión en kilopascales (kPa): '))
print(conversion_kilopascales(kilopascales))


# Ejercicio 68: Sumar los dígitos de un número entero positivo.
# 1234 => 1 + 2 + 3 + 4 = 10
numero = input('Escriba un número entero positivo: ')
lista_digitos = list(numero)
print(lista_digitos)
lista_digitos = [int(c) for c in lista_digitos]
print(lista_digitos)
suma = sum(lista_digitos)
print(suma)
suma = sum([int(c) for c in numero])
print(suma)


# Ejercicio 69: Ordenar tres números de menor a mayor sin usar condicionales ni ciclos.
x = int(input('Escriba el primer número: '))
y = int(input('Escriba el segundo número: '))
z = int(input('Escriba el tercer número: '))
a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c
# 1, 2, 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2
print('Los números ordenados son: {}, {} y {}'.format(a, b, c))


# Ejercicio 70: Ordenar un conjunto de archivos por fecha de creación.
import glob
import os
ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'
archivos = glob.glob(ruta + os.path.sep + '*.py')
archivos.sort(key=os.path.getctime)
print('\n'.join(archivos))


# Ejercicio 71: Calcular el tamaño de un archivo.
import os
archivo = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex071_archivo_tamagnio.py'
def calcular_tamagnio_archivo(archivo):
    """
    Calcula el tamaño de un archivo.
    """
    try:
        return os.path.getsize(archivo)
    except:
        return None
print(calcular_tamagnio_archivo(archivo))
archivo = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex071_archivo_tamagnio.ph'
print(calcular_tamagnio_archivo(archivo))


# Ejercicio 72: Consultar la funcionalidad que provee el módulo incorporado math.
import math
funcionalidad = dir(math)
print('\n'.join(funcionalidad))


# Ejercicio 73: Calcular el punto medio de un segmento de recta.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
def punto_medio(punto_1, punto_2):
    """
    Calcula el punto medio de un segmento de recta.
    """
    x = (punto_1.x + punto_2.x) / 2
    y = (punto_1.y + punto_2.y) / 2
    return Punto(x, y)
punto_1 = Punto(2, 3)
punto_2 = Punto(-5, -7)
m = punto_medio(punto_1, punto_2)
print(m)


# Ejercicio 74: Crear una función para calcular la desviación estándar.
from math import sqrt
def desviacion_estandar(valores, media):
    suma = 0
    for valor in valores:
        suma += (valor - media) ** 2
    radicando = suma / (len(valores) - 1)
    return sqrt(radicando)
def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma / len(valores)
if __name__ == "__main__":
    numeros = [7, 3, 13, 17, 10, 8, 12, 9]
    media = calcular_media(numeros)
    resultado = desviacion_estandar(numeros, media)
    print('La desviación estándar es: {}'.format(resultado))


# Ejercicio 75: Obtener la información de derechos de autor de un módulo.
import sys
import datetime
print(sys.copyright)
# print(datetime.copyright)


# Ejercicio 76: Obtener los argumentos de línea de comandos.
# $ python programa.py 1 Python
import sys
nombre_script = sys.argv[0]
cantidad_args = len(sys.argv)
argumentos = str(sys.argv)
print('Nombre script: {}'.format(nombre_script))
print('Cantidad de argumentos: {}'.format(cantidad_args))
print('Lista de argumentos: {}'.format(argumentos))


# Ejercicio 77: Determinar el orden de los bytes en la arquitectura de ejecución actual.
# Big-Endian, Little-Endian
import sys
if sys.byteorder == 'little':
    print('Plataforma little-endian')
else:
    print('Plataforma big-endian')


# Ejercicio 78: Obtener un listado de los módulos incorporados disponibles.
import sys
nombres_modulos = sorted(sys.builtin_module_names)
nombres_modulos = ', '.join(nombres_modulos)
print(nombres_modulos)


# Ejercicio 79: Obtener el tamaño en bytes de un objeto.
import sys
python = 'Python'
javascript = 'JavaScript'
java = 'Java'
csharp = 'C#'
print('La cadena %s ocupa %i bytes' % (python, sys.getsizeof(python)))
print('La cadena %s ocupa %i bytes' % (javascript, sys.getsizeof(javascript)))
print('La cadena %s ocupa %i bytes' % (java, sys.getsizeof(java)))
print('La cadena %s ocupa %i bytes' % (csharp, sys.getsizeof(csharp)))


# Ejercicio 80: Obtener el valor límite de recursión.
import sys
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(sys.getrecursionlimit())
numero = 50
print(fibonacci(numero))


# Ejercicio 81: Concatenar una n cantidad de cadenas de caracteres con join.
lenguajes = ['Python', 'C#', 'Java', 'JavaScript', 'Kotlin', 'Go', 'PHP']
cadena = ', '.join(lenguajes)
print(cadena)


# Ejercicio 82: Calcular la suma de los elementos de un objeto iterable.
numeros = [13, 7, 2, 5, 29, 17, 7, 31, 101]
suma = 0
for numero in numeros:
    suma += numero
print('Suma de todos los números: %i' % suma)
print()
suma = sum(numeros)
print('Suma de todos los números: %i' % suma)


# Ejercicio 83: Comprobar que todos los elementos de una colección son mayores respecto a un número.
numeros = [7, 3, 2, 5, 11]
print(all(x > 1 for x in numeros))
print(all(x > 5 for x in numeros))


# Ejercicio 84: Contar la cantidad de ocurrencias de un carácter en una cadena de caracteres.
cadena = 'Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.'
cantidad_e = cadena.count('e')
print('La cantidad del carácter `e` es igual a %i' % cantidad_e)
cantidad_ñ = cadena.count('ñ')
print('La cantidad del carácter `ñ` es igual a %i' % cantidad_ñ)


# Ejercicio 85: Determinar si una ruta corresponde con un archivo o carpeta.
import os
def validar_ruta(ruta):
    if os.path.isdir(ruta):
        return 'Es un directorio'
    elif os.path.isfile(ruta):
        return 'Es un archivo'
    else:
        return 'Es un archivo especial (socket, dispositivo de gestión archivos)'
ruta = r'D:\Dropbox\Pro\Tutorship\Java'
print(validar_ruta(ruta))
ruta = r'D:\Dropbox\Pro\Tutorship\Java\Reloj.jpg'
print(validar_ruta(ruta))


# Ejercicio 86: Obtener el valor numérico de un carácter ASCII.
perfil_twitter = '@Python'
for c in perfil_twitter:
    print('%s: %i' % (c, ord(c)))


# Ejercicio 87: Obtener el tamaño de un archivo.
ruta = r'D:\Dropbox\Downloads\Software\Hirens.BootCD.15.2.zip'
import os
archivo_bytes = os.path.getsize(ruta)
print(archivo_bytes)


# Ejercicio 88: Formatear la salida de una cadena de caracteres.
x = 2
y = 3
suma = x + y
print('La suma de ' + str(x) + ' y ' + str(y) + ' es igual a ' + str(suma))
print('La suma de',x, 'y', y , 'es igual a', str(suma))
print('La suma de %d y %d es igual a %d' % (x, y, suma))
print('La suma de {} y {} es igual a {}'.format(x, y, suma))


# Ejercicio 89: Generar números aleatorios y verificar que todos sean impares.
from random import randint
def generar_impares(n=5):
    impares = []
    while True:
        numeros = [randint(1, 10) for _ in range(n)]
        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break
    return impares
impares = generar_impares()
print(impares)
print(generar_impares(20))


# Ejercicio 90: Generar n cantidad de números primos consecutivos.
# 2, 3, 5, 7, 11, 13, ...
def generar_primo():
    numero = 2
    yield numero
    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0
            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1
                if contador_divisores > 2:
                    break
                contador += 1
            if contador_divisores == 2:
                yield temp
g = generar_primo()
primos = [next(g) for _ in range(20)]
print(primos)


# Ejercicio 91: Alternar el contenido de dos variables.
a = 2
b = 3
# a = 3, b = 2
print(a, b)
temp = a
a = b
b = temp
print(a, b)
print()
a = 2
b = 3
print(a, b)
a, b = b, a
# a, b = (b, a)
print(a, b)


# Ejercicio 92: Filtrar números por medio de la función filter.
numeros = [i for i in range(10)]
print(numeros)
filtro_impares = lambda x: x % 2 == 1
impares = filter(filtro_impares, numeros)
print(list(impares))


# Ejercicio 93: Obtener el número de ID de un objeto.
numeros = [2, 3, 5]
print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))
def mostrar_id(objeto):
    print(id(objeto))
mostrar_id(numeros)
objeto = object()
mostrar_id(objeto)


# Ejercicio 94: Convertir una cadena de bytes en una lista de enteros.
cadena_bytes = b'Python'
lista_enteros = list(cadena_bytes)
print(lista_enteros)
# Python


# Ejercicio 95: Comprobar si una cadena de caracteres representa un número.
def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except (TypeError, ValueError):
        return False
cadena = '2.7182'
print(es_numerico(cadena))
cadena = '3.1415ab'
print(es_numerico(cadena))
cadena = (5.3, 7.9)
print(es_numerico(cadena))


# Ejercicio 96: Imprimir el estado de la pila de llamadas.
import traceback
def funcion():
    xyz()
def xyz():
    traceback.print_stack()
funcion()


# Ejercicio 97: Imprimir el listado de variables especiales que usa Python.
# nombres = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print('\n'.join(' '.join(nombres[i:i+8]) for i in range(0, len(nombres), 8)))


# Ejercicio 98: Imprimir el tiempo del sistema con el módulo time.
import time
print(time.ctime())


# Ejercicio 99: Limpiar la pantalla o terminal.
import platform
import os
import time
def limpiar_pantalla():
    time.sleep(2)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
if __name__ == "__main__":
    limpiar_pantalla()
""" 
Unir muchos, unos 1000 archivos de python en uno solo que se llamara fer.py
ejemplo:
ex001_version.py
ex002_print.py
...
ex999_ordenar_lista_cadenas_segun_longitud_cadena.py
"""
# Importar módulos
import os
import glob
 # Variables
ruta = "./Parte001"
archivos = glob.glob(os.path.join(ruta, "ex*.py"))
salida = "fer.py"
# Unir archivos 
with open(salida, "w") as f_out:
    for archivo in archivos:
        with open(archivo) as f_in:
            f_out.write(f_in.read())
            f_out.write("")
 # Salida
print("Archivos unidos en: {}".format(salida))
# Archivos unidos en: fer.py
# Path: Parte001\ex1001_unir_archivos_python.py
# 
# # Ejercicio 100: Obtener el nombre del host donde se ejecuta un script.
import socket
nombre_host = socket.gethostname()
print('El nombre del host es %s' % nombre_host)


# Ejercicio 101: Acceder a una URL e imprimir su contenido HTML.
from http.client import HTTPConnection
url = 'example.com'
conexion = HTTPConnection(url)
conexion.request('GET', '/')
resultado = conexion.getresponse()
contenido = resultado.read()
print(contenido)


# Ejercicio 102: Mostrar el contenido de un directorio por medio de subprocess.
import subprocess
resultado = subprocess.check_output('dir', shell=True, universal_newlines=True)
print(resultado)


# Ejercicio 103: Obtener el nombre de archivo de una ruta absoluta.
import os
ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex030_mcd.py'
nombre_archivo = os.path.basename(ruta)
print(nombre_archivo)


# Ejercicio 104: Obtener el ID de usuario, el ID de grupo, y grupos complementarios en Linux.
import os
print('El ID de usuario es: %d' % os.geteuid())
print('El ID de grupo es: %d' % os.getegid())
print('Los IDs de grupos complementarios son: {}'.format(str(os.getgroups())))


# Ejercicio 105: Obtener la configuración de un usuario en el entorno operacional.
import os
print(os.environ)


# Ejercicio 106: Separar la ruta de la extensión de archivo.
import os.path
rutas = [r'C:\AUTOEXEC.BAT', '/etc/passwd', 'lenguajes.txt', '', 'code', r'C:\\', '/']
for ruta in rutas:
    print('%s: ' % ruta, os.path.splitext(ruta))


# Ejercicio 107: Obtener las propiedades básicas de un archivo.
import os
import time
archivo = 'archivo.txt'
print('Archivo: %s' % archivo)
print('Fecha modificación: {}'.format(time.ctime(os.path.getmtime(archivo))))
print('Fecha acceso: {}'.format(time.ctime(os.path.getatime(archivo))))
print('Fecha cambio: {}'.format(time.ctime(os.path.getctime(archivo))))
print('Tamaño: %d bytes' % os.path.getsize(archivo))


# Ejercicio 108: Consultar propiedades de archivos y directorios.
import os
rutas = ['archivo.txt', r'C:\Windows', 'no_existe.txt', os.path.dirname(r'C:\Windows'), __file__]
for ruta in rutas:
    print('Archivo: %s' % ruta)
    print('¿Existe?: {}'.format(os.path.exists(ruta)))
    print('¿Es ruta absoluta?: {}'.format(os.path.isabs(ruta)))
    print('¿Es archivo?: {}'.format(os.path.isfile(ruta)))
    print('¿Es carpeta?: {}'.format(os.path.isdir(ruta)))
    print()


# Ejercicio 109: Obtener el valor de una variable de entorno.
import os
variable_entorno = 'JAVA_HOME'
print(os.getenv(variable_entorno))
variable_entorno = 'MAVEN_HOME'
print(os.getenv(variable_entorno))
variable_entorno = 'CONDA_HOME'
print(os.getenv(variable_entorno))


# Ejercicio 110: Obtener los números divibles por 7 usando una función anónima.
numeros = [3, 14, 29, 42, 70, 2, 7, 8, 9, 13]
divisible_por_7 = lambda x: x % 7 == 0
numeros_div_7 = filter(divisible_por_7, numeros)
print(list(numeros_div_7))


# Ejercicio 111: Seleccionar archivos de un tipo específico.
import glob
import os
ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'
comodin = '*.py'
lista_archivos = glob.glob(ruta + os.sep + comodin)
print(lista_archivos)


# Ejercicio 112: Eliminar un elemento específico de una lista.
colores = ['Rojo', 'Verde', 'Azul', 'Naranja', 'Negro', 'Blanco']
print('Cantidad elementos: %d' % len(colores))
del colores[1]
print('Cantidad elementos: %d' % len(colores))
del colores[6]


# Ejercicio 113: Validar si un número ingresado por el usuario es válido.
def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
numero = input('Escriba un número entero: ')
if es_numerico(numero):
    print('Ha digitado un valor válido.')
else:
    print('El valor digitado no corresponde con un número.')


# Ejercicio 114: Usar la función filter para obtener los números positivos de una lista.
numeros = [-2, 4, -8, 5, 7, 9, -10, -13]
positivos = list(filter(lambda x: x >= 0, numeros))
print(positivos)


# Ejercicio 115: Calcular el producto de los elementos de una lista sin usar un ciclo for.
from functools import reduce
numeros = [2, 7, 9]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)


# Ejercicio 116: Crear representación de caracteres en estándar Unicode.
# ¡Python es tremendo!
cadena_unicode = u'\u00a1\u0050\u0079\u0074\u0068\u006f\u006e \u0065\u0073 \u0074\u0072\u0065\u006d\u0065\u006e\u0064\u006f\u0021'
print(cadena_unicode)


# Ejercicio 117: Validar que dos cadenas caracteres tienen la misma ubicación en memoria.
lenguaje = 'Python'
frase = 'Python es tremendo!'
print(hex(id(lenguaje)))
print(hex(id(frase)))
lenguaje = lenguaje + ' 3.8.0'
print(hex(id(lenguaje)))
cadena = 'Python'
print(hex(id(cadena)))


# Ejercicio 118: Crear la representación en cadena de bytes desde una cadena de caracteres.
frase = 'Python es tremendo!'
print(frase)
print(type(frase))
cadena_bytes = bytes(frase, 'utf-8')
print(cadena_bytes)
print(type(cadena_bytes))


# Ejercicio 119: Formatear la salida de un número de punto flotante (float).
real = 1.41421356
print('Valor de la variable `real`: %f' % real)
print('Valor de la variable `real`: %.2f' % real)
print('Valor de la variable `real`: %.7f' % real)
real = 1.00
print('Valor de la variable `real`: %f' % real)
print('Valor de la variable `real`: %.2f' % real)
print('Valor de la variable `real`: %.13f' % real)


# Ejercicio 120: Limitar la visualización del número de caracteres de una cadena.
lenguaje = '¡Python es tremendo!'
print(lenguaje)
print(lenguaje[0:7])
print(lenguaje[:7])
print('%.7s' % lenguaje)
print()
cadena = '123456789'
print(cadena[:6])
print('%.6s' % cadena)


# Ejercicio 121: Determinar si una variable está definida o no.
try:
    division = 5 / x
    print(division)
except NameError as e:
    print('No se pudo realizar la división. Una variable no existe: %s' % e)
else:
    print('La operación se realizó de forma satisfactoria.')
print('...')
x = 3
try:
    division = 5 / x
    print(division)
except NameError as e:
    print('No se pudo realizar la división. Una variable no existe: %s' % e)
else:
    print('La operación se realizó de forma satisfactoria.')
print('---')


# Ejercicio 122: Gestión de una excepción tipo aritmética.
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
print('...')


# Ejercicio 123: Mostrar información de las capacidades de los tipos numéricos.
import sys
print('Información tipo de dato float: ', sys.float_info)
print()
print('Información tipo de dato int: ', sys.int_info)
print()
print('Tamaño máximo entero: ', sys.maxsize)


# Ejercicio 124: Comprobar si múltiples variables contienen el mismo valor.
a, b, c = 50, 50, 50
print(a, b, c)
if a == b and a == c:
    print('Sí, son iguales')
if a == b == c:
    print('Sí, son iguales')


# Ejercicio 125: Computar la suma de los conteos de los duplicados de una lista.
from collections import Counter
numeros = [7, 5, 9, 2, 2, 3, 9, 7, 0, 1]
conteos = Counter(numeros)
print(conteos)
print(sum(conteos.values()))


# Ejercicio 126: Encontrar el módulo al que pertenece un elemento de programa.
from inspect import getmodule
from math import sin
print(getmodule(sin))
print(type(getmodule(sin)))
print(dir(type(getmodule(sin))))


# Ejercicio 127: Comprobar si un elemento de programa dado es una clase.
from inspect import isclass
from collections import Counter
from math import cos
print(isclass(Counter))
print(isclass(cos))
class Clase:
    pass
def funcion():
    pass
print()
print(isclass(Clase))
print(isclass(funcion))


# Ejercicio 128: Comprobar si un carácter dado existe en una cadena de caracteres.
lenguaje = 'Python es tremendo!'
print(lenguaje.count('y') > 0)
print(any(c == 'y' for c in lenguaje))
print(any(c == 'x' for c in lenguaje))
print(lenguaje.count('x') > 0)
print()
print(lenguaje.count('p') > 0)
print(lenguaje.count('P') > 0)
print()
print(any(c.lower() == 'p' for c in lenguaje))


# Ejercicio 129: Rellenar una cadena de caracteres con un carácter específico.
# Python => ***Python***
lenguaje = 'Python'
print(lenguaje)
print(lenguaje.rjust(6 + 3, '*'))
print(lenguaje.ljust(6 + 3, '*'))
print(lenguaje.rjust(6 + 3, '*').ljust(12, '*'))


# Ejercicio 130: Determinar si una función dada es una función generadora.
from inspect import isgeneratorfunction
def funcion():
    return 'Python'
print(isgeneratorfunction(funcion))
def generar_pares():
    numero = 2
    yield numero
    while True:
        numero += 2
        yield numero
print(isgeneratorfunction(generar_pares))


# Ejercicio 131: Crear variables a partir de los valores de una lista.
numeros = [2, 3, 5, 7]
dos, tres = numeros[0:2]
print(dos, tres)
print()
tres, siete = numeros[1], numeros[-1]
print(tres, siete)
print()
tres, _, siete = numeros[1:]
print(tres, siete)


# Ejercicio 132: Obtener la ruta absoluta del directorio del usuario.
import os
print(os.path.expanduser('~'))


# Ejercicio 133: Calcular el tiempo de ejecución de una función.
from timeit import default_timer
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
inicio = default_timer()
fibonacci(20)
fin = default_timer()
print(fin - inicio)
print()
inicio = default_timer()
fibonacci(37)
fin = default_timer()
print(fin - inicio)


# Ejercicio 134: Capturar datos enteros en una única línea de código.
print('Escriba los valores x e y: ', end='')
x, y = map(int, input().split())
print(x, y)


# Ejercicio 135: Comprobar si un elemento de programa es generador.
from inspect import isgenerator
def generador_impares():
    numero = 1
    yield numero
    while True:
        numero += 2
        yield numero
impares = generador_impares()
print(isgenerator(impares))
print(next(impares))
print(next(impares))
print(next(impares))
print(next(impares))
print(next(impares))
print(next(impares))


# Ejercicio 136: Excluir directorios durante la exploración de un directorio específico.
import os
ruta = r'C:\Windows'
archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]
print(archivos)


# Ejercicio 137: Extraer un único elemento (llave y valor) de un diccionario.
lenguajes = {'Python': '3.8.0', 'Java': '12', 'C#': '8', 'PHP': '7.1.0'}
(lenguaje, version), _, (csharp, vcsharp), _ = lenguajes.items()
print(lenguaje, version)
print(csharp, vcsharp)


# Ejercicio 138: Convertir valores lógicos a enteros.
a = 'true'
uno = int(a == 'true')
print(uno)
a = 'falso'
cero = int(a == 'true')
print(cero)


# Ejercicio 139: Validar si una dirección IP dada es válida.
import socket
def ip_valida(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
print(ip_valida('127.0.0.1'))
print(ip_valida('192.168.0.1'))
print(ip_valida('192.168.0.1024'))
print(ip_valida('192.168.0.24.7'))


# Ejercicio 140: Convertir un número entero a binario.
numero = 10
print(bin(numero))
print(format(numero, '0b'))
print(type(format(numero, '0b')))
print(format(numero, '010b'))
print(format(numero, '016b'))


# Ejercicio 141: Convertir un número entero a un número hexadecimal.
entero = 255
# Conversión numérica con la función hex:
hexadecimal = hex(entero)
print(type(hexadecimal))
print(hexadecimal)
print()
# Conversión a través de la función format:
hexadecimal = format(entero, '0x')
print(type(hexadecimal))
print(hexadecimal)


# Ejercicio 142: Obtener los datos básicos de la plataforma operacional.
import os, platform
print('Nombre de la plataforma: %s' % os.name)
print('Nombre del sistema operativo: %s' % platform.system())
print('Versión: %s' % platform.release())


# Ejercicio 143: Detectar el modo del sistema operativo (32 ó 64 bits).
import struct
modo_so = struct.calcsize('P') * 8
print('El sistema operativo actual es de %i bits' % modo_so)


# Ejercicio 144: Comprobar si una variable es entero o cadena de caracteres.
a = 13
print(isinstance(a, int) or isinstance(a, str))
a = '13'
print(isinstance(a, int) or isinstance(a, str))
a = [13]
print(isinstance(a, int) or isinstance(a, str))


# Ejercicio 145: Determinar si una variable es una lista, tupla, o un conjunto.
a = [2, 3, 5, 7]
b = (2, 3, 5, 7)
c = {2, 3, 5, 7}
print(type(a) is list)
print(type(b) is tuple)
print(type(c) is set)
# 146: Encontrar las rutas en disco donde se hallan las fuentes de los módulos Python.
import sys, os
print('Lista de directorios del módulo `sys`:')
print('\n'.join(sys.path))
print()
print('Lista de directorios del módulo `os`:')
print(os.path)


# Ejercicio 147: Comprobar si un número es múltiplo de otro.
def multiplo(a, b):
    """
    Comprueba si un número es múltiplo de otro.
    """
    return a % b == 0
print(multiplo(12, 6))
print(multiplo(13, 2))


# Ejercicio 148: Encontrar el mínimo y el máximo de una lista sin usar funciones existentes.
# min, max
def min_max(numeros):
    """
    Encuentra el menor y el mayor de una lista de números.
    """
    if len(numeros) > 0:
        menor = numeros[0]
        mayor = numeros[0]
        for n in numeros:
            if n < menor:
                menor = n
            if n > mayor:
                mayor = n
        return menor, mayor
    else:
        return None
datos = [9, 3, 2, 13, 0, 23, 8, 7]
print(min_max(datos))
datos = []
print(min_max(datos))


# Ejercicio 149: Calcular la suma del cubo de cada número menor a un número n dado.
# n = 5, 1^3 + 2^2 + 3^3 + 4^3
# = 1 + 8 + 27 + 64 = 100
def suma_cubos(n):
    suma = 0
    n -= 1
    while n > 0:
        suma += n**3
        n -= 1
    return suma
n = 5
print(suma_cubos(n))
sumatoria_cubos = sum([i**3 for i in range(0, n)])
print(sumatoria_cubos)


# Ejercicio 150: Comprobar si existe al menos un producto impar entre los elementos de una lista.
def es_producto_impar(numeros):
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if i != j:
                producto = numeros[i] * numeros[j]
                if producto & 1:
                    return True
    return False
datos = [2, 3, 7, 8, 1]
print(es_producto_impar(datos))
datos = [2, 4, 6]
print(es_producto_impar(datos))


# Ejercicio 151: Comprobar si todos los elementos de una lista son distintos.
# [2, 3, 2, 5, 1] => {2, 3, 5, 1}
def elementos_distintos(datos):
    return len(datos) == len(set(datos))
lista = [2, 3, 2, 5, 1]
print(elementos_distintos(lista))
lista = [2, 3, 5, 7]
print(elementos_distintos(lista))


# Ejercicio 152: Aleatorizar las vocales almacenadas en una lista.
import random
vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales)
random.shuffle(vocales)
print(vocales)


# Ejercicio 153: Eliminar cada i-ésimo elemento de una lista.
# [1, 2, 3, 4, 5, 6, 7, 8] => [1, 3, 5, 7]
# [1, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8] => [1, 2, 4, 5, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8] => []
def eliminar_i_esimo_elemento(datos, iesimo=2):
    longitud = len(datos)
    if longitud > 0:
        cantidad_eliminar = longitud // iesimo
        iesimo -= 1
        indice = 0
        while cantidad_eliminar > 0:
            indice = (iesimo + indice) % longitud
            datos.pop(indice)
            longitud -= 1
            cantidad_eliminar -= 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros)
print(numeros)
print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 3)
print(numeros)
print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 10)
print(numeros)
print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 8)
print(numeros)
print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros)
eliminar_i_esimo_elemento(numeros, 1)
print(numeros)


# Ejercicio 154: Obtener las tripletas de números diferentes cuya suma es cero.
from itertools import permutations
def obtener_tripletas(numeros):
    if len(numeros) == 3:
        if len(set(numeros)) == 3:
            if sum(numeros) == 0:
                return [tuple(numeros)]
            else:
                return []
        else:
            return []
    else:
        perms = permutations(numeros, 3)
        tripletas = []
        for perm in list(perms):
            if len(set(perm)) == 3 and sum(perm) == 0:
                tripletas.append(perm)
        return tripletas
lista = [0, -2, 0, -1, 2, 4, -6, 1]
print(obtener_tripletas(lista))


# Ejercicio 155: Uso del método zfill para rellenar una cadena de caracteres.
# 9 => 0009
# 123 => 0123
cadena = '9'
print(cadena.zfill(4))
cadena = '123'
print(cadena.zfill(4))
cadena = '1234'
print(cadena.zfill(4))


# Ejercicio 156: Contar el número de ocurrencias de palabras en una frase o párrafo.
frase = """
Crimen y castigo ​(en ruso: Преступле́ние и наказа́ние, romanización: Prestupléniye i nakazániye) es una novela de carácter psicológico escrita por el autor ruso Fiódor Dostoievski. Fue publicada por primera vez en la revista El mensajero ruso, en 1866, en doce partes, y publicada después como novela.2​3​ Junto con Guerra y paz de León Tolstói, se considera que la novela es una de las más influyentes e internacionales de la literatura rusa.4​ Asimismo, los diálogos mantenidos entre el protagonista, Raskólnikov, y el inspector de policía, son considerados por algunos autores, como el prestigioso literato Stefan Zweig, una de las cimas de la literatura universal.
La historia narra la vida de Rodión Raskólnikov, un estudiante en la capital de la Rusia Imperial, San Petersburgo. Este joven se ve obligado a suspender sus estudios por la miseria en la cual se ve envuelto, a pesar de los esfuerzos realizados por su madre Pulqueria y su hermana Dunia para enviarle dinero. Necesitado de financiación para pagar sus gastos, había recurrido a una anciana prestamista vil y egoísta, en cuya casa empeña algunos objetos de valor.
"""
palabras = frase.split(' ')
frecuencia_palabras = [palabras.count(p) for p in palabras]
print('Frase:\n%s\n' % frase)
print('Ocurrencias palabrass: ', frecuencia_palabras)
print()
print(str(list(zip(palabras, frecuencia_palabras))))


# Ejercicio 157: Contar las ocurrencias de las letras en un archivo de texto plano.
import collections
import pprint
nombre_archivo = 'crimen_castigo.txt'
with open(nombre_archivo, 'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)
# print(conteo_caracteres)
print(salida)


# Ejercicio 159: Obtener las últimas noticias desde Google News con Beautiful Soup.
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
# Conexión:
url_google_news = 'https://news.google.com/news/rss'
cliente = urlopen(url_google_news)
contenido_xml = cliente.read()
cliente.close()
# Lectura en el formato XML:
pagina = soup(contenido_xml, 'xml')
items = pagina.findAll('item')
# Iterar cada noticia:
for item in items:
    print(item.title.text)
    print(item.link.text)
    print(item.pubDate.text)
    print('=' * 70)


# Ejercicio 160: Mostrar el listado de todos los módulos instalados localmente.
import pkg_resources
modulos_instalados = pkg_resources.working_set
modulos_instalados = sorted(["%s==%s" % (i.key, i.version) for i in modulos_instalados])
for m in modulos_instalados:
    print(m)


# Ejercicio 161: Obtener información del sistema operativo donde se ejecuta un script Python.
import platform as pl
perfil_so = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for perfil in perfil_so:
    if hasattr(pl, perfil):
        print('%s: %s' % (perfil, getattr(pl, perfil)()))


# Ejercicio 162: Determinar si la suma de los elementos de una lista es igual a un número dado.
def suma_igual(numero, numeros):
    return sum(numeros) == numero
lista_1 = [2, 3, 5, 7, 11]
lista_2 = (8, 9, 2)
lista_3 = [0, 1, 3, 5]
total = 19
print(suma_igual(total, lista_1))
print(suma_igual(total, lista_2))
print(suma_igual(total, lista_3))


# Ejercicio 163: Generar combinaciones a través del módulo itertools.
from itertools import combinations
numeros = [2, 3, 5, 7, 11, 13]
for c in combinations(numeros, 3):
    print(c)


# Ejercicio 164: Crear una demostración de gráficos de tortuga.
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# Ejercicio 165: Calcular la suma de dos números sin usar el operador +.
# & 
# ^
# ~
# |
# <<
# >>
def suma_con_operador_bit(a, b):
    while b != 0:
        temp = a & b
        a = a ^ b
        b = temp << 1
    return a
# temp = 011 & 101 = 1
# a = 011 ^ 101 = 110
# b = 10
# temp = 110 & 010 = 010
# a = 110 ^ 010 = 100
# b = 0100
# temp = 0100 & 0100 = 0100
# a = 0100 ^ 0100 = 0000
# b = 01000
# temp = 00000 & 01000 = 00000
# a = 00000 ^ 01000 = 01000
# b = 000000
# a = 1000 = 8 [10]
print(suma_con_operador_bit(3, 5))
print(suma_con_operador_bit(10, 15))


# Ejercicio 166: Validar la prioridad de los operadores suma, resta, producto y división.
__prioridad__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}
def tiene_mayor_prioridad(operador_1, operador_2):
    return __prioridad__[operador_1] >= __prioridad__[operador_2]
# 3 + 7 - 3 = 7
print(tiene_mayor_prioridad('-', '+'))
# 3 * 7 - 3 = 18
print(tiene_mayor_prioridad('*', '+'))
print(tiene_mayor_prioridad('/', '*'))
print(tiene_mayor_prioridad('-', '/'))


# Ejercicio 167: Calcular el tercer lado de un triángulo rectángulo dados dos lados.
from math import sqrt
def pitagoras(cateto_adyacente, cateto_opuesto, hipotenusa):
    if cateto_adyacente == 'x':
        return 'cateto adyacente', sqrt(hipotenusa**2 - cateto_opuesto**2)
    elif cateto_opuesto == 'x':
        return 'cateto opuesto', sqrt(hipotenusa**2 - cateto_adyacente**2)
    elif hipotenusa == 'x':
        return 'hipotenusa', sqrt(cateto_adyacente**2 + cateto_opuesto**2)
    else:
        return None, None
print(pitagoras(5, 7, 'x'))
print(pitagoras('x', 5, 7))
print(pitagoras(5, 'x', 7))
print(pitagoras(5, 4.9, 7))


# Ejercicio 168: Uso básico del operador walrus de Python 3.8.0.
# :=
cadena = 'Python'
if (l := len(cadena)) > 5:
    print(f'La cadena de caracteres {cadena} tiene más de 5 caracteres; exactamente {l}')


# Ejercicio 169: Uso de parámetros sólo posicionales en Python 3.8.0.
def funcion(a, b, /, c, d, *, e, f):
    return 0
funcion(1, 2, 3, d=4, e=5, f=6)
#funcion(1, b=2, 3, d=4, e=5, f=6)
#funcion(a=1, b=2, 3, d=4, e=5, f=6)
#funcion(1, 2, 3, d=4, 5, f=6)
def potencia(x, y, /):
    return x**y
potencia(2, 3)


# Ejercicio 170: Encontrar el valor medio entre tres números.
# 3, 9, 7 => 3, 7, 9
x = int(input('Digite el primer número: '))
y = int(input('Digite el segundo número: '))
z = int(input('Digite el tercer número: '))
# Solución no. 1:
menor = min(x, y, z)
mayor = max(x, y, z)
valor_medio = (x + y + z) - menor - mayor
print(menor, valor_medio, mayor)
print()
# Solución no. 2:
numeros = [x, y, z]
print(numeros)
numeros = sorted(numeros)
print(numeros)


# Ejercicio 171: Encontrar la cantidad de potencias de 2 a la n en una cadena de caracteres.
# "248163264128"
# "24816"
# "248"
def encontrar_potencias_2(secuencia):
    respuesta = True
    base = 2
    resultado = 2
    grado = 1
    while respuesta:
        if str(resultado) in secuencia:
            grado += 1
            resultado = pow(base, grado)
        else:
            respuesta = False
    return grado - 1
print(encontrar_potencias_2('248'))
print(encontrar_potencias_2('24816'))
print(encontrar_potencias_2('248163264128'))


# Ejercicio 172: Explorar el nuevo soporte para depuración por medio de f-strings de Python 3.8.0.
import datetime
nombre = 'Daniela Ortiz'
fecha = datetime.datetime.now()
print('nombre=', nombre)
print('fecha=', fecha)
print()
# Uso de f-strings:
print(f'{nombre=}')
print(f'{fecha=}')
print()
fecha_nacimiento = datetime.date(1993, 10, 2)
hoy = datetime.date.today()
delta = hoy - fecha_nacimiento
print(f'{delta.days=:,d}')


# Ejercicio 173: Calcular la cantidad mínima de monedas para el cambio de una compra.
def calcular_cantidad_min_cambio(monto):
    nominaciones = [500, 200, 100, 50, 20, 10]
    monedas = 0
    for i in range(len(nominaciones)):
        nominacion = nominaciones[i]
        monedas += int(monto / nominacion)
        monto = int(monto % nominacion)
    return monedas
print(calcular_cantidad_min_cambio(1000))
print(calcular_cantidad_min_cambio(550))
print(calcular_cantidad_min_cambio(720))


# Ejercicio 174: Calcular en n-ésimo término de una secuencia.
# Descripción del problema: Crear una secuencia donde los primeros cuatro números de la secuencia sean iguales a 1, y cada término sucesivo es igual a la suma de los primeros cuatro términos.
# n = 5 => (1, 2, 3, 4) => 1
# 1 + 1 + 1 + 1 = 4
def secuencia(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    else:
        return secuencia(n - 1) + secuencia(n - 2) + secuencia(n - 3) + secuencia(n - 4)
print(secuencia(5))
# secuencia(4) + secuencia(3) + secuencia(2) + secuencia(1)
# 1 + 1 + 1 + 1 = 4
print(secuencia(6))
# secuencia(6):
# secuencia(5) + secuencia(4) + secuencia(3) + secuencia(2)
# secuencia(5):
# secuencia(4) + secuencia(3) + secuencia(2) + secuencia(1)
# 1 + 1 + 1 + 1 = 4
# 4 + 1 + 1 + 1 = 7


# Ejercicio 175: Reducir un número por medio de la suma de sus digitos.
# Descripción: Obtener un número entero positivo y sustraer la suma de sus digitos mientras que el número sea positivo.
def reducir_numero(n):
    cadena = str(n)
    contador = 0
    while n > 0:
        n -= sum([int(c) for c in cadena])
        cadena = str(n)
        contador += 1
    return contador
print(reducir_numero(7))
print(reducir_numero(29))
# n = 29
# cadena = '29', contador = 0
# n = 18
# cadena = '18', contador = 1
# n = 9
# cadena = '9', contador = 2
# n = 0
# cadena = '0', contador = 3


# Ejercicio 176: Contar la cantidad de divisores de un número entero positivo.
# Solución #1:
def contar_divisores(n):
    contador_divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador_divisores += 1
    return contador_divisores
# Solución #2:
def divisores(n):
    if isinstance(n, int):
        if n > 0:
            return len([i for i in range(1, n + 1) if n % i == 0])
        else:
            raise ValueError('El valor pasado no es un número positivo.')
    else:
        raise TypeError('El valor pasado como argumento no es un entero.')
print(contar_divisores(5))
print(contar_divisores(8))
print()
print(divisores(5))
print(divisores(8))
print()
try:
    print(divisores('5'))
except Exception as e:
    print(e)


# Ejercicio 177: Encontrar los dígitos faltantes en un número de teléfono móvil.
# 3112223333 => 0456789
# {1, 2, 3}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - {1, 2, 3} = {0, 4, 5, 6, 7, 8, 9}
def encontrar_digitos_faltantes(numero):
    if isinstance(numero, str):
        try:
            numero = int(numero)
            if numero > 0:
                digitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
                numero = {int(d) for d in str(numero)}
                digitos_faltantes = digitos.difference(numero)
                return digitos_faltantes
            else:
                raise ValueError('El número de teléfono debe ser positivo.')
        except:
            raise ValueError('El argumento no es un número')
    else:
        raise TypeError('El argumento no es de tipo cadena de caracteres.')
print(encontrar_digitos_faltantes('3112223333'))
# print(encontrar_digitos_faltantes('-3112223333'))
# print(encontrar_digitos_faltantes('3112223333a'))


# Ejercicio 178: Computar la suma del valor absoluto de pares de elementos de una lista.
# Descripción: Computar la suma de la diferencia absoluta entre dos elementos de una lista. Los elementos deben estar ordenados de forma ascendente.
# Solución:
# [1, 2, 3]
# [1, 2], [1, 3], [2, 3]
from itertools import combinations
def suma_pares_diferentes(numeros):
    """
    Calcula la suma de pares diferente de una lista.
    """
    if isinstance(numeros, list):
        suma = 0
        for c in combinations(numeros, 2):
            suma += sum(c)
        return suma
    else:
        raise TypeError('El argumento pasado a la función no es una lista.')
lista = [1, 2, 3]
print(suma_pares_diferentes(lista))
#print(suma_pares_diferentes('1,2,3'))


# Ejercicio 179: Identificar el tipo de progresión (aritmética o geométrica) a partir de una lista.
# Solución:
# Progresión aritmética: [1, 2, 3, 4] => incremento unitario, [2, 4, 6, 8, 10]
# Progresión geométrica: [2, 6, 18, 54]
def identificar_progresion(numeros):
    if sum(numeros) == 0:
        return None
    else:
        if numeros[1] - numeros[0] == numeros[2] - numeros[1]:
            return 'Aritmética'
        else:
            return 'Geométrica'
print(identificar_progresion([1, 2, 3, 4]))
print(identificar_progresion([0, 0, 0]))
print(identificar_progresion([2, 6, 18, 54]))


# Ejercicio 180: Encontrar los tres edificios más altos de un conjunto de 10 edificios.
# Solución:
from random import randint, seed
seed(0)
alturas = [randint(50, 500) for i in range(10)]
print(alturas)
alturas = sorted(alturas)
print(alturas)
edificios_mas_altos = alturas[-3:]
print(edificios_mas_altos)


# Ejercicio 181: Calcular la suma de los dígitos de dos números.
def suma_digitos(numero):
    return sum([int(c) for c in str(numero)])
def suma_digitos_numeros(numero_1, numero_2):
    if isinstance(numero_1, int) and isinstance(numero_2, int):
        suma_1 = suma_digitos(numero_1)
        suma_2 = suma_digitos(numero_2)
        return suma_1 + suma_2
    else:
        raise TypeError('Los números deben ser enteros.')
x = 13
y = 29
print(suma_digitos_numeros(x, y))
x = 13.5
print(suma_digitos_numeros(x, y))


# Ejercicio 182: Determinar el tipo de triángulo (isósceles, escaleno, equilatero) dados tres lados.
# Solución:
def tipo_triangulo(a, b, c):
    if a == b and a == c:
        return 'Equilatero'
    elif a != b and a != c:
        return 'Escaleno'
    else:
        return 'Isósceles'
print(tipo_triangulo(7, 7, 7))
print(tipo_triangulo(7, 7, 9))
print(tipo_triangulo(7, 8, 9))


# Ejercicio 183: Resolver un sistema de ecuaciones lineales.
# Solución:
# ax + by = c
# dx + ey = f
def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante
        return x, y
    else:
        return None, None
print('Digite los valores para a, b, c, d, e, y f: ')
a, b, c, d, e, f = map(float, input().split())
print(solucion_sistema_ecuaciones(a, b, c, d, e, f))


# Ejercicio 184: Uso de la función accumulate de itertools en Python 3.8.0.
from itertools import accumulate
numeros = [2, 3, 5, 7]
print(list(accumulate(numeros)))
print(list(accumulate(numeros, initial=0)))
print(list(accumulate(numeros, initial=2000)))


# Ejercicio 185: Encontrar todos los números primos menores a un número n dado.
# Función creada en el ejercicio 90:
def generar_primo():
    numero = 2
    yield numero
    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0
            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1 
                if contador_divisores > 2:
                    break
                contador += 1
            if contador_divisores == 2:
                yield temp
def primos_menores(n):
    generador = generar_primo()
    primos = []
    while True:
        primo = next(generador)
        if primo < n:
            primos.append(primo)
        else:
            break
    return primos
print(primos_menores(15))


# Ejercicio 186: Calcular la distancia euclidiana con math.dist de Python 3.8.0.
# math.dist(p, q)
from math import dist
punto_1 = (2, 3)
punto_2 = (-3, 5)
distancia = dist(punto_1, punto_2)
print(distancia)


# Ejercicio 187: Uso de las funciones mean y fmean del módulo statistics.
from statistics import mean, fmean
numeros = [2, 3, 5, 7, 11, 13, 17, 19]
promedio = mean(numeros)
print(promedio)
numeros = [2.3, 5.5, 1.11, 17.19, 13.13]
promedio = fmean(numeros)
print(promedio)


# Ejercicio 188: Calcular la moda de un conjunto de datos numéricos y nominales.
from statistics import mode
numeros = [3, 2, 7, 2, 3, 2, 5, 11, 13, 2]
print(mode(numeros))
lenguajes = ['Python', 'C++', 'C++', 'Java', 'Python', 'C', 'JavaScript', 'Java', 'Python', 'Python']
print(mode(lenguajes))
numeros.append(3)
numeros.append(3)
print(mode(numeros))


# Ejercicio 189: Determinar si dos números (o su suma) superan los 80 dígitos.
def supera_limite(a, b):
    """
    Comprueba si uno o dos números superan un límite establecido.
    """
    return a >= 10**80 or b >= 10**80 or a + b >= 10**80
x = 10**81
y = 1
print(supera_limite(x, y))
x = 3
print(supera_limite(x, y))


# Ejercicio 190: Ordenar un conjunto de datos numéricos de forma descendente.
print('Digite seis números: ', end='')
numeros = list(map(int, input().split()))
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)


# Ejercicio 191: Obtener múltiples modas desde un conjunto de datos numéricos o nominales.
from statistics import multimode
numeros = [0, 3, 2, 7, 2, 3, 2, 5, 11, 13, 2, 3, 3]
print(multimode(numeros))
lenguajes = ['Java', 'Python', 'C++', 'C++', 'Java', 'Python', 'C', 'JavaScript', 'Java', 'Python', 'Python', 'Java']
print(multimode(lenguajes))


# Ejercicio 192: Calcular la media armónica y la media geométrica usando el módulo statistics.
from statistics import geometric_mean, harmonic_mean
media_g = geometric_mean([54, 24, 36])
print(round(media_g, 1))
media_a = harmonic_mean([40, 60])
print(media_a)


# Ejercicio 193: Calcular el área y la circunferencia de un círculo de radio r.
# Solución: 
# área = pi*r^2
# circunferencia = 2*pi*r
from math import pi
r = float(input('Escriba el valor del radio: '))
area = pi * r ** 2
print('El área del círculo es igual a {:.2f}'.format(area))
circunferencia = 2 * pi * r
print('La circunferencia del círculo es igual a {:.2f}'.format(circunferencia))


# Ejercicio 194: Encontrar el nombre del día a partir de una fecha dada.
from datetime import date
print('Ingrese el número del mes y del día: ', end='')
mes, dia = map(int, input().split())
semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
numero_dia = date.isoweekday(date(2019, mes, dia))
print('El nombre del día es: %s' % semana[numero_dia])


# Ejercicio 195: Encontrar la palabra más frecuente y la más larga de un texto dado.
from collections import Counter
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec condimentum ipsum sit amet interdum pretium. Ut auctor magna ac elit molestie aliquet. Nulla quis nisl quam. Suspendisse nec blandit odio. Nulla purus neque, rhoncus quis ultricies vel, faucibus non turpis. Quisque eget tincidunt dolor. Maecenas sollicitudin tempor blandit. Donec tempus lectus sed nunc commodo elementum. Suspendisse volutpat felis vitae sapien iaculis, non tempus lectus laoreet. Maecenas id leo at ligula vehicula iaculis. Fusce ultrices vitae odio eget mattis. Aliquam auctor mattis ex ac tincidunt. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
palabras = texto.split()
contador = Counter(palabras)
palabra_frecuente = contador.most_common()[0][0]
print(contador.most_common())
print('Palabra más frecuente: %s' % palabra_frecuente)
def palabra_mas_larga(palabras):
    palabra = ''
    for p in palabras:
        if len(p) > len(palabra):
            palabra = p
    return palabra
print('La palabra más extensa es: %s' % palabra_mas_larga(palabras))


# Ejercicio 196: Encontrar una combinación de tamaño n que sea igual a un valor.
from itertools import combinations
while True:
    print('Ingrese el tamaño de las combinaciones y el valor de la suma: ', end='')
    n, suma = map(int, input().split())
    if n == 0 and suma == 0:
        break
    combinaciones = list(combinations(range(10), n))
    for c in combinaciones:
        if sum(c) == suma:
            print(c, sum(c))


# Ejercicio 197: Determinar si dos lados adyacentes y la diagonal corresponden a un rectángulo o rombo.
# Descripción: Determinar si dos lados adyacentes y la diagonal de un paralelogramo corresponden a un rectángulo o un rombo.
print('Escriba las longitudes de dos lados adyacentes y la diagonal: ', end='')
a, b, c = map(int, input().split(','))
if a**2 + b**2 == c**2:
    print('Los valores ingresados corresponden con un rectángulo.')
else:
    print('Los valores ingresados corresponden con un rombo.')


# Ejercicio 198: Alternar la posición de dos palabras específicas en una cadena de caracteres.
# Solución:
print('Escriba un texto que incluya las palabras `Python` y `C++`: ', end='')
palabras = input().split()
for i in range(len(palabras)):
    if 'C++' in palabras[i]:
        palabras[i] = 'Python'
    elif 'Python' in palabras[i]:
        palabras[i] = 'C++'
print(*palabras)


# Ejercicio 199: Computar la diferencia entre el valor menor y mayor de un número de 9 dígitos.
# Solución:
# 678961123
# Mayor -> 987663211
# Menor -> 112366789
# Diferencia = Abs(Mayor - Menor)
numero = ''
while len(numero) != 9:
    numero = input('Digite un número de 9 dígitos: ')
    try:
        int(numero)
    except ValueError as e:
        print('MENSAJE: Debe digitar un número.')
        numero = ''
digitos = list(numero)
menor = sorted([int(n) for n in digitos])
mayor = sorted([int(n) for n in digitos], reverse=True)
menor = int(''.join([str(d) for d in menor]))
mayor = int(''.join([str(d) for d in mayor]))
diferencia = mayor - menor
print('{} - {} = {}'.format(mayor, menor, diferencia))


# Ejercicio 200: Suma de los números primos en el rango 2 a 100.
# Función creada en el ejercicio 90:
def generar_primo():
    numero = 2
    yield numero
    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0
            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1 
                if contador_divisores > 2:
                    break
                contador += 1
            if contador_divisores == 2:
                yield temp
suma_primos = 0
generador_primos = generar_primo()
while True:
    primo = next(generador_primos)
    if primo <= 100:
        suma_primos += primo
    else:
        break
print('La suma de los números primos entre 2 y 100 es igual a {}.'.format(suma_primos))


# Ejercicio 201: Representar números como fracciones con la clase Fraction.
from fractions import Fraction
un_medio = Fraction(1, 2)
print(un_medio)
tres_medios = Fraction(3, 2)
print(tres_medios)
suma = un_medio + tres_medios
print(suma)
resta = un_medio - tres_medios
print(resta)
multiplicacion = tres_medios * un_medio
print(multiplicacion)
division = un_medio / tres_medios
print(division)


# Ejercicio 202: Obtener el numerador y denominador de un objeto Fraction.
from fractions import Fraction
tres_medios = Fraction(2, 10)
print(tres_medios)
numerador = tres_medios.numerator
print('Numerador: %i' % numerador)
denominador = tres_medios.denominator
print('Denominador: %i' % denominador)


# Ejercicio 203: Crear una fracción a partir de un número decimal o punto flotante.
# Solución:
# 0.5 => 1/2
# 0.3333333... => 1/3
from fractions import Fraction
decimal = 0.5
un_medio = Fraction(decimal)
print(decimal)
print(un_medio)
numero = '7e-5'
fraccion = Fraction(numero)
print(numero)
print(fraccion)


# Ejercicio 204: Sumar todos los dígitos que aparezcan en una cadena de caracteres.
# Solución:
# Python 3.8.0 es la versión más reciente de este lenguaje de programación.
import re
def sumar_digitos_cadena(cadena):
    patron = r'[0-9]{1,7}'
    numeros = re.findall(patron, cadena)
    numeros = map(int, numeros)
    return sum(numeros)
texto = 'Python 3.8.0 es la versión más reciente de este lenguaje de programación.'
print(sumar_digitos_cadena(texto))
texto = 'Python es génial. La versión mayor más reciente es 3. El número de mejor es 8.'
print(sumar_digitos_cadena(texto))
texto = 'ABC123XYZ7'
print(sumar_digitos_cadena(texto))


# Ejercicio 205: Uso de la función incorporada license.
license()


# Ejercicio 206: Mostrar los créditos Python con la función incorporada credits.
credits()


# Ejercicio 207: Restaurar un texto a partir de la versión acortada del texto.
# Descripción: Dado como texto acortado Python#4A3.8.0Tremend#3o, debería obtenerse PythonAAAA3.8.0Tremendooo
def restaurar_texto(acortado):
    resultado = ''
    indice = 0
    longitud = len(acortado)
    while indice < longitud:
        if acortado[indice] == '#':
            resultado += acortado[indice + 2] * int(acortado[indice + 1])
            indice += 3
        else:
            resultado += acortado[indice]
            indice += 1
    return resultado
texto_acortado = 'Python#4A3.8.0Tremend#3o'
print(restaurar_texto(texto_acortado))
print(restaurar_texto('Python 3.8.0'))


# Ejercicio 208: Calcular el área de un polígono regular dados sus lados y la longitud de cada lado.
from math import pi, tan
def area_poligono_regular(n, s):
    area = n * s**2 / (4 * tan(pi/n))
    return area
numero_lados = 5
longitud_lados =  12
print(area_poligono_regular(numero_lados, longitud_lados))


# Ejercicio 209: Obtener sólo las palabras de longitud de 3 a 6 caracteres.
# Solución:
# Python es génial => Python génial
# Esa canción suena muy bien => Esa canción suena muy bien
def extraer_palabras(frase):
    frase = frase.replace(',', '')
    frase = frase.replace('.', '')
    palabras = [p for p in frase.split() if 3 <= len(p) <= 6]
    return palabras
texto = 'Python es génial.'
print(extraer_palabras(texto))
texto = 'Esa canción suena muy bien'
print(extraer_palabras(texto))


# Ejercicio 210: Comprobar si una palabra o frase es palíndromo.
# Solución:
# oso, anita lava la tina, atar a la rata
# ataralarata
# izquierda = atara
# derecha = arata
# '1001'
def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2 == 0:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1:]
    return izquierda == derecha[::-1]
print(es_palindromo('1001'))
print(es_palindromo('ataralarata'))
print()
print(es_palindromo('1011'))
print(es_palindromo('python'))


# Ejercicio 211: Invertir una cadena de caracteres.
def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    return frase == frase[::-1]
print(es_palindromo('1001'))
print(es_palindromo('ataralarata'))
print(es_palindromo('Atar a la rata'))
print()
print(es_palindromo('1011'))
print(es_palindromo('python'))


# Ejercicio 212: Sumar filas y columnas de una matriz y crear una nueva matriz.
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
matriz = [
    [25, 69, 51, 26],
    [68, 35, 29, 54],
    [54, 57, 45, 63],
    [61, 68, 47, 59]
]
mostrar_matriz(matriz)
filas = len(matriz)
columnas = len(matriz[0])
for i in range(filas):
    suma = sum(matriz[i])
    matriz[i].append(suma)
print()
mostrar_matriz(matriz)
print()
nueva_fila = []
for j in range(columnas):
    suma = sum([fila[j] for fila in matriz])
    nueva_fila.append(suma)
nueva_fila.append(sum(nueva_fila))
matriz.append(nueva_fila)
mostrar_matriz(matriz)


# Ejercicio 213: Crear una función para calcular longitud de una cadena de caracteres sin usar len.
# Solución:
def calcular_longitud_cadena(cadena):
    """
    Calcula la longitud de una cadena de caracteres.
    """
    contador = 0
    for c in cadena:
        contador += 1
    return contador
texto = '¡Python es tremendo!'
print(len(texto))
print(calcular_longitud_cadena(texto))


# Ejercicio 214: Contar el número de ocurrencias por cada carácter de un texto.
from collections import Counter
def contador_ocurrencias(cadena):
    ocurrencias = {}
    for c in cadena:
        if c in ocurrencias.keys():
            ocurrencias[c] += 1
        else:
            ocurrencias[c] = 1
    return ocurrencias
texto = '¡Python es génial!'
c = Counter(texto)
print(c)
print()
print(contador_ocurrencias(texto))


# Ejercicio 215: Extraer los n caracteres extremos de una cadena de caracteres.
# ¡Python es tremendo!
# ¡Po!
# ¡Podo!
def extraer_caracteres_extremos(cadena, n=1):
    if n * 2 <= len(cadena):
        return cadena[:n] + cadena[-n:]
    else:
        return ''
texto = '¡Python es tremendo!'
print(extraer_caracteres_extremos(texto))
print(extraer_caracteres_extremos(texto, 2))
print(extraer_caracteres_extremos(texto, 3))
print(extraer_caracteres_extremos(texto, 4))
print(extraer_caracteres_extremos(texto, 30))


# Ejercicio 216: Sustituir por @ los caracteres que coincidan con el primer carácter excepto éste mismo.
# Solución:
# computición => computi@ión
# c, @omputa@ión
def sustituir_caracteres(cadena):
    primer_caracter = cadena[0]
    cadena = cadena.replace(primer_caracter, '@')
    return primer_caracter + cadena[1:]
texto = 'computición'
print(sustituir_caracteres(texto))
texto = 'elefante'
print(sustituir_caracteres(texto))


# Ejercicio 217: Alternar el segundo carácter entre dos palabras de tres letras.
# Solución:
# las los => los las
def intercambiar_caracteres(palabra1, palabra2):
    if len(palabra1) == 3 and len(palabra2) == 3:
        nueva_palabra1 = palabra1[0] + palabra2[1] + palabra1[2]
        nueva_palabra2 = palabra2[0] + palabra1[1] + palabra2[2]
        return nueva_palabra1, nueva_palabra2
    else:
        raise ValueError('Las palabras no son de 3 caracteres.')
print(('las', 'los'))
print(intercambiar_caracteres('las', 'los'))


# Ejercicio 218: Particionar una cadena por caracteres de límite de líneas.
# Solución:
texto = 'Python\nes tremendo\n\nLa versión más reciente\r\nes 3.8.0'
partes = texto.splitlines()
print(texto)
print()
print(partes)


# Ejercicio 219: Uso de la función format_map de la clase str.
datos = {'nombre': 'Edward Ortiz', 'email': 'edward@mail.com'}
resultado = 'Su nombre es: {nombre}. Su correo-e es: {email}'.format_map(datos)
print(resultado)


# Ejercicio 220: Encontrar la palabra más larga dentro de una lista de palabras.
def encontrar_palabra_mas_larga(palabras):
    palabra_longitud = []
    for p in palabras:
        palabra_longitud.append((len(p), p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]
palabras = ['JavaScript', 'Python', 'C++', 'PHP']
print(encontrar_palabra_mas_larga(palabras))


# Ejercicio 221: Remover el i-ésimo carácter de una cadena de caracteres.
# Python
def remover_i_esimo_caracter(palabra, i):
    izquierda = palabra[:i]
    derecha = palabra[i + 1:]
    return izquierda + derecha
texto = 'Python'
print(remover_i_esimo_caracter(texto, 2))
print(remover_i_esimo_caracter(texto, 3))
print(remover_i_esimo_caracter(texto, 4))
print(remover_i_esimo_caracter(texto, 5))
print(remover_i_esimo_caracter(texto, 10))


# Ejercicio 222: Intercambiar el primer y último carácter de una cadena de caracteres.
# Solución:
# Python => nythoP
def intercambiar_caracteres(cadena):
    return cadena[-1] + cadena[1:-1] + cadena[0]
texto = 'Python'
print(intercambiar_caracteres(texto))


# Ejercicio 223: Remover los caracteres ubicados en índices impares dentro de un texto.
# Análisis:
# Python => Pto
def remover_caracteres_impares(cadena):
    resultado = ''
    for i in range(len(cadena)):
        if i % 2 == 0:
            resultado += cadena[i]
    return resultado
texto = 'Python'
print(remover_caracteres_impares(texto))


# Ejercicio 224: Remover los caracteres ubicados en índices pares dentro de un texto.
# Análisis:
# Python -> yhn
def remover_caracteres_pares(palabra):
    resultado = []
    for i in range(len(palabra)):
        if i % 2 == 1:
            resultado.append(palabra[i])
    return ''.join(resultado)
texto = 'Python'
print(remover_caracteres_pares(texto))


# Ejercicio 225: Convertir cada palabra de una lista de palabras a mayúscula.
palabras = ['Python', 'java', 'c++', 'php', 'Perl']
palabras_mayus = list(map(str.upper, palabras))
print(palabras)
print(palabras_mayus)


# Ejercicio 226: Obtener las palabras únicas de un listado de palabras definido por el usuario.
entrada = input('Digite un grupo de palabras separadas por coma: ')
palabras = entrada.split(',')
print(palabras)
palabras_unicas = list(set(palabras))
print(palabras_unicas)


# Ejercicio 227: Diseñar e implementar una función para crear etiquetas HTML.
# Solución:
# <tag>CONTENIDO</tag>
# <span>Texto...</span>
# <p>Texto...</p>
def crear_etiqueta(etiqueta, contenido):
    return '<%s>%s</%s>' % (etiqueta, contenido, etiqueta)
print(crear_etiqueta('span', 'Python es tremendo'))
print(crear_etiqueta('p', 'Python es tremendo. Python es un lenguaje de programación.'))


# Ejercicio 228: Insertar una palabra en una posición específica de una cadena.
# Solución:
# "Python 3.8.0" => "Python versión 3.8.0"
def insertar_texto(cadena, texto, posicion):
    if posicion <= len(cadena):
        izquierda = cadena[:posicion]
        derecha = cadena[posicion + 1:]
        return '{} {} {}'.format(izquierda, texto, derecha)
    else:
        raise ValueError('La posición donde se quiere insertar el texto no existe.')
cadena = 'Python 3.8.0'
texto = 'versión'
posicion = 6
print(insertar_texto(cadena, texto, posicion))


# Ejercicio 229: Duplicar los n caracteres finales de una cadena de caracteres.
# Análisis:
# Python -> onon
def duplicar_ultimos_n_caracteres(cadena, n):
    if n <= len(cadena):
        return cadena[-n:] * 2
    else:
        raise ValueError('La cantidad de caracteres a duplicar sobrepasa la longitud de la cadena.')
cadena = 'Python'
print(duplicar_ultimos_n_caracteres(cadena, 2))
print(duplicar_ultimos_n_caracteres(cadena, 3)) # honhon
# print(duplicar_ultimos_n_caracteres(cadena, 20)) # Genera error


# Ejercicio 230: Uso de la función expandtabs de la clase str.
#Python\tversión\t3.8.0
#Python  versión 3.8.0
cadena = 'Python\tversión\t3.8.0'
print(cadena.expandtabs())


# Ejercicio 231: Obtener la cadena ubicada antes de un carácter específico.
url = 'https://ortizol.blogspot.com/ejercicios-python/aleatorios'
print(url.rsplit('/', 1)[0])
print(url.rsplit('-', 1)[0])


# Ejercicio 232: Invertir una cadena de caracteres con el método reversed.
texto = input('Escriba una cadena de texto: ')
print(texto)
texto_invertido = ''.join(reversed(texto))
print(texto_invertido)


# Ejercicio 233: Cambiar a mayúsculas un texto si hay al menos dos caracteres en mayúscula.
# Descripción: Cambiar a mayúsculas un texto si hay al menos dos caracteres en mayúscula en los primeros cuatro caracteres.
# Análisis:
# Python
# PYthon => PYTHON
def cambiar_mayusculas(cadena):
    if len(cadena) > 4:
        contador = 0
        for i in range(4):
            if cadena[i] == cadena[i].upper():
                contador += 1
        if contador >= 2:
            return cadena.upper()
        else:
            return cadena
    else:
        return cadena
texto = 'Python'
print(cambiar_mayusculas(texto))
texto = 'PyThon'
print(cambiar_mayusculas(texto))


# Ejercicio 234: Ordenar una cadena de caracteres de forma lexicográfica.
# Análisis:
# Python => hnoPty
def cadena_orden_lexicografico(cadena):
    return ''.join(sorted(cadena, key=str.upper))
texto = 'Python'
print(cadena_orden_lexicografico(texto))


# Ejercicio 235: Remover el carácter de nueva línea en una cadena de caracteres.
texto = 'Python es un lenguaje de programación\n'
print(texto, end='')
texto = texto.rstrip()
print(texto, end='')


# Ejercicio 236: Comprobar con str.startswith si una cadena inicia con texto específico.
texto = 'Python es un lenguaje de programación.'
print(texto.startswith('Python'))
print(texto.startswith('Python '))
print(texto.startswith('Python  '))
print(texto.startswith('python'))


# Ejercicio 237: Comprobar con str.endswith si una cadena termina con texto específico.
texto = 'Python versión 3.8.0'
print(texto.endswith('3.8.0'))
print(texto.endswith(' 3.8.0'))
print(texto.endswith('  3.8.0'))
print(texto.endswith('n 3.8.0'))
print(texto.endswith('N 3.8.0'))


# Ejercicio 238: Crear un algoritmo para implementar el cifrado César.
# Solución:
from string import ascii_lowercase, ascii_uppercase
def cifrado_cesar(texto, pasos):
    resultado = []
    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevo_indice])
        else:
            resultado.append(c)
    return ''.join(resultado)
texto = 'Python es tremendo'
print(cifrado_cesar(texto, 1))
print(cifrado_cesar(texto, 2))
print(cifrado_cesar(texto, 3))


# Ejercicio 239: Mostrar texto sobre un número de columnas específicas con textwrap.fill.
from textwrap import fill
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'
print(texto)
print()
print(fill(texto, width=50))


# Ejercicio 240: Remover indentación de un texto por medio de textwrap.dedent.
from textwrap import dedent
texto = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.
'''
print(texto)
texto_sin_indentacion = dedent(texto)
print()
print(texto_sin_indentacion)


# Ejercicio 241: Agregar un prefijo a cada línea de un texto con textwrap.indent.
from textwrap import dedent, indent, fill
texto = '   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'
print(texto)
print()
texto_sin_indentacion = dedent(texto)
texto_con_formato = fill(texto_sin_indentacion, width=60)
print(indent(texto_con_formato, '- '))


# Ejercicio 242: Agregar indentación a un texto con la función textwrap.fill.
from textwrap import dedent, fill
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'
texto = dedent(texto)
print(texto)
texto = fill(texto, initial_indent='', subsequent_indent=' ' * 4, width=50)
print()
print(texto)


# Ejercicio 243: Usar una cadena de formato para mostrar 3 decimales de un número real.
from math import e, pi
print(e)
print(pi)
print()
print('La constante de Euler con tres decimales: {:.3f}'.format(e))
print('La constante de Pi con tres decimales: {:.3f}'.format(pi))


# Ejercicio 244: Agregar el signo de un número en una cadena de formato.
from math import e, pi
print('Valor original de pi:', pi)
print('Pi con signo: {:+.5f}'.format(pi))
print()
print('Valor original de e:', e * -1)
print('e con signo: {:+.5f}'.format(e * -1))


# Ejercicio 245: Mostrar un número real sin decimales en una cadena de formato.
pi = 3.1415
print('Valor original de la constante pi:', pi)
print('La constante pi sin decimales: {:.0f}'.format(pi))


# Ejercicio 246: Crear una cadena de formato para mostrar valores porcentuales.
porcentaje = 0.3053
cadena_formato = 'El valor porcentual de {} es igual a {:.2%}'.format(porcentaje, porcentaje)
print(cadena_formato)


# Ejercicio 247: Justificar un valor numérico a la izquierda, centro y derecha de una cadena.
# Solución:
# 2050
# < : justifica a la izquierda
# ^ : justifica al centro
puntaje = 2050
print('Valor original de puntaje:', puntaje)
print('Puntaje justificado a la izquierda:')
print('{:<20}'.format(puntaje))
print('Puntaje justificado al centro:')
print('{:^20}'.format(puntaje))
print('Puntaje justificado a la derecha:')
print('{:20}'.format(puntaje))


# Ejercicio 248: Contar el número de ocurrencias de una subcadena de caracteres.
frase = 'Python es un lenguaje de programación. La versión más reciente de Python es 3.8.0. Python es un lenguaje de programación interpretado.'
contador_ocurrencias = frase.count('Python', 10)
print('Cantidad de ocurrencias: %i' % contador_ocurrencias)


# Ejercicio 249: Invertir o poner al revés una cadena de caracteres.
texto = 'Python es génial'
texto_invertido = ''.join(reversed(texto))
print(texto)
print(texto_invertido)


# Ejercicio 250: Remover un grupo de caracteres específicos de una cadena de caracteres.
# Solución:
# Python es tremendo => Pythn s trmnd
def remover_caracteres(cadena, caracteres):
    return ''.join(c for c in cadena if c not in caracteres)
texto = 'Python es tremendo'
print(remover_caracteres(texto, ['a', 'e', 'i', 'o', 'u']))
print(remover_caracteres(texto, 'aeiou'))


# Ejercicio 251: Obtener los caracteres que se repiten en una cadena.
# Solución:
from collections import defaultdict
texto = 'Python es un lenguaje de programación'
contador = defaultdict(int)
for c in texto:
    contador[c] += 1
for c in sorted(contador, key=contador.get, reverse=True):
    if contador[c] > 1:
        print('El carácter %s se repetir %i' % (c, contador[c]))


# Ejercicio 252: Imprimir los valores formateados para el área y el volumen de un cilindro.
area = 471.2389
volumen = 785.3981
print('El área del cilindro es igual {0:.{1}f}cm\u00b2.'.format(area, 2))
print('El volumen del cilindro es igual {0:.{1}f}cm\u00b3.'.format(volumen, 2))


# Ejercicio 253: Mostrar la posición de cada carácter en una cadena con enumerate.
cadena = 'Python 3.8.0'
for i, c in enumerate(cadena):
    print('Carácter: %s - Índice: %i' % (c, i))


# Ejercicio 254: Comprobar si una cadena de caracteres contiene todos los caracteres del alfabeto.
from string import ascii_lowercase
def validar_caracteres(cadena):
    return set(cadena) >= set(ascii_lowercase)
texto = 'The quick brown fox jumps over the lazy dgo'
print(validar_caracteres(texto))
texto = 'The quick brown fox jumps over the lazy cat'
print(validar_caracteres(texto))


# Ejercicio 255: Convertir una frase en una lista de palabras.
frase = 'Python es un lenguaje de programación interpretado'
palabras = frase.split()
print(palabras)
print(len(palabras))


# Ejercicio 256: Pasar a mínusculas los primeros n caracteres.
def poner_minusculas(cadena, n):
    return cadena[:n].lower() + cadena[n:]
texto = 'PYTHON ES GÉNIAL'
print(poner_minusculas(texto, 6))


# Ejercicio 257: Alternar los separadores de millares y decimales con maketrans y translate.
valor = '12.345,67' # 12,345.67
print(valor)
cambio = valor.maketrans
valor = valor.translate(cambio('.,', ',.'))
print(valor)


# Ejercicio 258: Obtener y contar las vocales que tiene una frase.
def obtener_vocales(frase):
    vocales = 'aeouiAEOUI'
    return set([c for c in frase if c in vocales])
texto = 'Python es genial'
print(obtener_vocales(texto))
print(len(obtener_vocales(texto)))


# Ejercicio 259: Particionar una cadena de caracteres por la última ocurrencia de un delimitador.
# Solución:
frase = 'Python,PHP,C#,C++,Java,JavaScript,Go'
# rsplit => right_split
lenguajes = frase.rsplit(',', 1)
print(lenguajes)
print()
lenguajes = frase.rsplit(',', 2)
print(lenguajes)


# Ejercicio 260: Encontrar el primer carácter no repetido en una cadena de caracteres.
# Análisis:
# Python es tremendo. Python v. 3.8.0
def primer_caracter_no_repetido(cadena):
    conteo = {}
    for c in cadena:
        if c in conteo:
            conteo[c] += 1
        else:
            conteo[c] = 1
    for c in conteo.keys():
        if conteo[c] == 1:
            return c
texto = 'Python es tremendo'
print(primer_caracter_no_repetido(texto))
texto = 'Python es tremendo. Python v. 3.8.0'
print(primer_caracter_no_repetido(texto))


# Ejercicio 261: Particionar una cadena de caracteres por la primera ocurrencia de un delimitador.
cadena = 'Python,Java,C++,PHP,C,Go,JavaScript'
partes = cadena.split(',', 1)
print(partes)
print(partes[0])


# Ejercicio 262: Generar todas las permutaciones con repetición posibles de una cadena.
from itertools import product
def permutaciones_repeticion(cadena, tamagnio):
    caracteres = list(cadena)
    permutaciones = []
    for c in product(caracteres, repeat=tamagnio):
        permutaciones.append(c)
    return permutaciones
texto = 'abc'
tamagnio = 3
print(permutaciones_repeticion(texto, tamagnio))
print()
print(permutaciones_repeticion(texto, 2))


# Ejercicio 263: Encontrar el primer carácter repetido de una cadena.
# Solución:
# Python => 0, P; 1, y; ...
def primer_caracter_repetido(cadena):
    for i, c in enumerate(cadena):
        if cadena[i + 1:].count(c) > 0:
            return c
    return None
cadena = 'Python es tremendo'
print(primer_caracter_repetido(cadena))
cadena = 'Python'
print(primer_caracter_repetido(cadena))


# Ejercicio 264: Encontrar el primer carácter repetido más cercano de una cadena.
# Solución:
# Python es tremendo
def caracter_repitido_cercano(cadena):
    auxiliar = []
    for c in cadena:
        if c in auxiliar:
            return c
        else:
            auxiliar.append(c)
    return None
texto = 'Python es tremendo'
print(caracter_repitido_cercano(texto))
print(caracter_repitido_cercano(texto) == ' ')


# Ejercicio 265: Encontrar la primera palabra repetida en una frase.
def primera_palabra_repetida(frase):
    auxiliar = set()
    for p in frase.split():
        if p in auxiliar:
            return p
        else:
            auxiliar.add(p)
    return None
cadena = 'Python es un lenguaje de programación. Python v. 3.8.0'
print(primera_palabra_repetida(cadena))
print()
cadena = 'Python es tremendo'
print(primera_palabra_repetida(cadena))
print()
cadena = 'Python es tremendo. Visual Studio Code es un editor liviano. Python es interpretado'
print(primera_palabra_repetida(cadena))


# Ejercicio 266: Encontrar la segunda palabra más repetida en una frase.
def segunda_palabra_repetida(frase):
    contador = {}
    palabras = frase.split()
    for p in palabras:
        if p in contador:
            contador[p] += 1
        else:
            contador[p] = 1
    contador = sorted(contador.items(), key=lambda item: item[1])
    return contador[-2]
cadena = 'Python es un lenguaje de programación. Python es un lenguaje interpretado. Python v. 3.8.0. Lenguaje de programación... es un'
print(segunda_palabra_repetida(cadena))


# Ejercicio 267: Remover todo el espacio de una cadena de caracteres.
def remover_espacio(cadena):
    return cadena.replace(' ', '')
url = '  https :// www.python. org'
print(url)
print(remover_espacio(url))


# Ejercicio 268: Mover el espacio de una cadena de caracteres al principio.
# Análisis:
# 'https  :/ /  www.python . org' => '       https://www.python.org'
def mover_espacio_al_frente(cadena):
    contador = cadena.count(' ')
    cadena = cadena.replace(' ', '')
    return ' ' * contador + cadena
texto = 'https  :/ /  www.python . org'
print(texto)
print(mover_espacio_al_frente(texto))


# Ejercicio 269: Obtener el carácter más recurrente de una cadena de caracteres.
def caracter_mas_recurrente(frase):
    contador = [0] * 256
    for c in frase:
        contador[ord(c)] += 1
    maximo = -1
    caracter = ''
    for c in frase:
        if maximo < contador[ord(c)]:
            maximo = contador[ord(c)]
            caracter = c
    return caracter
cadena = 'aabbxxxxyy'
print(caracter_mas_recurrente(cadena))


# Ejercicio 270: Poner en mayúscula el primer y último carácter de cada palabra en una frase.
# 'python es genial' => 'PythoN ES GeniaL'
def mayusculas_primer_ultimo_caracter(frase):
    resultado = ''
    for p in frase.split():
        resultado += p[0].upper() + p[1:-1] + p[-1].upper() + ' '
    return resultado
texto = 'python es genial'
print(texto)
print(mayusculas_primer_ultimo_caracter(texto))


# Ejercicio 271: Remover todos los caracteres duplicados de una cadena con fromKeys.
from collections import OrderedDict
def remover_caracteres_duplicados(frase):
    return ''.join(OrderedDict.fromkeys(frase))
texto = 'Python es un lenguaje de programación.'
print(texto)
print(remover_caracteres_duplicados(texto))


# Ejercicio 272: Sumar los dígitos que aparezcan en una cadena de caracteres.
# Solución:
# 'Python v. 3.8.0' => 11
def sumar_digitos_cadena(frase):
    suma = 0
    for c in frase:
        if c.isdigit():
            suma += int(c)
    return suma
frase = 'Python v. 3.8.0'
print(frase)
print(sumar_digitos_cadena(frase))
frase = 'PHP v. 7.1.2'
print(frase)
print(sumar_digitos_cadena(frase))


# Ejercicio 273: Remover los ceros redundantes de una dirección IP.
# Solución:
# 192.168.001.072 => 192.168.1.72
# 192.168.070.13 => 192.168.70.13
def remover_ceros_redundantes(ip):
    nueva_ip = '.'.join([str(int(o)) for o in ip.split('.')])
    return nueva_ip
direccion_ip = '192.168.001.072'
print(direccion_ip)
print(remover_ceros_redundantes(direccion_ip))
print()
direccion_ip = '192.168.070.13'
print(direccion_ip)
print(remover_ceros_redundantes(direccion_ip))


# Ejercicio 274: Computar la cantidad máxima de ceros consecutivos en un número binario.
# Análisis:
# 1001100001 => 4
# 100010001000 => 3
def cantidad_maxima_ceros_consecutivos(binario):
    return max(map(len, binario.split('1')))
numero_binario = '1001100001'
print(numero_binario)
print(cantidad_maxima_ceros_consecutivos(numero_binario))
print()
numero_binario = '100010001000'
print(numero_binario)
print(cantidad_maxima_ceros_consecutivos(numero_binario))


# Ejercicio 275: Obtener los caracteres comunes de dos cadenas de caracteres.
# Solución:
# Cadena 1: 'Python' - Cadena 2: PHP => P
# Cadena 1: 'JavaScript' - Cadena 2: Java => Java
# Cadena 1: 'Python' - Cadena 2: C++ => '' (None)
from collections import Counter
def caracteres_comunes(cadena_1, cadena_2):
    contador_1 = Counter(cadena_1)
    contador_2 = Counter(cadena_2)
    comunes = contador_1 & contador_2
    if len(comunes) == 0:
        return None
    comunes = list(comunes.elements())
    comunes = sorted(comunes)
    return comunes
texto_1 = 'Python'
texto_2 = 'PHP'
print(caracteres_comunes(texto_1, texto_2))
print()
texto_1 = 'JavaScript'
texto_2 = 'Java'
print(caracteres_comunes(texto_1, texto_2))
print()
texto_1 = 'Python'
texto_2 = 'C++'
print(caracteres_comunes(texto_1, texto_2))


# Ejercicio 276: Terminar la ejecución de un script Python con la función exit.
try:
    cadena = input('Digite un número: ')
    numero = int(cadena)
    exit(0)
except ValueError as e:
    print('Error:', e)
    exit(1)

# Ejercicio 277: Encontrar la subcadena mínima que contenga otra cadena de caracteres.
import collections
def subcadena_minima(frase, cadena):
    contador = collections.Counter(frase)
    longitud = len(cadena)
    i = 0
    p = 0
    q = 0
    for j, c in enumerate(frase, 1):
        longitud -= contador[c] > 0
        contador[c] -= 1
        if not longitud:
            while i < q and contador[frase[i]] < 0:
                contador[frase[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return frase[p+1:q+1]
print(subcadena_minima('caballo', 'aba'))


# Ejercicio 278: Mecanismos para clonar o copiar todos los elementos de una lista.
# list:
numeros = [2, 3, 5, 7, 11]
numeros_copia = list(numeros)
print(numeros)
print(numeros_copia)
print(numeros_copia is numeros)
numeros_2 = numeros
print(numeros_2 is numeros)
print()
# slicing:
numeros_copia = numeros[:]
print(numeros_copia)
print(numeros_copia is numeros)
print()
# Lista de comprensión:
numeros_copia = [numero for numero in numeros]
print(numeros_copia)
print(numeros_copia is numeros)


# Ejercicio 279: Uso del método casefold de la clase str.
aleman = 'der Fluß'
print(aleman.lower())
print(aleman.casefold())
print(aleman.casefold() == 'der fluss')


# Ejercicio 280: Crear una función básica para remover el i-ésimo carácter de una cadena.
def remover_caracter(cadena, i):
    resultado = ''
    for j in range(len(cadena)):
        if j != i:
            resultado += cadena[j]
    return resultado
frase = 'Python es tremendo!'
posicion = 3
print(remover_caracter(frase, posicion))


# Ejercicio 281: Contar los caracteres de una frase que ocupan la misma posición del alfabeto.
# Análisis:
# abril
# 1 + 1 = 2
def conteo_caracteres_alfabeto(frase):
    contador = 0
    for i in range(len(frase)):
        if (i == ord(frase[i]) - ord('A')) or (i == ord(frase[i]) - ord('a')):
            contador += 1
    return contador
frase = 'abril'
print(conteo_caracteres_alfabeto(frase))
frase = 'algoritmo'
print(conteo_caracteres_alfabeto(frase))


# Ejercicio 282: Crear función para encontrar la palabra más corta en una frase.
def palabra_mas_corta(frase):
    palabras = frase.split()
    mas_corta = palabras[0]
    for i in range(1, len(palabras)):
        if len(mas_corta) > len(palabras[i]):
            mas_corta = palabras[i]
    return mas_corta
frase = 'Python es un lenguaje de programación'
print(palabra_mas_corta(frase))
frase = "Python PHP C# JavaScript Java"
print(palabra_mas_corta(frase))


# Ejercicio 283: Crear función para encontrar la palabra más larga en una frase.
def palabra_mas_larga(frase):
    palabras = frase.split()
    mas_larga = palabras[0]
    for i in range(1, len(palabras)):
        if len(mas_larga) < len(palabras[i]):
            mas_larga = palabras[i]
    return mas_larga
frase = 'Python es un lenguaje de programación'
print(palabra_mas_larga(frase))
frase = 'Python JavaScript C# Java PHP'
print(palabra_mas_larga(frase))


# Ejercicio 284: Contar el número de caracteres de una cadena en un ciclo while.
def contar_caracteres(cadena):
    contador = 0
    while cadena[contador:]:
        contador += 1
    return contador
frase = 'Python v. 3.8.0'
print(len(frase))
print(contar_caracteres(frase))


# Ejercicio 285: Crear un objeto Python a partir de datos en formato JSON.
import json
datos_json = '{"nombre": "Edward", "apellido": "Ortiz", "edad": 29}'
objeto = json.loads(datos_json)
print(objeto)
print(objeto['nombre'])
print(objeto['apellido'])
print(objeto['edad'])
print()
print(type(objeto))


# Ejercicio 286: Convertir un objeto Python a datos en formato JSON con el módulo json.
import json
objeto = {'nombre': 'Edward', 'apellido': 'Ortiz', 'edad': 29}
print(type(objeto))
datos_json = json.dumps(objeto)
print(datos_json)
print(type(datos_json))


# Ejercicio 287: Convertir una lista de cadenas a formato JSON con el módulo json.
import json
lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'PHP']
print(lenguajes)
print(type(lenguajes))
datos_json = json.dumps(lenguajes)
print(datos_json)
print(type(datos_json))


# Ejercicio 288: Ordenar un diccionario para generar datos en formato JSON con dumps.
import json
objeto = {'7': 5, '9': 12, '1': 3, '2': 5}
print(objeto)
resultado = json.dumps(objeto, sort_keys=True, indent=4)
print(resultado)


# Ejercicio 289: Convertir una lista en formato JSON en una lista Python con loads.
import json
arreglo_json = '["Python", "Java", "PHP", "C#", "PHP"]'
lista = json.loads(arreglo_json)
print(type(lista))
print(lista)


# Ejercicio 290: Leer un archivo en formato JSON por medio de la función json.load().
import json
with open('Parte001/paises_capitales.json') as f:
    paises = json.load(f)
print(type(paises))
print(len(paises))
print(paises)
print()
print(paises[0])
print(type(paises[0]))


# Ejercicio 291: Crear un nuevo archivo JSON a partir de uno ya existente.
import json
with open('Parte001/paises_capitales.json') as f:
    paises_capitales = json.load(f)
print(len(paises_capitales))
print(paises_capitales[0])
for p in paises_capitales:
    del p['city']
print()
print(len(paises_capitales))
print(paises_capitales[0])
with open('Parte001/paises.json', 'w') as f:
    json.dump(paises_capitales, f, indent=4)


# Ejercicio 292: Codificar un número complejo como datos en formato JSON usando dumps.
import json
def codificar_numero_complejo(complejo):
    if isinstance(complejo, complex):
        return [complejo.real, complejo.imag]
    else:
        raise TypeError('{} el valor no puede ser convertido a complejo'.format(repr(complejo)))
numero_complejo = 3 + 6j
complejo_json = json.dumps(numero_complejo, default=codificar_numero_complejo)
print(complejo_json)


# Ejercicio 293: Decodificar un número complejo en formato JSON a objeto Python.
import json
def decodificar_numero_complejo(objeto):
    return complex(objeto['real'], objeto['imag'])
objeto = json.loads('{"real": 3, "imag": 6}', object_hook=decodificar_numero_complejo)
print(type(objeto))
print(objeto)


# Ejercicio 294: Representación de None en formato de datos JSON.
import json
persona = {'nombre': 'Edward', 'apellido': 'Ordoñez', 'edad': 29, 'email': None}
print(persona)
persona_json = json.dumps(persona)
print(persona_json)


# Ejercicio 295: Crear una función para sumar todos los elementos de una lista.
def sumar_lista(lista):
    """
    Suma un conjunto de valores en una lista.
    """
    suma = 0
    for numero in lista:
        suma += numero
    return suma
numeros = [1, 2, 3, 4, 5]
print(sumar_lista(numeros))
numeros = [1.1, 2.2, 3.3, 4.4, 5.5]
print(sumar_lista(numeros))


# Ejercicio 296: Crear una función para multiplicar todos los elementos de una lista.
def multiplicar_lista(numeros):
    """
    Multiplica un conjunto de valores numéricos.
    """
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto
numeros = [1, 2, 3, 4, 5]
print(multiplicar_lista(numeros))
numeros = [1.1, 2.2, 3.3, 4.4, 5.5]
print(multiplicar_lista(numeros))


# Ejercicio 297: Crear función para encontrar el valor máximo en una lista de valores.
def maximo(valores):
    mayor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor
numeros = [7, 11, 2, 0, 13, 5, -1, -8]
print(maximo(numeros))


# Ejercicio 298: Crear función para encontrar el valor mínimo en una lista de valores.
def valor_minimo(valores):
    """
    Calcular el valor mínimo de una lista de valores numéricos.
    """
    minimo = valores[0]
    for i in range(1, len(valores)):
        if valores[i] < minimo:
            minimo = valores[i]
    return minimo
numeros = [13, 11, 23, 2, 5, 29, 7]
print(valor_minimo(numeros))
numeros = [5.5, 3.3, 9.7, 1.7, 9.3, 17.11]
print(valor_minimo(numeros))


# Ejercicio 299: Crear función para contar el número de cadenas con longitud 5 o mayor.
def contar_cadenas(cadenas):
    contador = 0
    for c in cadenas:
        if len(c) >= 5:
            contador += 1
    return contador
palabras = ['Python', 'C#', 'C++', 'JavaScript', 'Java', 'PHP']
print(contar_cadenas(palabras))


# Ejercicio 300: Crear función para ordenar un grupo de tuplas a partir del último elemento.
def ordenar_lista_tuplas(tuplas):
    return sorted(tuplas, key=lambda t: t[-1])
listado = [(2, 7), (3, 11), (5, 2), (11, 9)]
resultado = ordenar_lista_tuplas(listado)
print(listado)
print(resultado)


# Ejercicio 301: Crear función para remover los duplicados de una lista de cadenas.
def remover_duplicados(cadenas):
    """
    Remueve los duplicados de una lista de cadenas.
    """
    no_duplicados = []
    for c in cadenas:
        if c not in no_duplicados:
            no_duplicados.append(c)
    return no_duplicados
lenguajes = ['Python', 'Java', 'JavaScript', 'Java', 'Java', 'python', 'C++', 'C', 'C++']
print(lenguajes)
resultado = remover_duplicados(lenguajes)
print(resultado)


# Ejercicio 302: Crear una función personalizada para comprobar si una lista está vacía.
def lista_vacia(lista):
    return not lista
numeros = [2, 3, 5]
print(lista_vacia(numeros))
numeros.pop()
print(lista_vacia(numeros))
numeros.pop()
print(lista_vacia(numeros))
numeros.pop()
print(lista_vacia(numeros))
print()
print(lista_vacia([]))


# Ejercicio 303: Crear función para obtener los elementos pares de una lista.
def pares(numeros):
    numeros_pares = []
    for n in numeros:
        if n % 2 == 0:
            numeros_pares.append(n)
    return numeros_pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = pares(numeros)
print(numeros)
print(resultado)


# Ejercicio 304: Crear función para obtener las palabras de n longitud.
def palabras_n_longitud(palabras, n):
    resultado = []
    for p in palabras:
        if len(p) == n:
            resultado.append(p)
    return resultado
lenguajes = ['Python', 'Java', 'C++', 'C', 'JavaScript', 'PHP']
longitud = 3
print(palabras_n_longitud(lenguajes, longitud))


# Ejercicio 305: Crear función básica para comprobar si 2 listas tienen un valor en común.
def listas_elemento_comun(lista_1, lista_2):
    for v1 in lista_1:
        for v2 in lista_2:
            if v1 == v2:
                return True
    return False
numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [3, 9, 12, 6, 18]
print(listas_elemento_comun(numeros_1, numeros_2))
numeros_3 = [-5, -4, -3]
print(listas_elemento_comun(numeros_1, numeros_3))


# Ejercicio 306: Remover elementos de una lista que se hallen en índices específicos.
lenguajes = ['Python', 'JavaScript', 'C', 'Java', 'C++', 'PHP', 'C#']
print(lenguajes)
indices = (2, 4, 6)
resultado = [lenguajes[i] for i in range(len(lenguajes)) if i not in indices]
print(resultado)


# Ejercicio 307: Crear un arreglo 3D con dimensiones 6x3x4 y llenar con asteriscos.
arreglo_3d = [[['*' for k in range(4)] for j in range(3)] for i in range(6)]
print(arreglo_3d)


# Ejercicio 308: Obtener los pares de un grupo de números usando una lista de comprensión.
numeros = list(range(1, 11))
print(numeros)
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Ejercicio 309: Obtener los impares de un grupo de números usando una lista de comprensión.
numeros = list(range(1, 11))
print(numeros)
impares = [numero for numero in numeros if numero % 2 == 1]
print(impares)


# Ejercicio 310: Aleatorizar un arreglo por medio de la función random.shuffle().
from random import shuffle
lenguajes = ['Python', 'C#', 'JavaScript', 'Java', 'C++', 'PHP']
print(lenguajes)
shuffle(lenguajes)
print(lenguajes)


# Ejercicio 311: Generar los números cuadrados para los valores 1 a 30.
# Descripción: Generar los números cuadrados para los valores 1 a 30 y obtener los n primeros y n últimos cuadrados.
def generar_cuadrados(n):
    if 2 * n <= 30:
        cuadrados = [i ** 2 for i in range(1, 31)]
        return cuadrados[:n] + cuadrados[-n:]
    else:
        raise ValueError('n no debe ser mayor a 2*n')
resultado = generar_cuadrados(5)
print(resultado)


# Ejercicio 312: Excluir los n primeros números cuadrados para los valores 1 a 30.
def excluir_cuadrados(n):
    if n <= 30:
        cuadrados = [i**2 for i in range(1, 31)]
        return cuadrados[n:]
    raise ValueError('n no puede ser mayor a 30')
print(excluir_cuadrados(5))


# Ejercicio 313: Excluir los n últimos números cuadrados para los valores 1 a 30.
def excluir_cuadrados(n):
    if n <= 30:
        cuadrados = [i**2 for i in range(1, 31)]
        return cuadrados[:-n]
    raise ValueError('n no debe ser mayor a 30')
print(excluir_cuadrados(5))


# Ejercicio 314: Generar las permutaciones para una lista de 3 valores numéricos.
from itertools import permutations
numeros = [1, 2, 3]
permutaciones = list(permutations(numeros))
print(permutaciones)


# Ejercicio 315: Calcular la diferencia de elementos entre dos listas.
numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = [1, 2, 7, 5]
diferencia = set(numeros_1) - set(numeros_2)
print(diferencia)
print()
diferencia = set(numeros_2) - set(numeros_1)
print(diferencia)


# Ejercicio 316: Acceder a los índices y valores de una lista con la función enumerate.
lenguajes = ['Python', 'JavaScript', 'C++', 'PHP', 'Java']
for indice, valor in enumerate(lenguajes):
    print('Índice: {} - Valor: {}'.format(indice, valor))


# Ejercicio 317: Convertir una lista de caracteres en una cadena de caracteres con join().
# ['P', 'y', 't', 'h', 'o', 'n'] => 'Python'
caracteres = ['P', 'y', 't', 'h', 'o', 'n']
resultado = ''.join(caracteres)
print(resultado)


# Ejercicio 318: Usar list.index() para encontrar el índice de un elemento en una lista.
lenguajes = ['Python', 'C#', 'PHP', 'C++', 'JavaScript', 'C', 'Java']
indice = lenguajes.index('JavaScript')
print(indice)
indice = lenguajes.index('Python')
print(indice)
print()
try:
    indice = lenguajes.index('python')
    print(indice)
except ValueError as e:
    print('ERROR:', e)


# Ejercicio 319: Aplanar una lista de listas por medio de la función itertools.chain().
# [[1, 2, 3], [4, 5], [6, 7, 8], [9]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]
from itertools import chain
lista = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]
lista_aplanada = list(chain(*lista))
print(lista)
print(lista_aplanada)


# Ejercicio 320: Unir o concatenar dos listas por medio del operador suma sobrecargado.
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
# +
lista_3 = lista_1 + lista_2
print(lista_1)
print(lista_2)
print(lista_3) # [1, 2, 3, 4, 5, 6]
print()
lista_4 = lista_2 + lista_1
print(lista_4) # [4, 5, 6, 1, 2, 3]


# Ejercicio 321: Seleccionar de forma aleatoria un elemento de una lista con random.choice().
from random import choice
lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'PHP', 'C#']
print(lenguajes)
lenguaje_aleatorio = choice(lenguajes)
print(lenguaje_aleatorio)
print()
for _ in range(10):
    print(choice(lenguajes))


# Ejercicio 322: Comprobar si dos listas son circularmente idénticas usando map() y join().
# [10 10 10 0 0] * 2 = [10 10 10 0 0 0 10 10 10 0 0 0]
def listas_circularmente_identicas(lista_1, lista_2):
    return ' '.join(map(str, lista_2)) in ' '.join(map(str, lista_1 * 2))
lista_1 = [10, 10, 0, 0, 10]
lista_2 = [10, 10, 10, 0, 0]
print(listas_circularmente_identicas(lista_1, lista_2))
lista_3 = [3, 10, 10, 0, 0]
print(listas_circularmente_identicas(lista_1, lista_3))


# Ejercicio 323: Encontrar el segundo número más pequeño en una lista.
def segundo_menor(numeros):
    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None
        if len(numeros) == 2 and numeros[0] == numeros[1]:
            return numeros[0]
        duplicados = set()
        unicos = []
        for n in numeros:
            if n not in duplicados:
                duplicados.add(n)
                unicos.append(n)
        unicos.sort()
        return unicos[1]
    raise TypeError('El parámetro numeros debe ser una lista')
numeros = [1, 3, 3, 7, 9, 11, 13, -5, 0, -1, 8, 12, 16, -5, -5]
print(segundo_menor(numeros))


# Ejercicio 324: Encontrar el segundo número más grande en una lista.
def segundo_mayor(numeros):
    if isinstance(numeros, list):
        if len(numeros) < 2:
            return None
        if len(numeros) == 2 and numeros[0] == numeros[1]:
            return None
        duplicados = set()
        unicos = []
        for n in numeros:
            if n not in duplicados:
                duplicados.add(n)
                unicos.append(n)
        unicos.sort()
        return unicos[-2]
    raise TypeError('El parámetro numeros debe ser una lista')
numeros = [1, 3, 3, 7, 9, 11, 13, -5, 0, -1, 8, 12, 16, -5, -5, 16, 16]
print(segundo_mayor(numeros))


# Ejercicio 325: Crear función para obtener los elementos únicos de una lista.
def valores_unicos(lista):
    return list(set(lista))
numeros = [2, 3, 3, 5, 7, 0, 0, 1, 11, 13, 13, 13]
resultado = valores_unicos(numeros)
print(numeros)
print(resultado)


# Ejercicio 326: Usar la clase Counter para calcular la frecuencia de elementos de una lista.
from collections import Counter
lenguajes = ['Python', 'C', 'C++', 'C', 'C', 'Python', 'Java', 'Java', 'C++', 'JavaScript', 'Java', 'Python', 'Java']
contador = Counter(lenguajes)
print(lenguajes)
print(contador)


# Ejercicio 327: Crear función para computar la cantidad de elementos en un rango de valores.
def contar_elementos_rango(valores, limite_inferior, limite_superior):
    contador = 0
    for v in valores:
        if limite_inferior <= v <= limite_superior:
            contador += 1
    return contador
numeros = list(range(1, 11))
print(numeros)
resultado = contar_elementos_rango(numeros, 4, 7)
print(resultado)
print()
caracteres = ['a', 'b', 'c', 'c', 'c', 'd', 'e', 'f']
resultado = contar_elementos_rango(caracteres, 'b', 'd')
print(caracteres)
print(resultado)


# Ejercicio 328: Comprobar si una lista contiene o no una sublista.
def es_sublista(lista, sublista):
    if len(sublista) == 0:
        return True
    if lista == sublista:
        return True
    if len(sublista) > len(lista):
        return False
    for v in sublista:
        if v not in lista:
            return False
    return True
lista_1 = [1, 2, 3, 4]
lista_2 = [3, 4]
print(es_sublista(lista_1, lista_2))
lista_3 = [3, 4, 5]
print(es_sublista(lista_1, lista_3))
lista_4 = [1, 2, 3, 4, 5]
print(es_sublista(lista_1, lista_4))
print(es_sublista(lista_1, []))


# Ejercicio 329: Generar todas las sublistas posibles de una lista de valores con combinations.
from itertools import combinations
def generar_sublistas(lista):
    sublistas = []
    for i in range(0, len(lista) + 1):
        sublista = [list(c) for c in combinations(lista, i)]
        if len(sublista) > 0:
            sublistas.extend(sublista)
    return sublistas
numeros = [1, 2, 3, 4, 5]
resultado = generar_sublistas(numeros)
print(numeros)
print(resultado)
print()
lenguajes = ['Python', 'C++', 'PHP', 'C#', 'Java']
resultado = generar_sublistas(lenguajes)
print(lenguajes)
print(resultado)


# Ejercicio 330: Usar el método de Criba de Eratóstenes para generar números primos hasta n.
def criba_eratostenes(n):
    primos = []
    no_primos = []
    for i in range(2, n + 1):
        if i not in no_primos:
            primos.append(i)
            for j in range(i * i, n + 1, i):
                no_primos.append(j)
    return primos
print(criba_eratostenes(120))
print(len(criba_eratostenes(120)))


# Ejercicio 331: Generar lista con caracteres alternantes y valores numéricos incrementales.
# [a, b]
# n
# [a1, b1, a2, b2, a3, b3,..., an, bn]
def generar_lista_alternante(caracteres, n):
    lista = ['{}{}'.format(c, i) for i in range(1, n + 1) for c in caracteres]
    return lista
caracteres = ['a', 'b']
n = 10
resultado = generar_lista_alternante(caracteres,  n)
print(resultado)


# Ejercicio 332: Generar un identificador único y variable para números y cadenas.
numero = 100
identificador = format(id(numero), 'x')
print(identificador)
print()
cadena = 'Python'
identificador = format(id(cadena), 'x')
print(identificador)


# Ejercicio 333: Crear función para obtener los elementos cómunes de dos listas.
def elementos_comunes(lista_1, lista_2):
    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)
    return list(conjunto_1 & conjunto_2)
numeros_1 = [1, 2, 2, 3, 4, 5, 6]
numeros_2 = [3, 4, 7, 9, 10]
resultado = elementos_comunes(numeros_1, numeros_2)
print(resultado)


# Ejercicio 334: Cambiar de posición cada n-ésimo elemento con el elemento n+1.
# [1, 2, 3, 4, 5, 6] => [2, 1, 4, 3, 6, 5]
from itertools import chain, zip_longest
def cambiar_posiciones(lista):
    return list(chain.from_iterable(zip_longest(lista[1::2], lista[::2])))
numeros = [1, 2, 3, 4, 5, 6]
resultado = cambiar_posiciones(numeros)
print(numeros)
print(resultado)
print()
numeros = [1, 2, 3]
resultado = cambiar_posiciones(numeros)
print(numeros)
print(resultado)


# Ejercicio 335: Crear un número entero único a partir de la unión de un listado de números.
# [1, 2, 3, 4, 5] => 12345
def union_listado_enteros(numeros):
    concatenacion = ''.join(map(str, numeros))
    return int(concatenacion)
numeros = [1, 2, 3, 4, 5]
resultado = union_listado_enteros(numeros)
print(numeros)
print(resultado)


# Ejercicio 336: Ordenar un grupo de palabras de forma ascendente por el último carácter.
def ordenar_palabras(palabras):
    return sorted(palabras, key=lambda p: p[-1])
lenguajes = ['Python', 'PHP', 'Java', 'JavaScript', 'C#', 'C++']
resultado = ordenar_palabras(lenguajes)
print(lenguajes)
print(resultado)


# Ejercicio 337: Crear un diccionario de n listas vacías.
def crear_diccionario_listas(n):
    diccionario = {}
    for i in range(1, n + 1):
        diccionario[i] = []
    return diccionario
resultado = crear_diccionario_listas(10)
print(resultado)


# Ejercicio 338: Computar la diferencia de elementos de dos listas de cadenas de caracteres.
lenguajes_1 = ['Python', 'C++', 'Java', 'C#']
lenguajes_2 = ['C#', 'PHP', 'JavaScript', 'C']
resultado = set(lenguajes_1).difference(set(lenguajes_2))
print(resultado)
print()
resultado = set(lenguajes_2).difference(set(lenguajes_1))
print(resultado)


# Ejercicio 339: Particionar una lista y guardar las partes en variables.
colores = [('Rojo', 'RGB(255, 0, 0)', '#FF0000'), ('Verde', 'RGB(0, 255, 0)', '#00FF00'), ('Azul', 'RGB(0, 0, 255)', '#0000FF')]
rojo, verde, azul = colores
print(colores)
print(rojo)
print(verde)
print(azul)


# Ejercicio 340: Crear una lista con 5 sublistas que contengan números consecutivos.
resultado = [[5*i + j for j in range(1, 6)] for i in range(5)]
print(resultado)


# Ejercicio 341: Convertir un listado de tuplas a una única lista ordenada.
puntos = [(1, 2), (3, 4), (6, 7), (5, 4), (13, 11), (-1, -2), (0, 0), (5, 19)]
print(puntos)
conjunto = set().union(*puntos)
print(conjunto)
resultado = sorted(conjunto)
print(resultado)


# Ejercicio 342: Usar notación de slicing para seleccionar las posiciones pares de una lista.
numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
resultado = numeros[::2]
print(numeros)
print(resultado)
print()
lenguajes = ['Python', 'C++', 'JavaScript', 'C', 'Java', 'PHP']
resultado = lenguajes[::2]
print(lenguajes)
print(resultado)


# Ejercicio 343: Agregar un nuevo elemento antes de cada elemento de una lista.
# ['Rojo', 'Verde', 'Azul'] => ['c', 'Rojo', 'c', 'Verde', 'c', 'Azul']
def agregar_elemento_lista(lista, caracter):
    return [valor for e in lista for valor in (caracter, e)]
colores = ['Rojo', 'Verde', 'Azul']
resultado = agregar_elemento_lista(colores, 'c')
print(colores)
print(resultado)


# Ejercicio 344: Imprimir cada sublista de una lista en una nueva línea.
lenguajes = [['Python'], ['JavaScript'], ['Java'], ['PHP'], ['C#']]
resultado = '\n'.join([str(sublista) for sublista in lenguajes])
print(lenguajes)
print()
print(resultado)


# Ejercicio 345: Convertir una lista en una lista de diccionarios.
nombres_colores = ['Blanco', 'Negro', 'Rojo', 'Verde', 'Azul']
codigos_colores = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF']
colores = [{'nombre': n, 'codigo': c} for n, c in zip(nombres_colores, codigos_colores)]
print(colores)


# Ejercicio 346: Ordenar una lista de diccionarios anidados por medio de su valor.
productos = [{'producto': {'valor': 1000}}, {'producto': {'valor': 3000}}, {'producto': {'valor': 2000}}]
print(productos)
print()
productos.sort(key=lambda p: p['producto']['valor'], reverse=True)
print(productos)


# Ejercicio 347: Particionar una lista en sublistas cada n-ésimo elemento.
# Análisis:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# => [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]
from string import ascii_lowercase
def particionar_lista(lista, n):
    return [lista[i*n:i*n+n] for i in range(n)]
print(ascii_lowercase)
az = list(ascii_lowercase)
print(az)
print()
resultado = particionar_lista(az, 5)
print(resultado)


# Ejercicio 348: Calcular la diferencia de dos listas usando la clase Counter.
from collections import Counter
lenguajes_1 = ['Python', 'C#', 'JavaScript', 'PHP']
lenguajes_2 = ['C++', 'Python', 'Java', 'C', 'Go']
contador_1 = Counter(lenguajes_1)
contador_2 = Counter(lenguajes_2)
print(contador_1)
print(contador_2)
print()
resultado = contador_1 - contador_2
print(resultado)
print()
resultado = contador_2 - contador_1
print(resultado)


# Ejercicio 349: Crear un contador infinito con la función count() de itertools.
from itertools import count
contador = count()
print(type(contador))
while True:
    print(next(contador))


# Ejercicio 350: Concatenar los elementos de una lista por un carácter específico.
def concatenar_lista(lista, caracter):
    if isinstance(lista, list):
        if isinstance(caracter, str):
            return caracter.join(map(str, lista))
        raise TypeError('El parámetro caracter debe ser una cadena de caracteres (str).')
    raise TypeError('El parámetro lista debe ser una lista.')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = concatenar_lista(numeros, '/')
print(resultado)


# Ejercicio 351: Remover diccionarios de una lista cuya llave sea igual a un valor dado.
productos = [{'nombre': 'Teclado', 'categoria': 'Periférico'}, {'nombre': 'Mouse', 'marca': 'Logitech'}, {'nombre': 'Parlantes', 'categoria': 'Periférico'}]
print(productos)
llave = 'categoria'
resultado = [p for p in productos if llave not in p.keys()]
print()
print(resultado)


# Ejercicio 352: Convertir una cadena que representa una lista en un objeto list de Python.
import ast
lenguajes = "['Python', 'JavaScript', 'C#', 'C++', 'PHP']"
print(type(lenguajes))
print(isinstance(lenguajes, list))
print(isinstance(lenguajes, str))
print()
resultado = ast.literal_eval(lenguajes)
print(type(resultado))
print(isinstance(resultado, list))
print(isinstance(resultado, str))
print()
print(lenguajes)
print(resultado)


# Ejercicio 353: Comprobar si todas las cadenas de una lista son iguales a una cadena dada.
lenguajes = ['Python', 'Python', 'Python', 'Python']
cadena = 'Python'
resultado = all(c == cadena for c in lenguajes)
print(resultado)
print()
lenguajes.append('Java')
resultado = all(c == cadena for c in lenguajes)
print(resultado)


# Ejercicio 354: Reemplazar el último elemento de una lista por los elementos de otra lista.
# [1, 2, 3, 4, 5]
# [6, 7, 8]
# => [1, 2, 3, 4, 6, 7, 8]
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8]
print(lista_a)
print(lista_b)
print()
lista_a[-1:] = lista_b
print(lista_a)


# Ejercicio 355: Convertir una cadena que representa un diccionario en un objeto dict.
import ast
persona = "{'nombre': 'Oliva', 'email': 'oliva@mail.co', 'edad': 37}"
print(type(persona))
print(isinstance(persona, dict))
print(isinstance(persona, str))
print()
resultado = ast.literal_eval(persona)
print(type(resultado))
print(isinstance(resultado, dict))
print(isinstance(resultado, str))
print()
print(persona)
print(resultado)


# Ejercicio 356: Encontrar la tupla en una lista cuyo valor en el segundo índice es menor.
def tupla_menor(lista):
    return min(lista, key=lambda t: (t[1], -t[0]))
puntos = [(7, 3), (11, 1), (5, 3), (2, 7), (-2, -4), (0, 0)]
resultado = tupla_menor(puntos)
print(resultado)


# Ejercicio 357: Generar una lista de diccionarios vacíos con una lista de comprensión.
n = 5
diccionarios_vacios = [{} for _ in range(n)]
print(diccionarios_vacios)


# Ejercicio 358: Imprimir el contenido de una lista en la función print().
lenguajes = ['Python', 'C#', 'JavaScript', 'C++', 'Java']
print(lenguajes)
print(*lenguajes)
print(lenguajes[0], lenguajes[1], lenguajes[2], lenguajes[3], lenguajes[4])


# Ejercicio 359: Agregar contenido al principio de cada elemento de una lista.
def agregar_contenido(lista, contenido):
    """
    Agrega contenido al principio de cada elemento de una lista.
    """
    return ['{}{}'.format(contenido, e) for e in lista]
numeros = list(range(1, 11))
print(numeros)
resultado = agregar_contenido(numeros, 'id')
print(resultado)


# Ejercicio 360: Iterar sobre dos listas de forma simultánea con la función zip().
nombres_colores = ['Blanco', 'Negro', 'Rojo', 'Verde', 'Azul']
codigos_colores = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF']
print(nombres_colores)
print(codigos_colores)
print()
for n, c in zip(nombres_colores, codigos_colores):
    print(n, c)


# Ejercicio 361: Acceder a las llaves de un diccionario por medio de un índice.
computador = {'marca': 'msi', 'cpu': 'Intel Core i7', 'ram': '32GB'}
print(computador)
lista_computador = list(computador)
print(lista_computador)
print(lista_computador[0])
print(lista_computador[1])
print(lista_computador[2])


# Ejercicio 362: Encontrar la sublista con la mayor suma de sus elementos.
listas_numeros = [[8, 3, 1], [4, 8, 1], [8, 5, 2], [4, 11, 13], [-8, 14, 2]]
# 12, 13, 15, 28, 8
resultado = max(listas_numeros, key=sum)
print(resultado)


# Ejercicio 363: Comprobar si todos los elementos de una lista son mayores a un valor dado.
numeros_1 = [11, 13, 7, 5, 19]
numeros_2 = [11, 2, 13, 8, 5]
valor = 5
resultado = all(n >= valor for n in numeros_1)
print(resultado)
resultado = all(n >= valor for n in numeros_2)
print(resultado)


# Ejercicio 364: Agregar elementos al principio de una lista con notación de slicing.
numeros_1 = [4, 5, 6]
numeros_2 = [1, 2, 3]
print(numeros_1)
print(numeros_2)
numeros_1[:0] = numeros_2
print()
print(numeros_1)


# Ejercicio 365: Remover los elementos duplicados de una lista de listas con groupby().
from itertools import groupby
matriz = [[1, 2], [3, 4], [7, 9], [1, 2], [7, 9], [11, 13], [0, 1]]
print(matriz)
matriz.sort()
print(matriz)
resultado = list(lista for lista, _ in groupby(matriz))
print()
print(resultado)


# Ejercicio 366: Calcular el nivel de profundidad de un objeto diccionario.
# {'a': {'b': 1, 'c': {'d': {}}}}
def profundidad_diccionario(diccionario):
    if isinstance(diccionario, dict):
        return 1 + (max(map(profundidad_diccionario, diccionario.values())) if diccionario else 0)
    return 0
d = {'a': {'b': 1, 'c': {'d': {}}}}
resultado = profundidad_diccionario(d)
print(resultado)


# Ejercicio 367: Crear función para comprobar si los diccionarios de una lista están vacíos.
def diccionarios_vacios(lista):
    """
    Comprueba si una lista de diccionarios se halla vacía.
    """
    return all(not d for d in lista)
lista = [{}, {}, {}, {}]
resultado = diccionarios_vacios(lista)
print(resultado)
lista = [{}, {}, {}, {1: 'Python'}]
resultado = diccionarios_vacios(lista)
print(resultado)


# Ejercicio 368: Ordenar un diccionario de forma ascendente y descendente por valor.
from operator import itemgetter
d = {1: 5, 2: 8, 3: 2, 4: 7, 7: 0, 8: -1, 6: 5}
d_asc = dict(sorted(d.items(), key=itemgetter(1)))
print(d)
print(d_asc)
print()
d_desc = dict(sorted(d.items(), key=itemgetter(1), reverse=True))
print(d_desc)


# Ejercicio 369: Agregar un nuevo elemento a un diccionario con el método update().
lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'Java': '12'}
print(lenguajes)
lenguajes.update({'C#': '7'})
print(lenguajes)


# Ejercicio 370: Usar el método update() para concatenar una lista de diccionarios.
def concatenar_diccionarios(lista):
    diccionarios = {}
    for d in lista:
        diccionarios.update(d)
    return diccionarios
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40, 5: 50}
dict_3 = {6: 60, 7: 70}
lista = [dict_1,  dict_2, dict_3]
resultado = concatenar_diccionarios(lista)
print(resultado)


# Ejercicio 371: Validar si una llave existe en un diccionario con el operador in.
lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'C#': '7.0', 'Java': '12'}
print('Python' in lenguajes)
print('python' in lenguajes)
print('PHP' in lenguajes)
print('Java' in lenguajes)


# Ejercicio 372: Iterar todos los ítems de un diccionario con un ciclo for.
lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'Java': '12', 'C#': '7.0', 'PHP': '7.1.2'}
for k, v in lenguajes.items():
    print('{} -> {}'.format(k, v))


# Ejercicio 373: Crear un diccionario con valores cuadrados para cada i-ésima llave.
def valores_cuadrados(n):
    return {i: i**2 for i in range(1, n + 1)}
resultado = valores_cuadrados(5)
print(resultado)
print(valores_cuadrados(10))


# Ejercicio 374: Iterar las llaves de un diccionario con el método keys().
lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'C#': '7.0', 'Java': '12'}
for k in lenguajes.keys():
    print('{} v. {}'.format(k, lenguajes[k]))


# Ejercicio 375: Fusionar dos diccionarios por medio del método update().
dict_1 = {'a': 100, 'b': 200, 'c': 300}
dict_2 = {'d': 400, 'e': 500}
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_1)
print(dict_2)
print(dict_3)


# Ejercicio 376: Iterar los valores de un diccionario con el método de instancia values().
lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'C#': '7.0', 'Java': '12'}
print(lenguajes)
print()
for v in lenguajes.values():
    print(v)


# Ejercicio 377: Usar la función sum() para sumar todos los valores de un diccionario.  
numeros = {i: i for i in range(1, 11)}
print(numeros)
suma = sum(numeros.values())
print(suma)


# Ejercicio 378: Calcular el producto de todos los valores de un diccionario.
def producto_valores(valores):
    producto = 1
    for v in valores:
        producto *= v
    return producto
numeros = {i: i**2 for i in range(1, 11)}
print(numeros)
valores = list(numeros.values())
print(valores)
resultado = producto_valores(valores)
print(resultado)


# Ejercicio 379: Remover un elemento de un diccionario con el operador del.
lenguajes = {'pyton': '3.7.4', 'JavaScript': 'ES6', 'C#': '7.0', 'Java': '12'}
print(lenguajes)
del lenguajes['pyton']
print(lenguajes)
lenguajes['Python'] = '3.7.4'
print(lenguajes)


# Ejercicio 380: Mapear dos listas en un único objeto diccionario.
nombres_lenguajes = ['Python', 'JavaScript', 'C#', 'Java']
versiones_lenguajes = ['3.8.0', 'ES6', '7.0', '12']
print(nombres_lenguajes)
print(versiones_lenguajes)
# {'nombre_lenguaje': 'version_lenguaje'}
lenguajes = dict(zip(nombres_lenguajes, versiones_lenguajes))
print(lenguajes)


# Ejercicio 381: Ordenar un objeto diccionario a partir de su llave con la función sorted().
from operator import itemgetter
colores = {'Negro': '#000000', 'Blanco': '#FFFFFF', 'Rojo': '#FF0000', 'Verde': '#00FF00', 'Azul': '#0000FF'}
print(colores)
colores = dict(sorted(colores.items(), key=itemgetter(0)))
print(colores)


# Ejercicio 382: Obtener el valor mínimo y máximo de un objeto diccionario.
productos = {'Mouse': 29, 'Teclado': 57.9, 'Monitor': 299, 'Audífonos': 25.9}
print(productos)
llave_minimo = min(productos.keys(), key=lambda k: productos[k])
print(llave_minimo, productos[llave_minimo])
llave_maximo = max(productos.keys(), key=lambda k: productos[k])
print(llave_maximo, productos[llave_maximo])


# Ejercicio 383: Crear un diccionario a partir de los campos de un objeto.
class Color(object):
    def __init__(self, rojo, verde, azul):
        self.rojo = rojo
        self.verde = verde
        self.azul = azul
negro = Color(0, 0, 0)
print(negro)
negro_dict = negro.__dict__
print(type(negro_dict))
print(negro_dict)
azul = Color(0, 0, 255)
azul_dict = azul.__dict__
print(azul_dict)


# Ejercicio 384: Remover los elementos duplicados en un diccionario.
def remover_duplicados(objetos):
    resultado = {}
    for k, v in objetos.items():
        if v not in resultado.values():
            resultado[k] = v
    return resultado
personas = {
    'id1': {
        'nombre': 'Edward',
        'apellido': 'Ortiz'
    },
    'id2': {
        'nombre': 'Daniela',
        'apellido': 'Ordoñez'
    },
    'id3': {
        'nombre': 'Alexander',
        'apellido': 'Meneses'
    },
    'id4': {
        'nombre': 'Edward',
        'apellido': 'Ortiz'
    },
    'id5': {
        'nombre': 'Daniela',
        'apellido': 'Ordoñez'
    }
}
print(len(personas))
print(personas)
personas_no_duplicados = remover_duplicados(personas)
print()
print(len(personas_no_duplicados))
print(personas_no_duplicados)


# Ejercicio 385: Comprobar si un objeto diccionario se encuentra vacío. 
d = {}
print(len(d) == 0)
print(not bool(d))
print(not d)
print()
d.update({1: 2})
print(len(d))
print(len(d) == 0)
print(not bool(d))
print(not d)


# Ejercicio 386: Combinar dos diccionarios para sumar los valores de llaves comunes.
from collections import Counter
dict_1 = {'w': 100, 'x': 200, 'y': 300}
dict_2 = {'x': 200, 'y': 100, 'z': 100}
resultado = Counter(dict_1) + Counter(dict_2)
print(resultado)


# Ejercicio 387: Obtener los valores únicos de una lista de diccionarios.
productos = [{'id': 101}, {'id': 201}, {'id': 301}, {'id': 101}, {'id': 101}, {'id': 301}, {'id': 401}, {'id': 401}]
ids_unicos = set(idp for p in productos for idp in p.values())
print(ids_unicos)


# Ejercicio 388: Crear todas las combinaciones de letras de los elementos de diccionarios.
from itertools import product
dict_letras = {'1': ['w', 'x'], '2': ['y', 'z']}
for c in product(*[dict_letras[k] for k in sorted(dict_letras.keys())]):
    print(''.join(c))


# Ejercicio 389: Encontrar las llaves con los tres valores más grandes en un diccionario.
from heapq import nlargest
productos = {'Monitor': 299, 'Mouse': 27, 'Teclado': 73.9, 'Audífonos': 25.9, 'Smartphone': 450}
productos_mas_costosos = nlargest(3, productos, key=productos.get)
print(productos_mas_costosos)


# Ejercicio 390: Combinar los elementos de una lista de diccionarios con la clase Counter.
from collections import Counter
productos = [{'id': 1, 'precio': 1000}, {'id': 2, 'precio': 2000}, {'id': 1, 'precio': 1000}, {'id': 3, 'precio': 3000}, {'id': 3, 'precio': 3000}, {'id': 4, 'precio': 4000}, {'id': 3, 'precio': 3000}, {'id': 5, 'precio': 5000}, {'id': 1, 'precio': 1000}, {'id': 5, 'precio': 5000}]
resultado = Counter()
for p in productos:
    resultado[p['id']] += p['precio']
print(resultado)


# Ejercicio 391: Contar las ocurrencias de las letras de una frase sobre un diccionario.
frase = 'python es tremendo'
resultado = {}
for c in frase:
    resultado[c] = resultado.get(c, 0) + 1
print(resultado)


# Ejercicio 392: Imprimir el contenido de un diccionario en una tabla.
valores = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
for fila in zip(*([k] + (v) for k, v in sorted(valores.items()))):
    print(*fila)


# Ejercicio 393: Contar la cantidad de estudiantes que pasaron un curso.
estudiantes = [{'id': 1, 'nombre': 'Edward', 'paso': True}, {'id': 2, 'nombre': 'Daniela', 'paso': False}, {'id': 3, 'nombre': 'Alexander', 'paso': True}, {'id': 4, 'nombre': 'Julio', 'paso': False}, {'id': 5, 'nombre': 'Sandra', 'paso': False}]
resultado = sum(e['paso'] for e in estudiantes)
print(resultado)


# Ejercicio 394: Convertir una lista de valores en un diccionario anidado de llaves.
numeros = [1, 2, 3, 4, 5]
nuevo_diccionario = {}
auxiliar = nuevo_diccionario
for n in numeros:
    nuevo_diccionario[n] = {}
    nuevo_diccionario = nuevo_diccionario[n]
print(auxiliar)


# Ejercicio 395: Ordenar las listas de valores de las llaves de un diccionario.
numeros = {'l1': [5, 3, 7], 'l2': [-7, -9, 0], 'l3': [13, 12, 9]}
print(numeros)
numeros = {k: sorted(v) for k, v in numeros.items()}
print(numeros)


# Ejercicio 396: Remover los caracteres de espacio de las llaves de un diccionario.
productos = {'ca   t1': ['Mouse', 'Teclado', 'Deademas'], 'c  at2': ['RAM', 'Procesador', 'Tarjeta gráfica'], 'ca         t3': ['Smartphone', 'Tablet', 'Portátil']}
print(productos)
resultado = {k.translate({32: None}): v for k, v in productos.items()}
print(resultado)


# Ejercicio 397: Encontrar los 3 productos más baratos desde un objeto diccionario.
from heapq import nsmallest
from operator import itemgetter
productos = {'Mouse': 29.9, 'Memoria USB': 13.5, 'Monitor': 299.9, 'Deademas': 57.9, 'Teclado': 63.9}
print(productos)
print(len(productos))
for n, p in nsmallest(3, productos.items(), key=itemgetter(1)):
    print('{}: ${}'.format(n, p))


# Ejercicio 398: Usar la función enumerate() para iterar por los ítems de un diccionario.
diccionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
for c, (k, v) in enumerate(diccionario.items(), 1):
    print(k, v, c)


# Ejercicio 399: Imprimir el contenido de un diccionario con un ciclo for.
productos = {'id1': {'nombre': 'Teclado', 'precio': 63.9}, 'id2': {'nombre': 'Mouse', 'precio': 25.9}, 'id3': {'nombre': 'Deademas', 'precio': 203.9}, 'id4': {'nombre': 'Monitor', 'precio': 299.9}, 'id5': {'nombre': 'Smartphone', 'precio': 453}}
for p in productos:
    print(p)
    for c in productos[p]:
        print('{}: {}'.format(c, productos[p][c]))
    print()


# Ejercicio 400: Comprobar si múltiples llaves existen en un diccionario.
persona = {'nombre': 'Edward', 'apellido': 'Ortiz', 'email': 'edward@mail.co', 'edad': 33}
print(persona.keys() >= {'nombre', 'edad'})
print(persona.keys() >= {'email', 'movil'})
print(persona.keys() >= {'email', 'apellido', 'edad'})
print(persona.keys() >= {'profesion'})


# Ejercicio 401: Contar la cantidad de elementos de los valores de un diccionario.
numeros = {'a': [1, 2, 3], 'b': [2, 3, 5, 7], 'c': [0, 1]}
cantidad = sum(map(len, numeros.values()))
print(cantidad)


# Ejercicio 402: Ordenar un diccionario a partir del valor de los elementos con Counter.
from collections import Counter
productos = {'Teclado': 57.9, 'Monitor': 299.9, 'Mouse': 29.5, 'Deademas': 73.5}
print(productos)
contador = Counter(productos)
print(contador.most_common())


# Ejercicio 403: Crear un diccionario con defaultdict usando dos listas de valores.
from collections import defaultdict
letras = ['A', 'B', 'C', 'D']
numeros = [1, 2, 2, 3]
diccionario = defaultdict(set)
for l, n in zip(letras, numeros):
    diccionario[l].add(n)
print(diccionario)


# Ejercicio 404: Sumar la lista de valores de cada llave de un objeto diccionario.
numeros = {'a': [1, 2, 3], 'b': [9, 8, 7], 'c': [2, 3, 5]}
print(numeros)
print()
numeros = {k: sum(v) for k, v in numeros.items()}
print(numeros)


# Ejercicio 405: Listar las llaves comunes entre dos objetos diccionario.
a = {'llave1': 1, 'llave2': 2, 'llave3': 3}
b = {'llave2': 1, 'llave4': 4, 'llave3': 3, 'llave5': 5, 'llave6': 6}
for k in set(a.keys()) & set(b.keys()):
    print(k)


# Ejercicio 406: Guardar un objeto diccionario en un archivo JSON.
import json
programacion = {'lenguajes': [{'nombre': 'Python', 'version': '3.8.0'}, {'nombre': 'Java', 'version': '12'}, {'nombre': 'JavaScript', 'version': 'ES6'}, {'nombre': 'PHP', 'version': '7.1.2'}], 'ides': ['Visual Studio', 'Eclipse IDE', 'NetBeans IDE', 'PyCharm', 'PhpStorm']}
print(programacion)
print()
print(type(programacion))
with open('programacion.json', 'w') as f:
    json.dump(programacion, f, indent=4, sort_keys=True)


# Ejercicio 407: Crear un Objeto Diccionario a partir de un Archivo JSON.
import json
with open('Parte001/programacion.json', 'r') as f:
    programacion = json.load(f)
    print(type(programacion))
    print(programacion)


# Ejercicio 408: Crear un objeto tupla vacía con una literal y la clase tuple.
# literal tupla vacía:
t = ()
print(type(t))
print(len(t))
print()
# Uso clase tuple:
t = tuple()
print(type(t))
print(len(t))


# Ejercicio 409: Inicializar un objeto tupla con elementos específicos.
tupla = (2, 3, 5, 7)
print(type(tupla))
print(len(tupla))
print(tupla)
print()
tupla = ('Python', 'JavaScript', 'Java', 'C#')
print(type(tupla))
print(len(tupla))
print(tupla)
print()
tupla = tuple([{'nombre': 'John', 'email': 'john@mail.co'}, {'nombre': 'Alex', 'email': 'alex@mail.co'}])
print(type(tupla))
print(len(tupla))
print(tupla)


# Ejercicio 410: Crear una tupla con elementos de diferente tipo de dato.
persona = ('Daniela', 'Ortiz', 29, 'daniela@mail.co', True, 100000.50)
print(persona)


# Ejercicio 411: Omitir los paréntesis al momento de crear un objeto de tipo tupla.
def fn():
    a = 1
    b = 2
    return a, b
tupla_1 = (1, 2, 3)
tupla_2 = 1, 2, 3
print(type(tupla_1))
print(type(tupla_2))


# Ejercicio 412: Crear un objeto tupla con un único elemento.
tupla = (2,)
print(tupla)
print(type(tupla))


# Ejercicio 413: Acceder al contenido de un objeto tupla.
punto = (2, 3)
print(punto)
print('Primer elemento de la tupla: {}'.format(punto[0]))
print('Segundo elemento de la tupla: {}'.format(punto[1]))
print()
# print(punto[2]) # IndexError
print('Penúltimo elemento de la tupla: {}'.format(punto[-2]))
print('Último elemento de la tupla: {}'.format(punto[-1]))
print()
# print(punto[-3]) # IndexError


# Ejercicio 414: Modificar el contenido de una tupla (TypeError).
punto = (2, 3)
print(punto)
print(len(punto))
# punto[0] = 5 # TypeError
# print(punto)


# Ejercicio 415: Iterar el contenido de una tupla a través de un ciclo for.
numeros = (2, 3, 5, 7, 11, 13, 17, 19)
for i in range(len(numeros)):
    print(numeros[i])
print()
for n in numeros:
    print(n)


# Ejercicio 416: Iterar el contenido de una tupla a través de un ciclo while.
numeros = (2, 3, 5, 7, 11, 13, 17, 19)
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1


# Ejercicio 417: Desempaquetar los elementos de una tupla en diferentes variables.
punto_3d = (2, 3, 5)
print(punto_3d)
print(len(punto_3d))
x, y, z = punto_3d
print(x, y, z)
print()
punto_3d = (7, 11, 13)
x, _, z = punto_3d
print(x, z)


# Ejercicio 418: Agregar un nuevo elemento a un objeto tupla.
numeros = (1, 2, 3, 4)
print(len(numeros))
print(numeros)
print()
numeros_nuevo = numeros + (5,)
print(len(numeros_nuevo))
print(numeros_nuevo)
print(numeros is numeros_nuevo)


# Ejercicio 419: Agregar elementos en una posición intermedia de un objeto tupla.
def agregar_elementos(tupla, i, elementos):
    if 0 < i < len(tupla) - 1:
        return tupla[:i] + elementos + tupla[i:]
    return None
numeros = (1, 2, 6, 7)
i = 2
elementos = (3, 4, 5)
resultado = agregar_elementos(numeros, i, elementos)
print(resultado)


# Ejercicio 420: Convertir un objeto tupla en un objeto lista.
tupla = (1, 2, 3)
print(len(tupla))
print(type(tupla))
print(tupla)
print()
lista = list(tupla)
print(len(lista))
print(type(lista))
print(lista)
print()
lista.append(4)
lista.append(5)
lista.append(6)
print(len(lista))
print(lista)
print()
tupla = tuple(lista)
print(len(tupla))
print(type(tupla))
print(tupla)


# Ejercicio 421: Convertir una tupla en una cadena de caracteres.
letras = ('P', 'y', 't', 'h', 'o', 'n')
python = ''.join(letras)
print(type(python))
print(python)


# Ejercicio 422: Crear una tupla a partir de una tupla de comprensión.
cuadrados = tuple(n**2 for n in range(1, 11))
print(type(cuadrados))
print(len(cuadrados))
print(cuadrados)


# Ejercicio 423: Crear una copia de un objeto tupla usando notación slicing y la clase tuple.
numeros = (1, 2, 3, 4, 5)
print(numeros)
print()
# Slicing:
numeros_copia_1 = numeros[:]
print(numeros_copia_1)
print(numeros_copia_1 is numeros)
print()
# Clase tuple:
numeros_copia_2 = tuple(numeros)
print(numeros_copia_2)
print(numeros_copia_2 is numeros)


# Ejercicio 424: Contar el número de ocurrencias de un elemento en una tupla.
numeros = (2, 3, 2, 2, 5, 5, 3, 7, 11, 13, 13, 2, 19, 23)
print(numeros)
cantidad_dos = numeros.count(2)
print('El número 2 aparece {} veces.'.format(cantidad_dos))


# Ejercicio 425: Comprobar si un elemento existe en un tupla por medio del operador in.
letras = ('P', 'y', 't', 'h', 'o', 'n')
print('y' in letras)
print('P' in letras)
print('p' in letras)
print('i' in letras)


# Ejercicio 426: Convertir un objeto lista en un objeto tupla con la clase tuple.
lista = list(range(1, 11))
print(len(lista))
print(type(lista))
print(lista)
print()
tupla = tuple(lista)
print(len(tupla))
print(type(tupla))
print(tupla)


# Ejercicio 427: Crear una función para remover un elemento de un objeto tupla.
def remover_elemento(tupla, i):
    if 0 <= i < len(tupla):
        return tupla[0:i] + tupla[i+1:]
    raise ValueError('i está por fuera del rango.')
numeros = (2, 3, 5, 7)
indice = 1
resultado = remover_elemento(numeros, indice)
print(numeros)
print(resultado)


# Ejercicio 428: Remover un elemento de una tupla usando una lista.
numeros = (2, 3, 5, 7, 11)
numeros_lista = list(numeros)
print(numeros_lista)
numeros_lista.pop(2)
print(numeros_lista)
print()
numeros = tuple(numeros_lista)
print(numeros)


# Ejercicio 429: Encontrar el índice de un elemento en una tupla.
lenguajes = ('Python', 'C#', 'JavaScript', 'C++', 'PHP')
indice = lenguajes.index('JavaScript')
print(indice)
try:
    indice = lenguajes.index('php')
    print(indice)
except ValueError as e:
    print('Ha ocurrido un error:', e)


# Ejercicio 430: Computar la longitud de un objeto tupla con la función len().
numeros = (2, 3, 5, 7, 11, 13, 17, 19)
print(numeros)
print(len(numeros))


# Ejercicio 431: Convertir un objeto tupla en un objeto diccionario.
lenguajes = (('Python', '3.8.1'), ('JavaScript', 'ES6'), ('C#', '7.0'), ('PHP', '7.1.2'))
print(lenguajes)
lenguajes_diccionario = dict((l, v) for l, v in lenguajes)
print()
print(type(lenguajes_diccionario))
print(lenguajes_diccionario)


# Ejercicio 432: Crear una lista de tuplas a partir de la función zip().
lista = [(1, 2), (3, 4), (5, 6), (7, 8)]
resultado = list(zip(*lista))
print(resultado)


# Ejercicio 433: Invertir el orden de los elementos de un objeto tupla.
numeros = (1, 2, 3, 4, 5)
print(numeros)
resultado = tuple(reversed(numeros))
print(resultado)


# Ejercicio 434: Crear un objeto diccionario a partir de una lista de objetos tupla.
lista_tuplas = [('a', 1), ('b', 2), ('a', 2), ('b', 3), ('c', 1), ('e', 5), ('c', 2), ('b', 1), ('b', 5)]
d = {}
for x, y in lista_tuplas:
    d.setdefault(x, []).append(y)
print(d)


# Ejercicio 435: Imprimir una tupla con el método de instancia format().
numeros = (2, 3, 5, 7)
print('El contenido de la tupla es: {}'.format(numeros))


# Ejercicio 436: Reemplazar el último valor de cada tupla de una lista.
tuplas = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print(tuplas)
tuplas = [t[0:-1] + (1000,) for t in tuplas]
print(tuplas)


# Ejercicio 437: Remover las tuplas vacías desde una lista de tuplas.
tuplas = [(1, 2), (5,), (), (9, 8, 7), (1,), (), ()]
print(tuplas)
print(len(tuplas))
print()
tuplas = [t for t in tuplas if t]
print(tuplas)
print(len(tuplas))


# Ejercicio 438: Ordenar una lista de tuplas por el valor de punto flotante de cada tupla.
productos = [('Mouse', '29.5'), ('Teclado', '77.9'), ('Auriculares', '15.9'), ('Deademas', '49.9')]
print(productos)
resultado = sorted(productos, key=lambda p: float(p[1]))
print(resultado)


# Ejercicio 439: Orden descendente una lista de tuplas por el valor de punto flotante de cada tupla.
productos = [('Mouse', '29.5'), ('Teclado', '77.9'), ('Auriculares', '15.9'), ('Deademas', '49.9')]
print(productos)
resultado = sorted(productos, key=lambda p: float(p[1]), reverse=True)
print(resultado)


# Ejercicio 440: Crear un conjunto utilizando la literal de conjunto y la clase set.
# Literal de conjunto:
conjunto_literal = {0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 5}
print(type(conjunto_literal))
print(len(conjunto_literal))
print(conjunto_literal)
print()
# Clase set:
conjunto = set((0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 5))
print(type(conjunto))
print(len(conjunto))
print(conjunto)


# Ejercicio 441: Iterar todos los elementos contenidos en un objeto conjunto.
numeros = {0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9}
print(type(numeros))
print(len(numeros))
print(numeros)
print()
for n in numeros:
    print(n)


# Ejercicio 442: Agregar elementos a un objeto conjunto con el método de instancia add().
lenguajes = set()
print(len(lenguajes))
print(lenguajes)
print()
lenguajes.add('Python')
print(len(lenguajes))
print(lenguajes)
print()
lenguajes.add('Java')
print(len(lenguajes))
print(lenguajes)
print()
lenguajes.add('Java')
print(len(lenguajes))
print(lenguajes)
print()
lenguajes.add('java')
print(len(lenguajes))
print(lenguajes)


# Ejercicio 443: Agregar múltiples elementos a un objeto conjunto con el método update().
colores = set()
colores.add('Negro')
colores.add('Blanco')
print(len(colores))
print(colores)
print()
lista_colores = ['Rojo', 'Verde', 'Azul', 'Rojo', 'Verde']
colores.update(lista_colores)
print(len(colores))
print(colores)


# Ejercicio 444: Remover elementos de un objeto conjunto con el método de instancia pop().
numeros = set([2, 3, 5, 7, 11])
print(len(numeros))
print(numeros)
print()
numero = numeros.pop()
print(numero)
print(len(numeros))
print(numeros)


# Ejercicio 445: Remover un elemento de un conjunto si está disponible con el método discard().
numeros = set([2, 3, 5, 7, 11, 13])
print(len(numeros))
print(numeros)
print()
numeros.discard(7)
print(len(numeros))
print(numeros)
print()
numeros.discard(0)
print(len(numeros))
print(numeros)


# Ejercicio 446: Hallar los elementos comunes de dos conjuntos con el operador intersección.
# &
colores_1 = set(['Negro', 'Blanco', 'Azul'])
colores_2 = set(['Rojo', 'Verde', 'Azul', 'Amarillo', 'Negro'])
print(colores_1)
print(colores_2)
print()
colores_comunes = colores_1 & colores_2
print(colores_comunes)


# Ejercicio 447: Computar el conjunto unión entre dos objetos conjunto.
colores_1 = set(['Negro', 'Blanco', 'Rojo'])
colores_2 = set(['Azul', 'Verde', 'Gris', 'Negro'])
print(colores_1)
print(colores_2)
print()
colores = colores_1 | colores_2
print(colores)


# Ejercicio 448: Calcular la diferencia entre dos objetos conjunto con el operador diferencia.
# -
colores_1 = set(['Negro', 'Blanco', 'Rojo'])
colores_2 = set(['Blanco', 'Negro', 'Azul', 'Gris'])
print(colores_1)
print(colores_2)
print()
resultado = colores_1 - colores_2
print(resultado)
print()
resultado = colores_2 - colores_1
print(resultado)


# Ejercicio 449: Calcular la diferencia simétrica entre dos objetos conjunto.
# ^
colores_1 = set(['Negro', 'Rojo'])
colores_2 = set(['Rojo', 'Blanco'])
print(colores_1)
print(colores_2)
print()
resultado = colores_1 ^ colores_2
print(resultado)


# Ejercicio 450: Comprobar si un conjunto es subconjunto o superconjunto de otro conjunto.
colores_1 = set(['Negro', 'Blanco'])
colores_2 = set(['Blanco', 'Rojo'])
colores_3 = set(['Blanco'])
print(colores_1)
print(colores_2)
print(colores_3)
print()
subconjunto = colores_1 <= colores_2
print(subconjunto)
print()
superconjunto = colores_1 >= colores_2
print(superconjunto)
print()
subconjunto = colores_3 <= colores_2
print(subconjunto)
print()
superconjunto = colores_2 >= colores_3
print(superconjunto)


# Ejercicio 451: Crear una copia de todos los elementos de un objeto conjunto.
numeros = set([2, 3, 5, 7])
print(numeros)
numeros_copia = numeros.copy()
print(numeros_copia)
print(numeros_copia is numeros)


# Ejercicio 452: Remover todos los elementos de un conjunto con el método de instancia clear().
numeros = set([2, 3, 5, 7])
print(len(numeros))
print(numeros)
print()
numeros.clear()
print(len(numeros))
print(numeros)


# Ejercicio 453: Comprobar si dos conjuntos no tienen elementos en común con isdisjoint().
colores_1 = set(['Negro', 'Blanco'])
colores_2 = set(['Azul', 'Rojo', 'Negro'])
colores_3 = set(['Gris'])
print(colores_1)
print(colores_2)
print(colores_3)
print()
print(colores_1.isdisjoint(colores_2))
print()
print(colores_1.isdisjoint(colores_3))
print()
print(colores_2.isdisjoint(colores_3))


# Ejercicio 454: Encontrar los valores mínimo y máximo en un objeto conjunto.
numeros = set([13, 2, 19, 7, 5, 11, 3])
print(numeros)
minimo = min(numeros)
print(minimo)
maximo = max(numeros)
print(maximo)


# Ejercicio 455: Filtrar los elementos de un objeto conjunto con la función filter().
numeros = set([2, 3, 5, 7, 11, 13, 17, 19])
print(len(numeros))
print(numeros)
print()
resultado = set(filter(lambda e: e > 7, numeros))
print(resultado)


# Ejercicio 456: Repetir un elemento cierta cantidad de veces con la clase Counter.
from collections import Counter
contador = Counter(a=5, e=4, i=0, o=-1, u=2)
print(contador)
print()
elementos_repetidos = list(contador.elements())
print(type(elementos_repetidos))
print(elementos_repetidos)


# Ejercicio 457: Hallar los elementos más comunes y el número de ocurrencias en una colección.
from collections import Counter
frase = 'Python es un lenguaje de programación. Python versión 3.8.1. Python es uno de los lenguajes más utilizados para crear soluciones de software.'
contador = Counter(frase)
print(contador)
print()
print(contador.most_common(5))


# Ejercicio 458: Crear un objeto deque e iterar su contenido con un ciclo for.
from collections import deque
d = deque('aeiou')
for v in d:
    print(v)


# Ejercicio 459: Encontrar las n palabras más recurrentes en un texto con la clase Counter.
from collections import Counter
import re
texto = """
En una tarde extremadamente calurosa de principios de julio, un joven salió de la reducida habitación que tenía alquilada en la callejuela de S*** y, con paso lento e indeciso, se dirigió al puente K***.
Había tenido la suerte de no encontrarse con su patrona en la escalera.
Su cuartucho se hallaba bajo el tejado de un gran edificio de cinco pisos y, más que una habitación, parecía una alacena. En cuanto a la patrona, que le había alquilado el cuarto con servicio y pensión, ocupaba un departamento del piso de abajo; de modo que nuestro joven, cada vez que salía, se veía obligado a pasar por delante de la puerta de la cocina, que daba a la escalera y estaba casi siempre abierta de par en par. En esos momentos experimentaba invariablemente una sensación ingrata de vago temor, que le humillaba y daba a su semblante una expresión sombría. Debía una cantidad considerable a la patrona y por eso temía encontrarse con ella. No es que fuera un cobarde ni un hombre abatido por la vida. Por el contrario, se hallaba desde hacía algún tiempo en un estado de irritación, de tensión incesante, que rayaba en la hipocondría. Se había habituado a vivir tan encerrado en sí mismo, tan aislado, que no sólo temía encontrarse con su patrona, sino que rehuía toda relación con sus semejantes. La pobreza le abrumaba. Sin embargo, últimamente esta miseria había dejado de ser para él un sufrimiento. El joven había renunciado a todas sus ocupaciones diarias, a todo trabajo.
En el fondo, se mofaba de la patrona y de todas las intenciones que pudiera abrigar contra él, pero detenerse en la escalera para oír sandeces y vulgaridades, recriminaciones, quejas, amenazas, y tener que contestar con evasivas, excusas, embustes... No, más valía deslizarse por la escalera como un gato para pasar inadvertido y desaparecer.
Aquella tarde, el temor que experimentaba ante la idea de encontrarse con su acreedora le llenó de asombro cuando se vio en la calle.
"""
palabras = re.findall('\w+', texto)
contador = Counter(palabras)
print(contador.most_common(10))


# Ejercicio 460: Ingresar n palabras y contar las ocurrencias de cada palabra.
from collections import Counter, OrderedDict
class ContadorOrdenado(Counter, OrderedDict):
    pass
n = int(input('Cantidad de palabras: '))
palabras = []
for _ in range(n):
    palabras.append(input().strip())
contador = ContadorOrdenado(palabras)
print(contador)
print(len(contador))
print()
for c in contador:
    print(contador[c], end=' ')


# Ejercicio 461: Acceder a un elemento de un objeto Counter.
from collections import Counter
c = Counter(rojo=255, verde=0, azul=0)
print(c)
print(c['rojo'])
print(c['verde'])
print(c['azul'])
print()
print(c['amarillo'])


# Ejercicio 462: Manipular un objeto deque con sus operaciones básicas.
from collections import deque
colores = deque(['Rojo', 'Verde', 'Azul'])
print(len(colores))
print(colores)
print()
colores.appendleft('Negro')
print(len(colores))
print(colores)
print()
colores.append('Blanco')
print(len(colores))
print(colores)
print()
colores.popleft()
print(len(colores))
print(colores)
print()
colores.pop()
print(len(colores))
print(colores)
print()
colores.reverse()
print(colores)


# Ejercicio 463: Crear un objeto deque utilizando un objeto tupla.
from collections import deque
numeros = (5, 7, 11, 13)
print(type(numeros))
print(numeros)
print()
primos = deque(numeros)
print(type(primos))
print(primos)
print()
primos.appendleft(3)
primos.append(17)
print(primos)


# Ejercicio 464: Crear un objeto deque a partir de un objeto diccionario.
from collections import deque
d = {'a': 1, 'b': 2, 'c': 3}
letras = deque(d)
print(len(letras))
print(letras)
print()
letras.appendleft('f')
letras.append('d')
print(len(letras))
print(letras)
print()
letras.extend({'g': 8, 'h': 9})
print(len(letras))
print(letras)


# Ejercicio 465: Eliminar todos los elementos de un objeto deque con el método clear().
from collections import deque
d = deque([3, 5, 7])
print(len(d))
print(d)
print()
d.appendleft(2)
d.append(11)
print(len(d))
print(d)
print()
d.clear()
print(len(d))
print(d)


# Ejercicio 466: Copiar los elementos de un objeto deque con el método de instancia copy().
from collections import deque
numeros = deque([2, 3, 5, 7, 11])
print(numeros)
print('ID:', id(numeros))
print()
numeros_copia = numeros.copy()
print(numeros_copia)
print('ID:', id(numeros_copia))


# Ejercicio 467: Contar el número de ocurrencias de un elemento en un objeto deque.
from collections import deque
numeros = deque((3, 5, 7, 2, 2, 2, 3, 5, 7, 13, 11, 2, 3, 5))
print(len(numeros))
print(numeros)
print()
conteo_dos = numeros.count(2)
print('El valor 2 aparece {} veces.'.format(conteo_dos))


# Ejercicio 468: Rotar un objeto deque una cantidad arbitraria de veces con el método rotate().
# [1, 2, 3], 1, 2
# [3, 1, 2]
# [2, 3, 1]
from collections import deque
numeros = deque([1, 2, 3, 4, 5])
print(numeros)
print()
numeros.rotate(3)
# 3, 4, 5, 1, 2
print(numeros)
print()
numeros.rotate(len(numeros))
print(numeros)


# Ejercicio 469: Rotación negativa de un objeto deque con el método de instancia rotate().
# [1, 2, 3, 4, 5], -2
# [3, 4, 5, 1, 2]
from collections import deque
numeros = deque([1, 2, 3, 4, 5])
print(numeros)
numeros.rotate(-2)
print(numeros)
numeros.rotate(-5)
print(numeros)


# Ejercicio 470: Encontrar el nombre de lenguaje de programación más común con Counter.
from collections import Counter
lenguajes = ['Python', 'C', 'C', 'PHP', 'Python', 'Java', 'Python', 'C++', 'JavaScript', 'Python', 'Perl', 'Java']
contador = Counter(lenguajes)
print(contador)
print(contador.most_common(1)[0][0])


# Ejercicio 471: Combinar dos objetos Counter con el operador sobrecargado +.
from collections import Counter
contador_1 = Counter([1, 2, 3, 4, 5])
contador_2 = Counter([1, 2, 3, 4, 5])
print(contador_1)
print(contador_2)
print()
contador_3 = contador_1 + contador_2
print(contador_3)


# Ejercicio 472: Crear un objeto array con elementos de tipo entero.
from array import array
numeros = array('i', [2, 3, 5, 7])
print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])


# Ejercicio 473: Agregar elementos a un objeto array con el método de instancia append().
from array import array
numeros = array('i')
print(len(numeros))
print(numeros)
print()
numeros.append(2)
numeros.append(3)
numeros.append(5)
numeros.append(7)
print(len(numeros))
print(numeros)
print()
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])


# Ejercicio 474: Iterar todos los elementos de un objeto array con un ciclo for.
from array import array
numeros = array('i', [2, 3])
numeros.append(5)
numeros.append(7)
numeros.extend([11, 13, 17])
print(numeros)
for n in numeros:
    print(n)


# Ejercicio 475: Invertir el orden de los elementos de un objeto array.
from array import array
numeros = array('i', [2, 3, 5, 7, 11, 13])
print(numeros)
print()
numeros.reverse()
print(numeros)


# Ejercicio 476: Obtener el tamaño en bytes de cada elemento de un objeto array con itemsize.
from array import array
numeros = array('i', [2, 3, 5, 7, 11])
print(numeros)
print(numeros.itemsize)
print()
punto_flotante = array('d', [2.2, 3.3, 5.5])
print(punto_flotante)
print(punto_flotante.itemsize)


# Ejercicio 477: Cargar elementos a un objeto array desde una lista con fromlist().
from array import array
numeros = array('i')
print(len(numeros))
print(numeros)
print()
primos = [2, 3, 5, 7, 11, 13, 17, 19]
numeros.fromlist(primos)
print(len(numeros))
print(numeros)


# Ejercicio 478: Guardar los elementos de un objeto array en un archivo binario con tofile().
from array import array
numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
with open('Parte001/numeros_array.bin', 'wb') as f:
    numeros.tofile(f)


# Ejercicio 479: Leer el contenido de un objeto array desde un archivo binario con fromfile().
from array import array
with open('Parte001/numeros_array.bin', 'rb') as f:
    numeros = array('i')
    numeros.fromfile(f, 8)
if numeros is not None:
    print(len(numeros))
    print(numeros)


# Ejercicio 480: Contar el numero de ocurrencias de un elemento en un objeto array.
from array import array
numeros = array('i', [2, 3, 2, 2, 5, 7, 7, 7, 13, 7, 7, 11, 2, 5, 19, 23, 29])
print(len(numeros))
print(numeros)
print()
conteo_7 = numeros.count(7)
print(conteo_7)


# Ejercicio 481: Agregar múltiples elementos al final de un objeto array con extend().
from array import array
primos = array('d', [1.1, 2.2, 3.3, 5.5])
print(len(primos))
print(primos)
numeros = array('d', [6.6, 7.7, 8.8, 9.9])
print(len(numeros))
print(numeros)
print()
primos.extend(numeros)
print(len(primos))
print(primos)


# Ejercicio 482: Obtener la representación en bytes de un objeto array con tobytes().
from array import array
arreglo_bytes = array('b', [80, 121, 116, 104, 111, 110])
cadena_bytes = arreglo_bytes.tobytes()
print(cadena_bytes)


# Ejercicio 483: Iterar los elementos de un objeto array con un ciclo while.
from array import array
numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1


# Ejercicio 484: Agregar un elemento en un índice específico de un objeto array con insert().
from array import array
primos = array('i', [2, 5, 7, 11, 13])
print(len(primos))
print(primos)
print()
primos.insert(1, 3)
print(len(primos))
print(primos)


# Ejercicio 485: Eliminar un elemento en un índice específico de un objeto array con pop().
from array import array
numeros = array('i', [2, 3, 5, 7, 11])
print(len(numeros))
print(numeros)
print()
numeros.pop()
print(len(numeros))
print(numeros)
print()
numeros.pop(1)
print(len(numeros))
print(numeros)


# Ejercicio 486: Eliminar la primera ocurrencia de un valor en un objeto array con remove().
from array import array
numeros = array('i', [2, 2, 3, 2, 5, 5, 3, 7, 7, 11, 13, 17, 19])
print(len(numeros))
print(numeros)
print()
numeros.remove(2)
print(len(numeros))
print(numeros)
print()
numeros.remove(3)
print(len(numeros))
print(numeros)


# Ejercicio 487: Convertir un objeto array en un objeto list con el método tolist().
from array import array
numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print(len(numeros))
print(numeros)
print()
primos = numeros.tolist()
print(len(primos))
print(type(primos))
print(primos)


# Ejercicio 488: Crear función para determinar si un objeto array contiene duplicados.
from array import array
def elementos_duplicados(arreglo):
    conjunto = set(arreglo.tolist())
    return len(conjunto) != len(arreglo)
numeros = array('i', [1, 2, 3, 4, 5])
print(elementos_duplicados(numeros))
numeros.append(1)
print(elementos_duplicados(numeros))


# Ejercicio 489: Uso del método de instancia tostring() de la clase array.
from array import array
numeros = array('i', [2, 3, 5, 7])
cadena = numeros.tostring()
print(cadena)
print()
primos = array('i')
primos.fromstring(cadena)
print(primos)


# Ejercicio 490: Encontrar los números divibles por 7 y múltiplos de 5 en un rango dado.
def numeros_divibles_multiplos(limite_inferior, limite_superior):
    if limite_superior > limite_inferior:
        resultado = []
        for n in range(limite_inferior, limite_superior + 1):
            if n % 7 == 0 and n % 5 == 0:
                resultado.append(n)
        return resultado
    raise ValueError('El límite inferior debe ser menor al límite superior.')
numeros = numeros_divibles_multiplos(500, 1000)
print(numeros)


# Ejercicio 491: Crear una función para convertir grados Celsius en grados Fahrenheit.
def convertir_celsius_fahrenheit(celsius):
    """
    Convierte grados Celsius en grados Fahrenheit.
    """
    return (celsius * 9.0/5.0) + 32
print(convertir_celsius_fahrenheit(9))


# Ejercicio 492: Crear una función para convertir grados Fahrenheit en grados Celsius.
def fahrenheit_celsius(f):
    """
    Convierte grados Fahrenheit en grados Celsius.
    """
    return (f - 32) * 5.0/9.0
print(fahrenheit_celsius(9))


# Ejercicio 493: Solicitar al usuario que adivine un número entre 1 y 9.
from random import randint
aleatorio = randint(1, 9)
numero = 0
while aleatorio != numero:
    numero = int(input('Adivine un número entre 1 y 9: '))
print('¡Bien hecho!')


# Ejercicio 494: Crear el siguiente patrón usando un ciclo for anidado.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('* ', end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print('* ', end='')
    print()


# Ejercicio 495: Invertir una palabra escrita por el usuario utilizando un ciclo for.
def invertir_palabra(palabra):
    resultado = ''
    for c in range(len(palabra) - 1, -1, -1):
        resultado += palabra[c]
    return resultado
frase = input('Digite un palabra: ')
print(invertir_palabra(frase))


# Ejercicio 496: Crear función para contar la cantidad números pares e impares en una lista.
def contar_pares_impares(lista):
    pares, impares = 0, 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = contar_pares_impares(numeros)
print('La cantidad de pares es: %i' % resultado[0])
print('La cantidad de impares es: %i' % resultado[1])


# Ejercicio 497: Imprimir el valor y el tipo de dato de cada elemento de una lista.
lista_mixta = ['Python', 3.1415, [1, 2, 3], 0, {'a': 1}, (0, 1), set([0, 1, 2]), 5+3j, True, False]
for i in range(len(lista_mixta)):
    print('Valor: {} - Tipo de dato: {}'.format(lista_mixta[i], type(lista_mixta[i])))


# Ejercicio 498: Imprimir los números del rango 0 a 10 excepto los múltiplos de 3.
for n in range(11):
    if n % 3 != 0:
        print(n)


# Ejercicio 499: Generar los números de la serie Fibonacci menores a 100.
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b


# Ejercicio 500: Iterar un ciclo for en orden inverso por medio de la función range().
for i in range(1, 11):
    print(i, end=' ')
print()
for i in range(10, 0, -1):
    print(i, end=' ')


# Ejercicio 501: Crear una matriz mxn con los tamaños especificados por el usuario.
def crear_matriz(m, n):
    """
    Crea una matriz de m filas y n columnas.
    """
    return [[i*j for j in range(n)] for i in range(m)]
filas = int(input('Digite la cantidad de filas: '))
columnas = int(input('Digite la cantidad de columnas: '))
matriz = crear_matriz(filas, columnas)
print(matriz)


# Ejercicio 502: Convertir a mayúscula una serie de palabras ingresadas por el usuario.
palabras = []
while True:
    palabra = input()
    if palabra:
        palabras.append(palabra.upper())
    else:
        break
for p in palabras:
    print(p)


# Ejercicio 503: Capturar binarios de 4 bits separados por coma y validar si son divibles por 5.
numeros = []
cadena = input('Escriba números binarios de 4 bits separados por coma: ')
binarios = [b for b in cadena.split(',')]
for b in binarios:
    entero = int(b, 2)
    if not entero % 5:
        numeros.append(b)
print(', '.join(numeros))


# Ejercicio 504: Contar la cantidad de dígitos y letras en una cadena de caracteres.
def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0
    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras
texto = input('Digite un texto: ')
resultado = contar_digitos_letras(texto)
print('Cantidad de dígitos: %i' % resultado[0])
print('Cantidad de letras: %i' % resultado[1])


# Ejercicio 505: Validar si una contraseña especificada por el usuario es segura.
import re
def validar_password(password):
    if 8 <= len(password) <= 16:
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            if re.search('[0-9]', password):
                if re.search('[$@#]', password):
                    return True
    return False
clave = input('Escriba la contraseña: ')
print(validar_password(clave))


# Ejercicio 506: Imprimir los números cuyos dígitos sean pares en el rango 100 a 400.
def digitos_pares():
    pares = []
    for n in range(100, 401):
        cadena = str(n)
        if int(cadena[0]) % 2 == 0 and int(cadena[1]) % 2 == 0 and int(cadena[2]) % 2 == 0:
            pares.append(cadena)
    return pares
resultado = digitos_pares()
print(', '.join(resultado))


# Ejercicio 507: Imprimir un patrón de asteriscos para representar la letra A mayúscula.
#   ***                                                                                                         
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *****                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   * 
for i in range(0, 7):
    for j in range(0, 7):
        if (i == 0 and ( 2 <= j <= 4)):
            print('*', end='')
        elif (i == 1 or i == 2 or i >= 4) and (j == 1 or j == 5):
            print('*', end='')
        elif i == 3 and 1 <= j <= 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 508: Imprimir un patrón de asteriscos para representar la letra D mayúscula.
#  ****                                                                                                         
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  ****  
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and (1 <= j <= 4):
            print('*', end='')
        elif (1 <= i <= 5) and (j == 1 or j == 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 509: Imprimir un patrón de asteriscos para representar la letra E mayúscula.
#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 1 <= j <= 5:
            print('*', end='')
        elif (i == 1 or i == 2 or i == 4 or i == 5) and j == 1:
            print('*', end='')
        elif i == 3 and 1 <= j <= 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 510: Imprimir un patrón de asteriscos para representar la letra G mayúscula.
#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 2 <= j <= 4:
            print('*', end='')
        elif (i == 1 or i == 4 or i == 5) and (j== 1 or j == 5):
            print('*', end='')
        elif i == 2 and j == 1:
            print('*', end='')
        elif i == 3 and (j == 1 or 3 <= j <= 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 511: Imprimir un patrón de asteriscos para representar la letra L mayúscula.
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****
for i in range(7):
    for j in range(7):
        if 0 <= i <= 5 and j == 1:
            print('*', end='')
        elif i == 6 and 1 <= j <= 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 512: Imprimir un patrón de asteriscos para representar la letra M mayúscula.
#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *
for i in range(7):
    for j in range(12):
        if (i == 0 or i == 1 or 4 <= i <= 6) and (j == 1 or j == 11):
            print('*', end='')
        elif i == 2 and (j == 1 or j == 3 or j == 9 or j == 11):
            print('*', end='')
        elif i == 3 and (j == 1 or j == 6 or j == 11):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 513: Imprimir un patrón de asteriscos para representar la letra O mayúscula.
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 2 <= j <= 4:
            print('*', end='')
        elif 1 <= i <= 5 and (j == 1 or j == 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 514: Imprimir un patrón de asteriscos para representar la letra P mayúscula.
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *  
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 3) and (1 <= j <= 4):
            print('*', end='')
        elif (i == 1 or i == 2) and (j == 1 or j == 5):
            print('*', end='')
        elif (4 <= i <= 6) and j == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 515: Imprimir un patrón de asteriscos para representar la letra R mayúscula.
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 3) and (1 <= j <= 4):
            print('*', end='')
        elif (i == 1 or i == 2) and (j == 1 or j == 5):
            print('*', end='')
        elif i == 4 and (j == 1 or j == 3):
            print('*', end='')
        elif i == 5 and (j == 1 or j == 4):
            print('*', end='')
        elif i == 6 and (j == 1 or j == 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 516: Imprimir un patrón de asteriscos para representar la letra S mayúscula.
#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
for i in range(7):
    for j in range(7):
        if i == 0 and (2 <= j <= 5):
            print('*', end='')
        elif (i == 1 or i == 2) and j == 1:
            print('*', end='')
        elif i == 3 and 2 <= j <= 4:
            print('*', end='')
        elif (i == 4 or i == 5) and j == 5:
            print('*', end='')
        elif i == 6 and 1 <= j <= 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 517: Imprimir un patrón de asteriscos para representar la letra S mayúscula.
#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 
for i in range(15):
    for j in range(22):
        if i == 0 and 2 <= j <= 20:
            print('*', end='')
        elif (i == 1 or i == 2 or i == 6 or i == 7 or i == 8 or i == 12 or i == 13 or i == 14) and (1 <= j <= 19):
            print('*', end='')
        elif (3 <= i <= 5) and 1 <= j <= 4:
            print('*', end='')
        elif (9 <= i <= 11) and 16 <= j <= 19:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 518: Imprimir un patrón de asteriscos para representar la letra T mayúscula.
#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  
for i in range(7):
    for j in range(7):
        if i == 0 and 1 <= j <= 5:
            print('*', end='')
        elif i > 0 and j == 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 519: Imprimir un patrón de asteriscos para representar la letra U mayúscula.
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(7):
    for j in range(7):
        if 1 <= i <= 5 and (j == 1 or j == 5):
            print('*', end='')
        elif i == 6 and (2 <= j <= 4):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 520: Imprimir un patrón de asteriscos para representar la letra X mayúscula.
#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 1 or i == 5 or i == 6) and (j == 1 or j == 5):
            print('*', end='')
        elif (i == 2 or i == 4) and (j == 2 or j == 4):
            print('*', end='')
        elif i == 3 and j == 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 521: Imprimir un patrón de asteriscos para representar la letra Z mayúscula.
# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******
for i in range(7):
    for j in range(9):
        if (i == 0 or i == 6) and (1 <= j <= 7):
            print('*', end='')
        elif i == 1 and j == 6:
            print('*', end='')
        elif i == 2 and j == 5:
            print('*', end='')
        elif i == 3 and j == 4:
            print('*', end='')
        elif i == 4 and j == 3:
            print('*', end='')
        elif i == 5 and j == 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Ejercicio 522: Calcular la edad en años de un perro a partir de la edad de una persona.
# Análisis:
# edad_persona <= 2:
# edad perro = edad_persona * 10.5
# edad_persona > 2:
# edad perro = 21 + (edad_persona - 2) * 4
def calcular_edad_perro(edad_persona):
    if edad_persona <= 2:
        return edad_persona * 10.5
    else:
        return 21 + (edad_persona - 2) * 4
edad_persona = int(input('Digite la edad en años de la persona: '))
if edad_persona > 0:
    resultado = calcular_edad_perro(edad_persona)
    print(f'La edad del perro en años sería {resultado}')


# Ejercicio 523: Identificar si una letra ingresa por el usuario es una vocal o consonante.
def vocal_o_consonante(letra):
    if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return 'Vocal'
    elif letra in ('y', 'Y'):
        return 'Vocal/Consonante'
    else:
        return 'Consonante'
l = input('Escriba una letra cualquiera: ')
print(vocal_o_consonante(l))


# Ejercicio 524: Determinar la cantidad de días de un mes ingresado por el usuario.
def cantidad_dias(mes):
    if mes.lower() in ('enero', 'marzo', 'julio', 'agosto', 'octubre', 'diciembre'):
        return '31'
    elif mes.lower() == 'febrero':
        return '28/29'
    else:
        return '30'
nombre_mes = input('Ingrese el nombre del mes: ')
print(cantidad_dias(nombre_mes))


# Ejercicio 525: Calcular la suma de 2 números. Si la suma está entre 15 y 30, retornar 20.
def calcular_suma(a, b):
    suma = a + b
    if suma in range(15, 31):
        return 20
    return suma
operando_1 = 13
operando_2 = 30
print(calcular_suma(operando_1, operando_2))
operando_1 = 13
operando_2 = 15
print(calcular_suma(operando_1, operando_2))


# Ejercicio 526: Crear una función para comprobar si una cadena representa un número.
def es_entero(cadena):
    return all(cadena[i] in '0123456789' for i in range(len(cadena)))
valor = input('Digite un número entero: ')
print(es_entero(valor))


# Ejercicio 527: Determinar si un triángulo es equilátero, isósceles o escaleno.
def tipo_triangulo(a, b, c):
    if a == b and a == c:
        return 'Equilátero'
    elif a != b and a != c:
        return 'Escaleno'
    else:
        return 'Isósceles'
lado_1 = 5
lado_2 = 5
lado_3 = 5
print(tipo_triangulo(lado_1, lado_2, lado_3))
lado_1 = 5
lado_2 = 3
lado_3 = 5
print(tipo_triangulo(lado_1, lado_2, lado_3))
lado_1 = 5
lado_2 = 15
lado_3 = 10
print(tipo_triangulo(lado_1, lado_2, lado_3))


# Ejercicio 528: Determinar la estación meteorológica del año a partir del nombre del mes.
def estacion_meteorologica(mes):
    if mes.lower() in ('enero', 'febrero', 'marzo'):
        return 'Invierno'
    elif mes.lower() in ('abril', 'mayo', 'junio'):
        return 'Primavera'
    elif mes.lower() in ('julio', 'agosto', 'septiembre'):
        return 'Verano'
    else:
        return 'Otoño'
mes = 'Enero'
print(estacion_meteorologica(mes))
mes = 'julio'
print(estacion_meteorologica(mes))
mes = 'Noviembre'
print(estacion_meteorologica(mes))
mes = 'abril'
print(estacion_meteorologica(mes))


# Ejercicio 529: Encontrar el tamaño máximo de palabra representable en Python.
import sys
print(sys.maxsize)


# Ejercicio 530: Ejecutar una aplicación Windows con la función subprocess.Popen().
from subprocess import Popen
proceso = 'notepad.exe'
Popen([proceso])


# Ejercicio 531: Crear una función personalizada para calcular la mediana de tres números.
def calcular_mediana(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
print(calcular_mediana(3, 7, 5))
print(calcular_mediana(3, 7, 9))
print(calcular_mediana(-3, -7, -5))


# Ejercicio 532: Obtener la fecha del siguiente día a partir de una fecha dada.
def fecha_dia_siguiente(agnio, mes, dia):
    bisiesto = False
    if agnio % 400 == 0:
        bisiesto = True
    elif agnio % 4 == 0:
        bisiesto = True
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30
    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            agnio += 1
        else:
            mes += 1
    return (agnio, mes, dia)
print(fecha_dia_siguiente(2020, 1, 15))
print(fecha_dia_siguiente(2020, 1, 31))
print(fecha_dia_siguiente(2020, 2, 28))
print(fecha_dia_siguiente(2020, 12, 31))


# Ejercicio 533: Calcular el promedio de n cantidad de números enteros.
contador = 0
suma = 0
numero = 1
while numero != 0:
    numero = int(input('Digite un número entero (0 para terminar): '))
    if numero != 0:
        suma += numero
        contador += 1
if contador == 0:
    print('No digitó ningún número.')
else:
    promedio = suma / contador
    print('El promedio de los {} números es igual a {}.'.format(contador, promedio))


# Ejercicio 534: Crear la tabla de multiplicar (desde 1 hasta 10) para un x número.
numero = int(input('Digite un número entero: '))
for i in range(1, 11):
    print(f'{i} x {numero} = {i * numero}')


# Ejercicio 535: Construir un patrón de números por medio de un ciclo for anidado.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999  
for n in range(1, 10):
    # for x in range(n):
    #     print(n, end='')
    print(str(n) * n)


# Ejercicio 536: Crear una función personalizada para calcular el máximo de tres números.
def maximo_dos_numeros(a, b):
    if a > b:
        return a
    return b
def maximo_tres_numeros(a, b, c):
    return maximo_dos_numeros(a, maximo_dos_numeros(b, c))
print(maximo_tres_numeros(7, 5, 3))
print(maximo_tres_numeros(-7, -5, -3))
print(maximo_tres_numeros(11, 3, 19))


# Ejercicio 537: Crear una función personalizada para sumar los números de una lista o tupla.
def sumar(numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma
lista_numeros = [1, 2, 3, 4, 5]
print(type(lista_numeros))
print(sumar(lista_numeros))
print()
tupla_numeros = (1, 2, 3, 4, 5)
print(type(tupla_numeros))
print(sumar(tupla_numeros))


# Ejercicio 538: Crear una función para multiplicar los números de una lista o tupla.
def multiplicar(numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto
lista_numeros = [2, 3, 5, 7, 11]
print(type(lista_numeros))
print(multiplicar(lista_numeros))
print()
tupla_numeros = (2, 3, 5, 7, 11)
print(type(tupla_numeros))
print(multiplicar(tupla_numeros))


# Ejercicio 539: Crear una función personalizada para invertir una cadena de caracteres.
def invertir_cadena(texto):
    resultado = ''
    indice = len(texto)
    while indice > 0:
        resultado += texto[indice - 1]
        indice -= 1
    return resultado
lenguaje = 'nohtyP'
print(invertir_cadena(lenguaje))
print(invertir_cadena('Python'))


# Ejercicio 540: Crear una función recursiva para calcular el factorial de un número.
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    # producto = 1
    # for i in range(1, n + 1):
    #     producto *= i
    # return producto
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(10))


# Ejercicio 541: Crear una función para comprobar si un número dado se halla en un rango.
def esta_en_rango(rango, numero):
    return numero in range(*rango)
print(esta_en_rango([1, 6], 2))
print(esta_en_rango([1, 6], -1))
print(esta_en_rango([1, 6], 6))
print(esta_en_rango([1, 6], 5))


# Ejercicio 542: Crear una función para contar las minúsculas y las mayúsculas de una cadena.
def contador_minusculas_mayusculas(cadena):
    contador = {'minusculas': 0, 'mayusculas': 0}
    for c in cadena:
        if c.isupper():
            contador['mayusculas'] += 1
        elif c.islower():
            contador['minusculas'] += 1
    return contador
frase = 'Python es un lenguaje de programación'
print(contador_minusculas_mayusculas(frase))
escritor = 'Fyodor Mijalovich Dostoevskiy'
print(contador_minusculas_mayusculas(escritor))


# Ejercicio 543: Crear una función para remover los duplicados de una lista o tupla.
def remover_duplicados(elementos):
    no_duplicados = []
    for e in elementos:
        if e not in no_duplicados:
            no_duplicados.append(e)
    return no_duplicados
lista_numeros = [2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7]
print(type(lista_numeros))
print(len(lista_numeros))
resultado = remover_duplicados(lista_numeros)
print(resultado)
print(len(resultado))
print()
tupla_numeros = (2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7)
print(type(tupla_numeros))
print(len(tupla_numeros))
resultado = remover_duplicados(tupla_numeros)
print(resultado)
print(len(resultado))


# Ejercicio 544: Crear una función para comprobar si un número dado es primo.
def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
for i in range(1, 101):
    print(i, es_primo(i))


# Ejercicio 545: Crear una función para filtrar los números pares de una lista o tupla.
def filtrar_pares(numeros):
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares
lista_numeros = list(range(1, 11))
print(type(lista_numeros))
resultado = filtrar_pares(lista_numeros)
print(resultado)
print()
tupla_numeros = tuple(range(1, 11))
print(type(tupla_numeros))
resultado = filtrar_pares(tupla_numeros)
print(resultado)


# Ejercicio 546: Crear una función para determinar si un número es perfecto.
# 6 -> 1, 2, 3 => 1 + 2 + 3 = 6
# 28 -> 1 + 2 + 4 + 7 + 14 = 28
def es_numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero
print(es_numero_perfecto(6))
print(es_numero_perfecto(12)) # 1 + 2 + 3 + 4 + 6 = 16
print(es_numero_perfecto(28))
print(es_numero_perfecto(496))
print(es_numero_perfecto(8128))


# Ejercicio 547: Crear una función para determinar si una cadena es palíndromo.
# ana
# madam
def es_palindromo(cadena):
    posicion_izquierda = 0
    posicion_derecha = len(cadena) - 1
    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
            return False
        posicion_izquierda += 1
        posicion_derecha -= 1
    return True
print(es_palindromo('ana'))
print(es_palindromo('madam'))
print(es_palindromo('oso'))
print(es_palindromo('lateleletal'))
print(es_palindromo('python'))


# Ejercicio 548: Crear una función para generar n filas del triángulo de Pascal.
def triangulo_pascal(filas):
    fila = [1]
    cero = [0]
    for i in range(filas):
        print(fila)
        fila = [i + d for i, d in zip(fila + cero, cero + fila)]
triangulo_pascal(8)


# Ejercicio 549: Crear una función personalizada para comprobar si una frase es un pangrama.
from string import ascii_lowercase
def es_pangrama(frase):
    conjunto = set(ascii_lowercase)
    return conjunto <= set(frase.lower())
cadena = 'The quick brown fox jumps over the lazy dog'
print(es_pangrama(cadena))
print(es_pangrama('Python es un lenguaje de programación multiparadigma'))


# Ejercicio 550: Crear una función para crear una frase ordenada separada por guiones.
def separar_frase_guiones(frase):
    frase = frase.split()
    frase.sort()
    return '-'.join(frase)
cadena = 'python java c++ php c javascript'
print(cadena)
resultado = separar_frase_guiones(cadena)
print(resultado)


# Ejercicio 551: Crear función para generar números cuadrados para valores desde 1 hasta n.
def generar_cuadrados(n):
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i**2)
    return cuadrados
resultado = generar_cuadrados(10)
print(resultado)


# Ejercicio 552: Crear funciones decoradoras para aplicar etiquetas HTML a un texto.
def negrita(fn):
    def envoltura():
        return f'<b>{fn()}</b>'
    return envoltura
def cursiva(fn):
    def envoltura():
        return f'<i>{fn()}</i>'
    return envoltura
def subrayado(fn):
    def envoltura():
        return f'<u>{fn()}</u>'
    return envoltura
@negrita
@cursiva
@subrayado
def aplicar_etiquetas():
    return 'Python'
resultado = aplicar_etiquetas()
print(resultado)


# Ejercicio 553: Crear función para ejecutar código como cadena de caracteres.
def ejecutar_codigo(cadena):
    exec(cadena)
codigo = 'print("Python")'
ejecutar_codigo(codigo)
print()
codigo = """
def sumar(a, b):
    return a + b
print(sumar(2, 3))
"""
ejecutar_codigo(codigo)


# Ejercicio 554: Crear una función para invocar una función anidada.
def funcion_externa(a):
    def funcion_anidada(b):
        nonlocal a
        a += 1
        return a + b
    return funcion_anidada
resultado = funcion_externa(2)
print(resultado)
print(resultado(3))


# Ejercicio 555: Contar la cantidad de variables locales declaradas en una función.
def funcion(a, b):
    x = 1
    y = 2
    lenguaje = 'Python'
    print(x, y, lenguaje)
print(funcion.__code__.co_nlocals)


# Ejercicio 556: Crear una función lambda para sumar un valor a la constante 10.
sumar = lambda v: 10 + v
print(sumar(5))


# Ejercicio 557: Crear una función lambda para multiplicar dos números.
multiplicar = lambda x, y: x * y
resultado = multiplicar(2, 3)
print(resultado)


# Ejercicio 558: Crear una función lambda para replicar una cadena de caracteres n veces.
replicar = lambda c, n: c * n
resultado = replicar('Python', 5)
print(resultado)


# Ejercicio 559: Crear una función lambda para ordenar las tuplas contenidas en una lista.
productos = [('Mouse', 29.5), ('Audífonos', 19.9), ('Teclado', 59.0), ('Monitor', 259)]
print(productos)
print()
productos.sort(key=lambda p: p[1], reverse=True)
print(productos)


# Ejercicio 560: Crear una función lambda para ordenar una lista de diccionarios.
productos = [{'nombre': 'Teclado', 'precio': 55.9, 'color': 'Negro'}, {'nombre': 'Mouse', 'precio': 25.9, 'color': 'Gris'}, {'nombre': 'Monitor', 'precio': 255.9, 'color': 'Negro'}, {'nombre': 'Audífonos', 'precio': 39.9, 'color': 'Blanco'}, {'nombre': 'Mac', 'precio': 755.9, 'color': 'Plateado'}]
print(productos)
print()
productos = sorted(productos, key=lambda p: p['color'])
print(productos)


# Ejercicio 561: Crear una función lambda para filtrar los números pares de una lista.
numeros = list(range(1, 11))
print(numeros)
print()
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)


# Ejercicio 562: Crear una función lambda para filtrar números impares de una lista.
numeros = list(range(1, 11))
print(numeros)
print()
impares = list(filter(lambda n: n % 2 != 0, numeros))
print(impares)


# Ejercicio 563: Crear una función lambda para generar números cuadrados.
numeros = list(range(1, 11))
print(numeros)
print()
cuadrados = list(map(lambda n: n ** 2, numeros))
print(cuadrados)


# Ejercicio 564: Crear una función lambda para generar números cúbicos.
numeros = list(range(1, 11))
print(numeros)
print()
cubicos = list(map(lambda n: n ** 3, numeros))
print(cubicos)


# Ejercicio 565: Crear una función lambda para validar si una cadena inicia con un carácter.
inicia_con = lambda c: True if c.startswith('P') else False
cadena = 'Python'
print(inicia_con(cadena))
print()
print(inicia_con('python'))


# Ejercicio 566: Crear una función lambda para extraer las partes de un objeto fecha.
from datetime import datetime
ahora = datetime.now()
print(ahora)
print()
extrear_partes_fecha = lambda f: (f.year, f.month, f.day, f.time())
resultado = extrear_partes_fecha(ahora)
print(resultado)


# Ejercicio 567: Crear una función lambda para determinar si una cadena es un número.
es_numero = lambda n: n.replace('.', '', 1).isdigit()
print(es_numero('123.456'))
print(es_numero('123.456a'))
print(es_numero('-123.456'))
print(es_numero('123'))


# Ejercicio 568: Crear una función lambda para obtener valores de la serie Fibonacci.
from functools import reduce
generar_serie_fibonacci = lambda n: reduce(lambda a, _: a + [a[-1] + a[-2]], range(n-2), [0, 1])
valores = generar_serie_fibonacci(2)
print(valores)
valores = generar_serie_fibonacci(5)
print(valores)
valores = generar_serie_fibonacci(10)
print(valores)


# Ejercicio 569: Crear una función lambda para calcular la intersección entre dos arreglos.
numeros_1 = [2, 3, 5, 7, 11, 13]
numeros_2 = [1, 4, 5, 3, 11, 10, 19, 23]
print(numeros_1)
print(numeros_2)
print()
resultado = list(filter(lambda n: n in numeros_1, numeros_2))
print(resultado)


# Ejercicio 570: Crear una función lambda para convertir a mayúscula varias cadenas.
lenguajes = ['Python', 'JavaScript', 'Java', 'PHP', 'C++', 'Perl']
print(lenguajes)
print()
resultado = list(map(lambda c: c.upper(), lenguajes))
print(resultado)


# Ejercicio 571: Crear una función lambda para contar la cantidad de pares e impares.
numeros = list(range(1, 12))
print(numeros)
cantidad_pares = len(list(filter(lambda n: n % 2 == 0, numeros)))
cantidad_impares = len(list(filter(lambda n: n % 2 != 0, numeros)))
print(f'Cantidad de números pares: {cantidad_pares}')
print(f'Cantidad de números impares: {cantidad_impares}')


# Ejercicio 572: Crear una función lambda para obtener las palabras con longitud mayor a 5.
lenguajes = ['Python', 'PHP', 'C', 'C++', 'Java', 'JavaScript', 'C#']
print(lenguajes)
print()
resultado = filter(lambda l: len(l) > 5, lenguajes)
for e in resultado:
    print(e)


# Ejercicio 573: Crear una enumeración para representar los 4 puntos cardinales.
from enum import Enum
class PuntoCardinal(Enum):
    Norte = 1
    Sur = 2
    Este = 3
    Oeste = 4
print(PuntoCardinal.Norte.name)
print(PuntoCardinal.Norte.value)
print()
print(PuntoCardinal.Oeste.name)
print(PuntoCardinal.Oeste.value)


# Ejercicio 574: Iterar todos los elementos que contiene una enumeración en un ciclo for.
from enum import Enum
class PuntoCardinal(Enum):
    Norte = 1
    Sur = 2
    Este = 3
    Oeste = 4
for p in PuntoCardinal:
    print('{:10}: {}'.format(p.name, p.value))


# Ejercicio 575: Ordenar los nombres de una enumeración a partir de su valor.
from enum import IntEnum
class PuntoCardinal(IntEnum):
    Norte = 1
    Sur = 3
    Oeste = 4
    Este = 2
resultado = sorted(PuntoCardinal)
print(resultado)
resultado = '\n'.join(p.name for p in resultado)
print(resultado)


# Ejercicio 576: Obtener todos los valores declarados en una enumeración.
from enum import IntEnum
class PuntoCardinal(IntEnum):
    Norte = 1
    Sur = 3
    Oeste = 4
    Este = 2
valores = list(map(int, PuntoCardinal))
print(valores)


# Ejercicio 577: Encontrar la palabra más frecuente en una lista de cadenas de caracteres.
from collections import Counter
colores = [
   'Rojo', 'Verde', 'Negro', 'Rosado', 'Negro', 'Blanco', 'Negro', 'eyes',
   'Blanco', 'Negro', 'Naranja', 'Rosado', 'Rosado', 'Rojo', 'Rojo', 'Blanco', 'Naranja',
   'Blanco', "Negro", 'Rosado', 'Verde', 'Verde', 'Rosado', 'Verde', 'Rosado',
   'Blanco', 'Naranja', "Naranja", 'Rojo'
]
contador = Counter(colores)
color_mas_repetido = contador.most_common(1)
print(color_mas_repetido)


# Ejercicio 578: Agrupar valores de un conjunto de tuplas usando la clase defaultdict.
from collections import defaultdict
lenguajes = (('Python', '2'), ('Python', '3'), ('Java', '6'), ('Java', '7'), ('Java', '8'), ('C#', '5'), ('C#', '6'), ('C#', '7'))
agrupacion = defaultdict(list)
for l, v in lenguajes:
    agrupacion[l].append(v)
print(agrupacion)


# Ejercicio 579: Contar el número de ocurrencias de nombres de lenguajes de programación.
from collections import Counter
lenguajes = (('Python', '2'), ('Python', '3'), ('Java', '6'), ('Java', '7'), ('Java', '8'), ('C#', '5'), ('C#', '6'), ('C#', '7'), ('Java', '12'))
ocurrencias = Counter(l for l, v in lenguajes)
print(ocurrencias)


# Ejercicio 580: Crear una enumeración para representar colores básicos.
from enum import Enum
class Color(Enum):
    Negro = 1
    Blanco = 2
    Rojo = 3
    Verde = 4
    Azul = 5
print(Color.Negro)
print(Color.Blanco)


# Ejercicio 581: Crear un diccionario ordenado con la clase OrderedDict.
from collections import OrderedDict
nombres = {'Daniela': 27, 'Edward': 29, 'Germán': 31, 'John': 35}
diccionario_ordenado = OrderedDict(nombres.items())
for k in diccionario_ordenado:
    print(k, diccionario_ordenado[k])
print()
for k in reversed(diccionario_ordenado):
    print(k, diccionario_ordenado[k])


# Ejercicio 582: Crear una enumeración para representar los nombres de los días de la semana.
from enum import Enum
class Semana(Enum):
    Domingo = 1
    Lunes = 2
    Martes = 3
    Miércoles = 4
    Jueves = 5
    Viernes = 6
    Sabado = 7
domingo = Semana.Domingo
print(domingo)
numero_dia = 7


# Ejercicio 583: Comparar si dos listas no ordenadas contienen los mismos elementos.
from collections import Counter
def comparar_listas(a, b):
    return Counter(a) == Counter(b)
numeros_1 = [7, 5, 3, 2, 1, 11, 3, 2]
numeros_2 = [7, 13, 3, 2, 1, 11, 3, 2]
numeros_3 = [7, 5, 3, 2, 1, 11, 3, 2]
print(comparar_listas(numeros_1, numeros_2))
print(comparar_listas(numeros_2, numeros_3))
print(comparar_listas(numeros_1, numeros_3))


# Ejercicio 584: Crear un objeto array e iterar cada uno de sus elementos en un ciclo for.
from array import array
numeros = array('i', [2, 3, 5, 7, 11, 13])
print(numeros)
print(type(numeros))
print()
for n in numeros:
    print(n)


# Ejercicio 585: Consultar el tamaño en bytes de los elementos de un objeto array.
from array import array
enteros = array('i', [2, 3, 5])
print(enteros.itemsize)
print()
reales = array('d', [3.1415, 2.7172])
print(reales.itemsize)


# Ejercicio 586: Consultar la información de búfer de un objeto array con buffer_info().
from array import array
numeros = array('i', [2, 3, 5, 7, 11])
print(numeros.buffer_info())


# Ejercicio 587: Usar len() para consultar la cantidad de elementos de un objeto array.
from array import array
enteros = array('i', [2, 3, 5, 7, 11, 13, 17])
print(len(enteros))
enteros.append(19)
enteros.append(23)
print(len(enteros))


# Ejercicio 588: Convertir un objeto array a una lista usando el método tolist().
from array import array
primos = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print(primos)
print(len(primos))
print(type(primos))
print()
lista_primos = primos.tolist()
print(lista_primos)
print(len(lista_primos))
print(type(lista_primos))


# Ejercicio 589: Convertir un objeto array a su representación máquina en bytes.
from array import array
from binascii import hexlify
primos = array('i', [2, 3, 5, 7, 11, 13])
print(primos)
print()
arreglo_bytes = primos.tobytes()
print(hexlify(arreglo_bytes))


# Ejercicio 590: Convertir un arreglo de bytes a un objeto array con frombytes().
from array import array
from binascii import hexlify
primos = array('i', [2, 3, 5, 7, 11])
print(primos)
print()
arreglo_bytes = primos.tobytes()
print(hexlify(arreglo_bytes))
print()
primos_2 = array('i')
primos_2.frombytes(arreglo_bytes)
print(primos_2)


# Ejercicio 591: Uso básico de la estructura de datos incorporada heapq.
import heapq
cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))
for e in cola:
    print(e)


# Ejercicio 592: Extraer elementos de un objeto heapq con el método heappop().
import heapq
cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))
print(cola[0])
elemento = heapq.heappop(cola)
print(elemento)
print()
for e in cola:
    print(e)


# Ejercicio 593: Extraer y agregar elementos a una estructura de datos heapq.
import heapq
cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))
for e in cola:
    print(e)
print()
heapq.heappushpop(cola, ('PHP', '7.1.2'))
for e in cola:
    print(e)


# Ejercicio 594: Crear una función para ordenar una estructura de datos heapq.
import heapq
def ordenar(lista):
    cola = []
    for e in lista:
        heapq.heappush(cola, e)
    return [heapq.heappop(cola) for i in range(len(cola))]
numeros = [1, 2, 5, 7, 9, 2, 5, 4, 6, 8, 10]
print(numeros)
resultado = ordenar(numeros)
print(resultado)


# Ejercicio 595: Obtener el mínimo y el máximo de una lista con usando el módulo heapq.
import heapq
primos = [19, 11, 29, 3, 7, 37, 2, 5]
print('Mínimo:', heapq.nsmallest(1, primos))
print('Máximo:', heapq.nlargest(1, primos))


# Ejercicio 596: Localizar el punto de inserción de un elemento en una lista ordenada.
import bisect
def localizar_punto_insercion(lista, valor):
    indice = bisect.bisect_left(lista, valor)
    return indice
numeros = [2, 5, 7, 11]
numero = 3
print(localizar_punto_insercion(numeros, numero))
numero = 13
print(localizar_punto_insercion(numeros, numero))


# Ejercicio 597: Crear una entidad tipo namedtuple para representar datos de una persona.
from collections import namedtuple
Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad', 'email'])
edward = Persona('Edward', 'Ortiz', 29, 'edward@mail.co')
print(edward)
print(edward.nombre)
print(edward.apellido)
print(edward.edad)
print(edward.email)


# Ejercicio 598: Crear una entidad tipo namedtuple para representar datos de un producto.
from collections import namedtuple
Producto = namedtuple('Producto', ['nombre', 'codigo', 'cantidad', 'precio'])
computador = Producto('Computador gamer', 'ABC123', 100, 967)
print(computador)
print(computador.codigo)
print(computador.nombre)
print(computador.cantidad)
print(computador.precio)


# Ejercicio 599: Ordenar una lista de números con la función bisect().
from bisect import bisect, insort
def ordenar(lista):
    lista_ordenada = []
    for e in lista:
        posicion = bisect(lista_ordenada, e)
        insort(lista_ordenada, e)
    return lista_ordenada
numeros = [7, 2, 13, 5, 17, 19, 3, 11]
print(numeros)
resultado = ordenar(numeros)
print(resultado)


# Ejercicio 600: Uso de la clase Queue para crear una estructura de datos tipo cola.
from queue import Queue
clientes = Queue()
clientes.put('Edward')
clientes.put('Daniela')
clientes.put('Oliva')
clientes.put('Juan')
print(clientes.qsize())
print()
for c in list(clientes.queue):
    print(c, end=' ')


# Ejercicio 601: Comprobar si una cola está vacía a través del método de instancia empty().
from queue import Queue
q = Queue()
print(q.empty())
print()
for i in range(5):
    q.put(i)
print(q.empty())


# Ejercicio 602: Recorrer todos los elementos de una cola por medio de un ciclo while.
from queue import Queue
q = Queue()
for i in range(5):
    q.put(i)
print(q.qsize())
print()
while not q.empty():
    print(q.get(), end=' ')


# Ejercicio 603: Usar la clase LifoQueue para crear una estructura LIFO (Last-In-First-Out).
from queue import LifoQueue
pila = LifoQueue()
for i in range(1, 6):
    pila.put(i)
print(pila.qsize())
print()
while not pila.empty():
    print(pila.get())


# Ejercicio 604: Uso de la clase PriorityQueue para priorizar elementos de datos.
from queue import PriorityQueue
class Curso(object):
    def __init__(self, prioridad, nombre):
        self.prioridad = prioridad
        self.nombre = nombre
    def __lt__(self, otro):
        return self.prioridad < otro.prioridad
cursos = PriorityQueue()
cursos.put(Curso(3, 'Python'))
cursos.put(Curso(10, 'C++'))
cursos.put(Curso(1, 'Algoritmia'))
while not cursos.empty():
    c = cursos.get()
    print(c.prioridad, c.nombre)


# Ejercicio 605: Uso de la clase SimpleQueue del módulo incorporado queue.
from queue import SimpleQueue
q = SimpleQueue()
for i in range(1, 6):
    q.put(i)
print(q.qsize())
print()
while not q.empty():
    print(q.get())


# Ejercicio 606: Crear una función para el algoritmo de búsqueda binaria sobre una lista.
def busqueda_binaria(lista, valor):
    primero = 0
    ultimo = len(lista) - 1
    encontrado = False
    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2
        if lista[mitad] == valor:
            encontrado = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1
    return encontrado
numeros = [2, 3, 5, 7, 11, 13, 17, 19]
llave = 10
print(busqueda_binaria(numeros, llave))
llave = 2
print(busqueda_binaria(numeros, llave))
llave = 19
print(busqueda_binaria(numeros, llave))

# Ejercicio 607: Crear una función para el algoritmo de búsqueda secuencial sobre una lista.
def busqueda_secuencial(lista, valor):
    posicion = 0
    encontrado = False
    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1
    return encontrado, posicion
numeros = [2, 7, 3, 5, 13, 31, 29, 17, 19]
llave = 37
print(busqueda_secuencial(numeros, llave))
llave = 5
print(busqueda_secuencial(numeros, llave))
llave = 19
print(busqueda_secuencial(numeros, llave))


# Ejercicio 608: Crear función para el algoritmo para búsqueda binaria en una lista ordenada.
def busqueda_binaria_lista_ordenada(lista, valor):
    if len(lista) == 0:
        return False
    else:
        mitad = len(lista) // 2
        if lista[mitad] == valor:
            return True
        else:
            if valor < lista[mitad]:
                return busqueda_binaria(lista[:mitad], valor)
            else:
                return busqueda_binaria(lista[mitad + 1:], valor)
def busqueda_binaria(lista, valor):
    primero = 0
    ultimo = len(lista) - 1
    encontrado = False
    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2
        if lista[mitad] == valor:
            encontrado = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1
    return encontrado
numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31]
llave = 37
print(busqueda_binaria_lista_ordenada(numeros, llave))
llave = 11
print(busqueda_binaria_lista_ordenada(numeros, llave))
print(busqueda_binaria_lista_ordenada([], llave))


# Ejercicio 609: Crear una función para el algoritmo de ordenamiento burbuja sobre una lista.
def ordenamiento_burbuja(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
numeros = [7, 19, 2, 13, 5, 23, 29, 11, 17]
print(numeros)
ordenamiento_burbuja(numeros)
print(numeros)


# Ejercicio 610: Crear una función para el algoritmo de ordenamiento por selección.
def ordenamiento_seleccion(lista):
    for n in range(len(lista) - 1, 0, -1):
        posicion_maxima = 0
        for l in range(1, n + 1):
            if lista[l] > lista[posicion_maxima]:
                posicion_maxima = l
        temp = lista[n]
        lista[n] = lista[posicion_maxima]
        lista[posicion_maxima] = temp
numeros = [19, 17, 2, 29, 3, 5, 11, 7, 13]
print(numeros)
ordenamiento_seleccion(numeros)
print(numeros)


# Ejercicio 611: Crear una función para el algoritmo de ordenamiento shell.
def shell(lista):
    mitad = len(lista) // 2
    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista, p, mitad)
        mitad = mitad // 2
def reducir_busqueda(lista, inicio, salto):
    for i in range(inicio + salto, len(lista), salto):
        valor = lista[i]
        posicion = i
        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        lista[posicion] = valor
numeros = [7, 2, 11, 3, 1, 13, 5]
print(numeros)
shell(numeros)
print(numeros)


# Ejercicio 612: Crear una función para el algoritmo de ordenamiento merge sort.
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]
        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0
        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1
numeros = [13, 5, 2, 19, 11, 7, 1, 3]
print(numeros)
merge_sort(numeros)
print(numeros)


# Ejercicio 613: Crear una función para el algoritmo de ordenamiento quicksort.
def quick_sort(lista):
    quick_sort_auxiliar(lista, 0, len(lista) - 1)
def quick_sort_auxiliar(lista, inicio, fin):
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)
        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)
def particionar(lista, inicio, fin):
    pivote = lista[inicio]
    izquierda = inicio + 1
    derecha = fin
    terminado = False
    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1
        if derecha < izquierda:
            terminado = True
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]
    return derecha
numeros = [7, 3, 2, 13, 5, 7, 11, 1]
print(numeros)
quick_sort(numeros)
print(numeros)


# Ejercicio 614: Crear una función para el algoritmo de ordenamiento por cuentas.
def ordenamiento_cuentas(lista):
    maximo = max(lista) + 1
    conteo = [0] * maximo
    for n in lista:
        conteo[n] += 1
    i = 0
    for j in range(maximo):
        for k in range(conteo[j]):
            lista[i] = j
            i += 1
    return lista
numeros = [2, 3, 8, 4, 3, 2, 5, 3, 4, 3, 2]
print(numeros)
numeros = ordenamiento_cuentas(numeros)
print(numeros)


# Ejercicio 615: Crear una función personalizada para la generación de contraseñas.
import string
import random
def generador_clave(tamagnio = 10, caracteres=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(caracteres) for _ in range(tamagnio))
print(generador_clave())
print(generador_clave(8))
print(generador_clave(8))


# Ejercicio 616: Leer un archivo de texto para contar las ocurrencias de nombres almacenados.
def contar_ocurrencias_nombres(nombre_archivo):
    ocurrencias = {}
    with open(nombre_archivo, 'r') as f:
        nombre = f.readline()
        while nombre:
            nombre = nombre.strip()
            if nombre in ocurrencias:
                ocurrencias[nombre] += 1
            else:
                ocurrencias[nombre] = 1
            nombre = f.readline()
    return ocurrencias
resultado = contar_ocurrencias_nombres('Parte001/nombres_star_wars.txt')
print(resultado)


# Ejercicio 617: Calcular el mayor de tres números pasados como argumentos desde la línea de comandos.
import sys
if len(sys.argv) == 4:
    numero_1 = sys.argv[1]
    numero_2 = sys.argv[2]
    numero_3 = sys.argv[3]
    if numero_1.isnumeric() and numero_2.isnumeric() and numero_3.isnumeric():
        mayor = max(int(numero_1), int(numero_2), int(numero_3))
        print('El número mayor es: {}'.format(mayor))
    else:
        print('Los valores deben ser de tipo numérico.')
else:
    print('Uso: <valor_1> <valor_2> <valor_3>')
    sys.exit(1)


# Ejercicio 618: Seleccionar de forma aleatoria una palabra desde un archivo de texto plano.
import random
def seleccionar_palabra_aleatoria(nombre_archivo):
    palabras = []
    with open(nombre_archivo, 'r') as f:
        palabra = f.readline().strip()
        palabras.append(palabra)
        while palabra:
            palabra = f.readline().strip()
            palabras.append(palabra)
    return random.choice(palabras)
for _ in range(10):
    print(seleccionar_palabra_aleatoria('Parte001/palabras_ingles.txt'))


# Ejercicio 619: Seleccionar de forma aleatoria una palabra desde un archivo de texto plano.
import random
def seleccionar_palabra_aleatoria(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        palabras = list(f)
    return random.choice(palabras).strip()
for _ in range(10):
    print(seleccionar_palabra_aleatoria('Parte001/palabras_ingles.txt'))


# Ejercicio 620: Crear generador de la serie Fibonacci usando memoización.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
def fibonacci(n):
    if n == 0:
        serie_fibonacci = []
    elif n == 1:
        serie_fibonacci = [1]
    elif n == 2:
        serie_fibonacci = [0, 1]
    elif n > 2:
        serie_fibonacci = [0, 1]
        i = 1
        while i < n - 1:
            serie_fibonacci.append(serie_fibonacci[i] + serie_fibonacci[i - 1])
            i += 1
    return serie_fibonacci
resultado = fibonacci(11)
print(len(resultado))
print(resultado)


# Ejercicio 621: Crear una función para generar n cantidad de múltiplos de un número.
def generar_multiplos(numero, n):
    return [numero * i for i in range(1, n + 1)]
print(generar_multiplos(7, 10))
print(generar_multiplos(12, 7))


# Ejercicio 622: A partir de un diccionario con los datos de compra y venta calcular la ganancia.
# {
#   "precio_costo": 30.0,
#   "precio_venta": 42.0,
#   "inventario": 1200
# }
def calcular_ganancia(producto):
    ganancia = producto['precio_venta'] * producto['inventario']
    ganancia -= producto['precio_costo'] * producto['inventario']
    return ganancia
producto = {
  "precio_costo": 30.0,
  "precio_venta": 42.0,
  "inventario": 1200
}
resultado = calcular_ganancia(producto)
print('La ganacia total es: %f' % resultado)


# Ejercicio 623: Cambiar el formato de una fecha representada como una cadena de caracteres.
# 02/12/2019 -> 20191202
def cambiar_formato_fecha(fecha):
    partes_fecha = fecha.split('/')
    return '{}{}{}'.format(partes_fecha[2], partes_fecha[1], partes_fecha[0])
print(cambiar_formato_fecha('02/12/2019'))
print(cambiar_formato_fecha('14/02/2020'))


# Ejercicio 624: Crear una función para validar si un número dado es Sastry.
# n = 183
# n + = 184
# 183184
# x ^ 2 = 183184
# 428
from math import isqrt, sqrt
def es_Sastry(numero):
    sucesor = numero + 1
    resultado = int('{}{}'.format(numero, sucesor))
    return isqrt(resultado) == sqrt(resultado)
print(es_Sastry(183))
print(es_Sastry(23))


# Ejercicio 625: Crear una función para contar cuántas soluciones tiene una ecuación cuadrática.
# a*x^2 + b*x + c = 0
def soluciones_ecuacion_cuadratica(coeficientes):
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]
    determinante = b**2 - 4 * a * c
    if determinante >= 0:
        if a != 0:
            if determinante == 0:
                return 1
            else:
                return 2
        else:
            return 0
    else:
        return 0
print(soluciones_ecuacion_cuadratica((1, 0, 1)))
print(soluciones_ecuacion_cuadratica((1, 0, 0)))
print(soluciones_ecuacion_cuadratica((1, 0, -1)))


# Ejercicio 626: Crear una función para contar las letras repetidas de una palabra.
# caballo -> a, l
from collections import Counter
def contar_letras_repetidas(texto):
    contador = Counter(texto)
    duplicados = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(duplicados)
texto = 'caballo'
print(contar_letras_repetidas(texto))
print(contar_letras_repetidas('serrucho'))
print(contar_letras_repetidas('programación'))
print(contar_letras_repetidas('Python'))


# Ejercicio 627: Crear una función para sumar o concatenar valores de manera polimórfica.
# 1 + 2 => 3
# '1' + '2' => '12'
# 1 + '2' => '12'
def suma_polimorfica(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return '{}{}'.format(a, b)
print(suma_polimorfica(1, 2))
print(suma_polimorfica(1, '2'))
print(suma_polimorfica('1', '2'))
print(suma_polimorfica('1', 2))


# Ejercicio 628: Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b*x + c = 0
# a, b, c
from math import sqrt
def resolver_ecuacion(a, b, c):
    determinante = b**2 - 4*a*c
    if determinante > 0:
        x_1 = -b + sqrt(b**2 - 4*a*c) / (2*a)
        x_2 = -b - sqrt(b**2 - 4*a*c) / (2*a)
        return x_1, x_2
    elif determinante == 0:
        x_1 = -b / (2*a)
        return (x_1,)
    else:
        return tuple()
print(resolver_ecuacion(1, 0, 0))
print(resolver_ecuacion(1, 0, 1))
print(resolver_ecuacion(1, 0, -1))


# Ejercicio 629: Crear una función para sumar fracciones y redondear al número entero más cercano.
def sumar_fracciones(fracciones):
    suma = 0
    for f in fracciones:
        suma += f[0]/f[1]
    return round(suma)
numeros = [(2, 3), (1, 2), (3, 2), (1, 3)]
resultado = sumar_fracciones(numeros)
print(resultado)


# Ejercicio 630: Crear una clase para representar una lista simplemente enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
for d in numeros.iterar():
    print(d)


# Ejercicio 631: Escribir la lógica para contar los elementos de una lista enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)


# Ejercicio 632: Implementar método para la búsqueda de un dato en una lista enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        return False
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))


# Ejercicio 633: Obtener un dato desde una lista enlazada a través de su índice.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        return False
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))
print()
primos = [2, 3, 5, 7]
print(primos[1])
print(primos[3])
print(primos[-1])
print()
# print(numeros[-1]) # Genera excepción
print(numeros[0])
print(numeros[3])
# print(numeros[4]) # Genera excepción


# Ejercicio 634: Cambiar un dato en una lista enlazada a través de su índice.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        return False
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    def __setitem__(self, indice, nuevo_dato):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            actual.dato = nuevo_dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))
print()
primos = [2, 3, 5, 7]
print(primos[1])
print(primos[3])
print(primos[-1])
print()
# print(numeros[-1]) # Genera excepción
print(numeros[0])
print(numeros[3])
# print(numeros[4]) # Genera excepción
print()
# numeros[-1] = 1 # Genera excepción
print(numeros[3])
numeros[3] = 11
print(numeros[3])
# numeros[4] = 13 # Genera excepción


# Ejercicio 635: Eliminar la primera ocurrencia de un dato desde una lista enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1
        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    def iterar(self):
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        return False
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    def __setitem__(self, indice, nuevo_dato):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            actual.dato = nuevo_dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    def eliminar_dato(self, dato):
        actual = self.cola
        anterior = self.cola
        while actual:
            if actual.dato == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    # [2]->[3]->[5] => [2]->[5]
                    anterior.siguiente = actual.siguiente
                self.tamagnio -= 1
                return
            anterior = actual
            actual = actual.siguiente
numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar(5)
numeros.insertar(7)
print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)
print()
for d in numeros.iterar():
    print(d)
print()
print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))
print()
primos = [2, 3, 5, 7]
print(primos[1])
print(primos[3])
print(primos[-1])
print()
# print(numeros[-1]) # Genera excepción
print(numeros[0])
print(numeros[3])
# print(numeros[4]) # Genera excepción
print()
# numeros[-1] = 1 # Genera excepción
print(numeros[3])
numeros[3] = 11
print(numeros[3])
# numeros[4] = 13 # Genera excepción
print()
# Eliminar la primera ocurrencia de una lista enlazada:
# 2 3 5 11
print('Cantidad de elementos antes de la inserción: ', numeros.tamagnio)
numeros.insertar(5)
print('Cantidad de elementos después de la inserción: ', numeros.tamagnio)
# 2 3 5 11 5
print()
numeros.eliminar_dato(5)
print('Después de la eliminación hay', numeros.tamagnio)
numeros.eliminar_dato(13)
print('Después de intentar eliminar el valor 11 hay', numeros.tamagnio, ' numeros')
numeros.eliminar_dato(11)
print('Cantidad de elementos después de la última eliminación:', numeros.tamagnio)


# Ejercicio 636: Crear una clase para representar una lista doblemente enlazada.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)


# Ejercicio 637: Crear método de inserción al principio de una lista doblemente enlazada.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            self.contador += 1
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)
for d in numeros.iterar():
    print(d)


# Ejercicio 638: Crear método para buscar dato en una lista doblemente enlazada.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            self.contador += 1
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        return False
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)
for d in numeros.iterar():
    print(d)
print()
print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', numeros.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', numeros.buscar(numero))


# Ejercicio 639: Crear método para eliminar un dato de una lista doblemente enlazada.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            self.contador += 1
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        return False
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        if eliminado:
            self.contador -= 1
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)
for d in numeros.iterar():
    print(d)
print()
print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', numeros.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', numeros.buscar(numero))
print()
print('Eliminación de datos:')
numero = 1
print('Cantidad de elementos antes de la eliminación:', numeros.contador)
numeros.eliminar(numero)
print('Cantidad de elementos después de la eliminación:', numeros.contador)
print('¿Este el valor 1 en la lista?:', numeros.buscar(numero))


# Ejercicio 640: Obtener un dato desde una lista doblemente enlazada a través de su índice.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            self.contador += 1
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        return False
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        if eliminado:
            self.contador -= 1
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)
for d in numeros.iterar():
    print(d)
print()
print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', numeros.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', numeros.buscar(numero))
print()
print('Eliminación de datos:')
numero = 1
print('Cantidad de elementos antes de la eliminación:', numeros.contador)
numeros.eliminar(numero)
print('Cantidad de elementos después de la eliminación:', numeros.contador)
print('¿Este el valor 1 en la lista?:', numeros.buscar(numero))
print()
print('Acceso a un elemento por medio de su índice:')
# indice = -1
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción
indice = 0
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 2
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 3
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 4
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
# indice = 7
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción


# Ejercicio 641: Modificar un dato en una lista doblemente enlazada a través de su índice.
class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.contador += 1
    def iterar(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            self.contador += 1
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        return False
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        if eliminado:
            self.contador -= 1
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente
            actual.dato = dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)
print()
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)
print('Cantidad actual de elementos:', numeros.contador)
print()
for d in numeros.iterar():
    print(d)
print()
numeros.insertar_inicio(0)
numeros.insertar_inicio(1)
print('Cantidad de elementos después de insertar el valor cero:', numeros.contador)
for d in numeros.iterar():
    print(d)
print()
print('Búsqueda de un dato')
numero = 19
print('¿Se halla 19 en la lista?:', numeros.buscar(numero))
numero = 7
print('¿Se halla 7 en la lista?:', numeros.buscar(numero))
print()
print('Eliminación de datos:')
numero = 1
print('Cantidad de elementos antes de la eliminación:', numeros.contador)
numeros.eliminar(numero)
print('Cantidad de elementos después de la eliminación:', numeros.contador)
print('¿Este el valor 1 en la lista?:', numeros.buscar(numero))
print()
print('Acceso a un elemento por medio de su índice:')
# indice = -1
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción
indice = 0
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 2
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 3
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
indice = 4
print('Valor en la posición %i es igual a %i' % (indice, numeros[indice]))
# indice = 7
# print('Valor en la posición %i es igual a %i' % (indice, numeros[indice])) # Genera excepción
print()
print('Modificación valores de la lista a partir de un índice:')
# numeros[-1] = 19 # Genera excepción
print('Cantidad actual de elementos: %i' % numeros.contador)
print('Contenido en la posición 5 antes de la modificación: %i' % numeros[5])
numeros[5] = 17
print('Contenido en la posición 5 después de la modificación: %i' % numeros[5])
 
 
 # Ejercicio 642: Implementar clase para un nodo de un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
  
  
  # Ejercicio 643: Crear función para insertar un nodo en un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
 
 
 # Ejercicio 644: Crear función para recorrido inorden de un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))
inorden(raiz)
 
 
 # Ejercicio 645: Crear función para recorrido preorden de un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)
def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))
inorden(raiz)
print()
preorden(raiz)
 
 
 # Ejercicio 646: Crear función para recorrido postorden de un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)
def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))
inorden(raiz)
print()
preorden(raiz)
print()
postorden(raiz)
 
 
 # Ejercicio 647: Crear función para buscar un dato en un árbol binario de búsqueda.
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)
def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)
def buscar_dato(raiz, dato):
    if raiz is None:
        return False
    elif raiz.dato == dato:
        return True
    elif dato < raiz.dato:
        return buscar_dato(raiz.izquierda, dato)
    else:
        return buscar_dato(raiz.derecha, dato)
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))
inorden(raiz)
print()
preorden(raiz)
print()
postorden(raiz)
print()
print(buscar_dato(raiz, 2))
print(buscar_dato(raiz, 10))
print(buscar_dato(raiz, 100))


# Ejercicio 648: Crear función recursiva para sumar los elementos de una lista.
def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sumar_lista(numeros)
print('La suma de los valores de 1 a 5 es igual a %i' % resultado)
print()
primos = []
resultado = sumar_lista(primos)
print(resultado)


# Ejercicio 649: Crear función recursiva para sumar los elementos de una lista mixta.
# [1, 2, [2, 3], [[4, 5]], [[[6]]]]
def sumar_lista_mixta(lista):
    total = 0
    for l in lista:
        if type(l) == type([]):
            total += sumar_lista_mixta(l)
        else:
            total += l
    return total
numeros = [1, 2, [2, 3], [[4, 5]], [[[6]]], [], []]
resultado = sumar_lista_mixta(numeros)
print(resultado)


# Ejercicio 650: Crear una función recursiva para convertir un entero a cualquier base.
def convertir_entero_base(numero, base):
    conversion_cadena = '0123456789ABCDEF'
    if numero < base:
        return conversion_cadena[numero]
    else:
        return convertir_entero_base(numero//base, base) + conversion_cadena[numero % base]
numero = 13
base = 8
resultado = convertir_entero_base(numero, base)
print(resultado)
# convertir_entero_base(1, 8) + '5' => '1' + '5'
# numero = 1, base = 8
# 


# Ejercicio 651: Crear una función recursiva para calcular el factorial de un número.
# 5! = 1 * 2 * 3 * 4 * 5 = 120
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # 120
print(factorial(6)) # 720
print(factorial(7)) # 5040


# Ejercicio 651: Crear una función recursiva para calcular el enésimo valor de Fibonacci.
# 0 1 1 2 3 5 8 13 21 34 55 89, ...
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(9))


# Ejercicio 653: Crear una función recursiva para sumar los dígitos de un número entero.
# 253 => 2, 5, 3 => 2 + 5 + 3 = 10
def sumar_digitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)
print(sumar_digitos(253)) # 10
print(sumar_digitos(123)) # 6
print(sumar_digitos(12345)) # 15


# Ejercicio 654: Crear función recursiva para sumar los valores n+(n-2)+(n-4) hasta n-x <= 0.
def sumar_valores(n):
    if n < 1:
        return 0
    else:
        return n + sumar_valores(n - 2)
print(sumar_valores(8))
# n = 8
# 8 + 12 = 20
#   n = 6
#   6 + 6
#       n = 4
#       4 + 2
#           n = 2
#           2 + 0
#               n = 0


# Ejercicio 655: Crear una función recursiva para calcular la suma armónica.
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
def suma_armonica(n):
    if n < 2:
        return 1
    else:
        return 1/n + suma_armonica(n - 1)
resultado = suma_armonica(7)
print(resultado)


# Ejercicio 656: Crear una función recursiva para calcular la potencia de un número.
# a^b = a_1 * a_2 * a_3 * ... * a_b
def potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * potencia(a, b - 1)
# 2 ^ 4 = 16
print(potencia(2, 4))
# 4 ^ 3 = 4 * 4 * 4 = 64
print(potencia(4, 3))
# 3 ^ 4 = 3 * 3 * 3 * 3 = 81
print(potencia(3, 4))


# Ejercicio 657: Crear una función recursiva para calcular el máximo común divisor (MCD).
def mcd(a, b):
    minimo = min(a, b)
    maximo = max(a, b)
    if minimo == 0:
        return maximo
    elif minimo == 1:
        return 1
    else:
        return mcd(minimo, maximo % minimo)
print(mcd(4, 12)) # 4
print(mcd(6, 12)) # 6
print(mcd(3, 4)) # 3 => 1, 3, 4 => 1, 2, 4


# Ejercicio 658: Obtener las partes esenciales de una fecha con el módulo datetime.
import datetime
ahora = datetime.datetime.now()
print('Fecha y hora actuales:', ahora)
hoy = datetime.date.today()
print('Hoy:', hoy)
print()
print('Año:', hoy.strftime('%Y'))
print('Nombre del mes:', hoy.strftime('%B'))
print('Número de la semana en el año:', hoy.strftime('%W'))
print('Número del día de la semana:', hoy.strftime('%w'))
print('Número del día del año:', hoy.strftime('%j'))
print('Número del día en el mes:', hoy.strftime('%d'))
print('Nombre del día de la semana:', hoy.strftime('%A'))


# Ejercicio 659: Crear una función para determinar si un año es bisiesto.
def es_bisiesto(agnio):
    if agnio % 400 == 0:
        return True
    elif agnio % 100 == 0:
        return False
    elif agnio % 4 == 0:
        return True
    else:
        return False
agnio = 2020
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2013
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2000
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))


# Ejercicio 660: Crear una función para convertir una cadena de caracteres a un objeto fecha.
from datetime import datetime
def convertir_cadena_a_fecha(cadena):
    fecha = datetime.strptime(cadena, '%b %d %Y %I:%M:%S')
    return fecha
cadena_fecha = 'Feb 22 2020 10:05:17'
fecha = convertir_cadena_a_fecha(cadena_fecha)
print(type(fecha))
print(fecha)


# Ejercicio 661: Obtener la hora actual por medio de la función time() de la clase datetime.
from datetime import datetime
hora = datetime.now().time()
print(hora)
print(type(hora))


# Ejercicio 662: Substraer 10 días a la fecha actual usando un objeto timedelta.
from datetime import date, timedelta
fecha_actual = date.today()
resultado = fecha_actual - timedelta(10)
print('Fecha actual:', fecha_actual)
print('10 días antes de la fecha actual:', resultado)


# Ejercicio 663: Convertir segundos del tiempo Unix a un objeto fecha con fromtimestamp().
import datetime
segundos_unix = 1435554000
fecha = datetime.datetime.fromtimestamp(segundos_unix)
print(type(fecha))
print(fecha)


# Ejercicio 664: Obtener la fecha de ayer, hoy y mañana con un objeto timedelta.
import datetime
hoy = datetime.date.today()
ayer = hoy - datetime.timedelta(1)
manana = hoy + datetime.timedelta(1)
print('Ayer:', ayer)
print('Hoy:', hoy)
print('Mañana:', manana)


# Ejercicio 665: Convertir un objeto date a un objeto datetime con combine().
from datetime import date, datetime
hoy = date.today()
print(type(hoy))
print(hoy)
print()
dt = datetime.combine(hoy, datetime.min.time())
print(type(dt))
print(dt)


# Ejercicio 666: Generar diez fechas a partir de la fecha actual.
import datetime
hoy = datetime.datetime.today()
print('Fecha actual:', hoy)
fechas = [hoy + datetime.timedelta(dia) for dia in range(1, 11)]
for f in fechas:
    print(f)


# Ejercicio 667: Sumar 5 segundos a la hora actual por medio de timedelta.
import datetime
hora_actual = datetime.datetime.now()
print('Hora actual:', hora_actual)
resultado = hora_actual + datetime.timedelta(seconds=5)
print('Hora más 5 segundos:', resultado)


# Ejercicio 668: Obtener el número del día del año en curso.
import datetime
hoy = datetime.datetime.now()
numero_dia = (hoy - datetime.datetime(hoy.year, 1, 1)).days + 1
print('Número día del año:', numero_dia)


# Ejercicio 669: Obtener la cantidad de milisegundos transcurridos desde el inicio del tiempo Unix.
# Tiempo Unix: 1 enero, 1970
import time
segundos = time.time()
milisegundos = int(round(segundos * 1000))
print('Milisegundos desde el inicio del tiempo Unix: %i' % milisegundos)


# Ejercicio 670: Obtener el número de la semana actual del año en curso.
import datetime
fecha_actual = datetime.date.today()
print('Fecha actual:', fecha_actual)
numero_semana = fecha_actual.isocalendar()
print('Número de la semana del año en curso:', numero_semana[1])


# Ejercicio 671: Obtener la fecha del primer lunes del número de una semana específica.
import time
numero_semana = 8
fecha = time.asctime(time.strptime('2020 8 1', '%Y %W %w'))
print('Fecha primer lunes semana número 8:', fecha)
print(type(fecha))


# Ejercicio 672: Obtener todas las fechas de los domingos de un año particular.
from datetime import date, timedelta
def generar_fecha_domingo(agnio):
    fecha = date(agnio, 1, 1)
    fecha += timedelta(days=6-fecha.weekday())
    while fecha.year == agnio:
        yield fecha
        fecha += timedelta(days=7)
for f in generar_fecha_domingo(2020):
    print(f)


# Ejercicio 673: Crear una función para sumar n cantidad de años a una fecha.
import datetime
from datetime import date
def sumar_agnios(fecha, agnios):
    try:
        return fecha.replace(year = fecha.year + agnios)
    except ValueError:
        return fecha + (date(fecha.year + agnios, 1, 1) - date(fecha.year, 1, 1))
fecha = date(2020, 1, 13)
print(sumar_agnios(fecha, 2))
print(sumar_agnios(fecha, -2))
print()
fecha = date(2020, 2, 29)
print(sumar_agnios(fecha, 1))
print(sumar_agnios(fecha, 4))


# Ejercicio 674: Remover los microsegundos de un objeto datetime usando replace().
import datetime
hoy = datetime.datetime.today()
print('Fecha actual:', hoy)
hoy = hoy.replace(microsecond=0)
print('Fecha actual (sin microsegundos):', hoy)


# Ejercicio 675: Diferencia en días entre dos fechas (objetos date).
from datetime import date
fecha_1 = date(2010, 1, 1)
fecha_2 = date(2020, 1, 1)
diferencia = fecha_2 - fecha_1
print(f'Diferencia total en días: {diferencia.days}')


# Ejercicio 676: Crear una función para obtener la fecha del último martes.
from datetime import date, timedelta
def fecha_ultimo_martes():
    hoy = date.today()
    dias = (hoy.weekday() - 1) % 7
    ultimo_martes = hoy - timedelta(days=dias)
    return ultimo_martes
resultado = fecha_ultimo_martes()
print('Fecha último martes:', resultado)


# Ejercicio 677: Crear una función para determinar si una fecha es el tercer miércoles del mes.
import datetime
def es_tercer_miercoles(cadena):
    fecha = datetime.datetime.strptime(cadena, '%Y %m %d')
    return fecha.weekday() == 2 and 14 < fecha.day <= 22
print(es_tercer_miercoles('2020 02 17'))
print(es_tercer_miercoles('2020 02 19'))
print(es_tercer_miercoles('2020 01 22'))


# Ejercicio 678: Crear una función para encontrar el último número de día de un mes y un año.
import calendar
def ultimo_numero_dia(mes, agnio):
    return calendar.monthrange(agnio, mes)
print(ultimo_numero_dia(2, 2020)[1])
print(ultimo_numero_dia(12, 2020)[1])


# Ejercicio 679: Crear función para obtener la cantidad de días de un mes de un año específico.
from calendar import monthrange
def cantidad_dias_mes(mes, agnio):
    return monthrange(agnio, mes)[1]
print(cantidad_dias_mes(2, 2020))
print(cantidad_dias_mes(2, 2021))


# Ejercicio 680: Crear una función para sumar un mes a una fecha.
from datetime import date, timedelta
from calendar import monthrange
def cantidad_dias_mes(mes, agnio):
    """
    Obtiene la cantidad de días de un mes y año específicos.
    """
    return monthrange(agnio, mes)[1]
def sumar_mes_fecha(fecha):
    dias_mes = cantidad_dias_mes(fecha.month, fecha.year)
    resultado = fecha + timedelta(days=dias_mes)
    return resultado
fecha = date(2020, 12, 31)
resultado = sumar_mes_fecha(fecha)
print(resultado)


# Ejercicio 681: Contar la cantidad de lunes que son el primer día de cada mes en un rango de años.
from datetime import datetime
def cantidad_lunes_primer_dia_mes(agnio_1, agnio_2):
    contador = 0
    for a in range(agnio_1, agnio_2 + 1):
        for m in range(1, 13):
            if datetime(a, m, 1).weekday() == 0:
                contador += 1
    return contador
agnio_1 = 2018
agnio_2 = 2020
resultado = cantidad_lunes_primer_dia_mes(agnio_1, agnio_2)
print(resultado)
print(cantidad_lunes_primer_dia_mes(2020, 2020))


# Ejercicio 682: Crear función para imprimir un texto específico cada 3 segundos.
import time
def imprimir_texto(texto, n, intervalo=3):
    for _ in range(n):
        print(texto)
        time.sleep(intervalo)
imprimir_texto('¡Python es tremendo!', 5)


# Ejercicio 683: Sumar seis (6) meses a una fecha específica usando timedelta.
from datetime import date, timedelta
fecha_actual = date.today()
seis_meses_despues = fecha_actual + timedelta(365/2)
print('Fecha actual:', fecha_actual)
print('Seis meses después:', seis_meses_despues)


# Ejercicio 684: Generar hasta doce (12) fechas diferenciadas cada una por 15 días.
from datetime import date, timedelta
def generar_fechas(fecha_inicio, cantidad=12, dias_diferencia=15):
    fechas = []
    fechas.append(fecha_inicio)
    for _ in range(cantidad):
        fecha_inicio = fecha_inicio + timedelta(days=dias_diferencia)
        fechas.append(fecha_inicio)
    return fechas
fecha = date.today()
resultado = generar_fechas(fecha)
print('Fecha actual:', fecha)
for f in resultado:
    print(f)


# Ejercicio 685: Generar las fechas de hace 30 días y después de 30 días a partir de la actual.
from datetime import date, timedelta
def generar_fechas_30_dias():
    fecha_actual = date.today()
    hace_30_dias = fecha_actual - timedelta(days=30)
    despues_30_dias = fecha_actual + timedelta(days=30)
    return hace_30_dias, fecha_actual, despues_30_dias
resultado = generar_fechas_30_dias()
print(resultado)


# Ejercicio 686: Generar la fecha UTC (Universal Time Coordinated) con timezone.utc.
from datetime import datetime, timezone
fecha_utc = datetime.now(timezone.utc)
print(fecha_utc.strftime('%Y-%m-%d %H:%M:%S%z'))


# Ejercicio 687: Convertir un objeto fecha (datetime) a una marca de tiempo (timestamp).
import datetime
import time
def convertir_fecha_timestamp(fecha):
    fecha = fecha.timetuple()
    resultado = time.mktime(fecha)
    return resultado
ahora = datetime.datetime.now()
print(convertir_fecha_timestamp(ahora))


# Ejercicio 688: Convertir una cadena de caracteres de una fecha a una marca de tiempo (timestamp).
import datetime
import time
fecha_cadena = '1972/06/23'
resultado = time.mktime(datetime.datetime.strptime(fecha_cadena, '%Y/%m/%d').timetuple())
print(resultado)


# Ejercicio 689: Calcular la diferencia en días entre dos objetos fecha (date).
from datetime import date
def diferencia_dias(fecha_1, fecha_2):
    return (fecha_2 - fecha_1).days
ahora = date.today()
nacimiento_turin = date(1912, 6, 23)
resultado = diferencia_dias(nacimiento_turin, ahora)
print(resultado)
resultado = diferencia_dias(ahora, nacimiento_turin)
print(resultado)


# Ejercicio 690: Usar time.ctime() para generar la fecha y hora en un formato legible.
import time
fecha_hora = time.ctime()
print('Fecha y hora actuales:', fecha_hora)


# Ejercicio 691: Convertir un objeto fecha (datetime) a una marca de tiempo (timestamp).
import datetime
import time
fecha = datetime.datetime(2013, 12, 27)
print(type(fecha))
print('Fecha y hora:', fecha)
marca_tiempo = time.mktime(fecha.timetuple())
print('Marca de tiempo:', marca_tiempo)


# Ejercicio 692: Calcular diferencia en segundos entre dos objetos fecha.
from datetime import datetime, time
def diferencia_segundos_fechas(fecha_1, fecha_2):
    diferencia = fecha_2 - fecha_1
    resultado = diferencia.days * 24 * 3600 + diferencia.seconds
    return resultado
fecha_1 = datetime(2019, 1, 1)
fecha_2 = datetime.now()
print('Fecha actual:', fecha_2)
print(diferencia_segundos_fechas(fecha_1, fecha_2))


# Ejercicio 693: Convertir diferencia en segundos de dos fechas en dias, horas, minutos.
from datetime import datetime
def diferencia_segundos_fechas(fecha_1, fecha_2):
    diferencia = fecha_2 - fecha_1
    resultado = diferencia.days * 24 * 3600 + diferencia.seconds
    return resultado
def dias_horas_minutos_segundos(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    dias, horas = divmod(horas, 24)
    return dias, horas, minutos, segundos
fecha_1 = datetime(2019, 1, 1)
fecha_2 = datetime.now()
print('Fecha actual:', fecha_2)
segundos = diferencia_segundos_fechas(fecha_1, fecha_2)
print(segundos)
print()
resultado = dias_horas_minutos_segundos(segundos)
print(resultado)


# Ejercicio 694: Crear función para obtener la última fecha de modificación de un archivo.
from datetime import datetime
import time
import os
def ultima_fecha_modificacion(ruta_archivo):
    estado = os.stat(ruta_archivo)
    fecha = time.localtime(estado.st_mtime)
    fecha = datetime(fecha[0], fecha[1], fecha[2], fecha[3], fecha[4], fecha[5])
    return fecha
nombre_archivo = 'Parte001/lenguajes.txt'
resultado = ultima_fecha_modificacion(nombre_archivo)
print(resultado)


# Ejercicio 695: Calcular la edad en años a partir de la fecha de nacimiento.
from datetime import date
def calcular_edad_agnios(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado
fecha_nacimiento_turing = date(1912, 6, 23)
edad = calcular_edad_agnios(fecha_nacimiento_turing)
print(f'La edad de Turin es de {edad} años.')


# Ejercicio 696: Generar representación en cadena de caracteres de una fecha (datetime).
from datetime import datetime
ahora = datetime.now()
print(type(ahora))
ahora_cadena = ahora.strftime('%Y-%m-%d %H:%M:%S')
print(type(ahora_cadena))
print(ahora_cadena)


# Ejercicio 697: Generar calendario para un mes específico empezando desde el lunes.
import calendar
calendario = calendar.TextCalendar(calendar.MONDAY)
print('Primer mes del año 2020:')
calendario.prmonth(2020, 1)


# Ejercicio 698: Generar el calendario completo (12 meses) para un año particular.
import calendar
calendario = calendar.TextCalendar(calendar.SUNDAY)
print(calendario.formatyear(2020, 2, 1, 1, 3))


# Ejercicio 699: Mostrar calendario para un lugar (locale) específico.
import calendar
calendario = calendar.LocaleTextCalendar(locale='en_CA.utf8')
calendario.prmonth(2020, 2)


# Ejercicio 700: Generar el calendario de un año y mes específicos en formato HTML.
import calendar
calendario_html = calendar.HTMLCalendar(calendar.MONDAY)
print(calendario_html.formatmonth(2020, 2))


# Ejercicio 701: Convertir una cadena de caracteres de fecha en un objeto datetime.
from datetime import datetime
cadena_fecha = 'Jun 23 1912 3:31AM'
fecha = datetime.strptime(cadena_fecha, '%b %d %Y %I:%M%p')
print('Tipo de dato de la variable fecha:', type(fecha))
print(fecha)


# Ejercicio 702: Crear una función para generar una lista de fechas en un rango específico.
from datetime import date, timedelta
def generar_rango_fechas(fecha_1, fecha_2):
    fechas = []
    dias = (fecha_2 - fecha_1).days + 1
    for i in range(dias):
        fechas.append(fecha_1 + timedelta(i))
    return fechas
inicio = date(2020, 2, 1)
fin = date(2020, 2, 15)
resultado = generar_rango_fechas(inicio, fin)
for f in resultado:
    print(f)


# Ejercicio 703: Generar una marca de tiempo (timestamp) en el formato RFC 3339.
from datetime import datetime, timezone
rfc_3339 = datetime.now(timezone.utc).astimezone()
print('Marca de tiempo RFC 3339:', rfc_3339)


# Ejercicio 704: Obtener la hora mínima y máxima con las propiedades min y max de time.
from datetime import time
hora_minima = time.min
hora_maxima = time.max
print('Hora mínima:', hora_minima)
print('Hora máxima:', hora_maxima)


# Ejercicio 705: Crear una clase para invertir una frase palabra por palabra.
class OperacionesCadenas:
    def inversion_frases(self, frase):
        resultado = ' '.join(reversed(frase.split()))
        return resultado
frase = 'Python es un lenguaje de programación'
operaciones = OperacionesCadenas()
print(frase)
print(operaciones.inversion_frases(frase))


# Ejercicio 706: Obtener el nombre de la clase de una instancia u objeto.
from datetime import datetime
class ClasePersonalizada:
    pass
cp = ClasePersonalizada()
print(type(cp).__name__)
ahora = datetime.now()
print(type(ahora))
print(type(ahora).__name__)


# Ejercicio 707: Crear una clase personalizada para cálculos básicos sobre un círculo.
from math import pi
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        resultado = pi * self.radio ** 2
        return resultado
    def perimetro(self):
        resultado = 2 * pi * self.radio
        return resultado
c = Circulo(5)
print('Área:', c.area())
print('Perímetro:', c.perimetro())


# Ejercicio 708: Crear una clase personalizada para cálculos básicos sobre un rectángulo.
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        resultado = self.ancho * self.alto
        return resultado
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)
        return resultado
r = Rectangulo(10, 7)
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())


# Ejercicio 709: Crear una clase personalizada para cálculos básicos sobre un triángulo.
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        resultado = self.base * self.altura / 2
        return resultado
    def perimetro(self, a, b, c):
        resultado = a + b + c
        return resultado
t = Triangulo(3, 5)
print('Área del triángulo: %.2f' % t.area())
print('Perimetro del triángulo: %.2f' % t.perimetro(2, 3, 7))


# Ejercicio 710: Crear una jerarquía de herencia para figuras geométricas: círculo y rectángulo.
from abc import ABC, abstractmethod
from math import pi
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        resultado = pi * self.radio ** 2
        return resultado
    def perimetro(self):
        resultado = 2 * pi * self.radio
        return resultado
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        resultado = self.ancho * self.alto
        return resultado
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)
        return resultado
c = Circulo(5)
print('Cálculos del círculo:')
print('Área:', c.area())
print('Perímetro:', c.perimetro())
print()
r = Rectangulo(10, 7)
print('Cálculos del rectángulo:')
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())


# Ejercicio 711: Encontrar los 3 elementos que suman cero (0) desde una lista de números.
from itertools import combinations
def elementos_suma_cero(numeros):
    sublistas_tres = list(combinations(numeros, 3))
    sublistas = []
    for s in sublistas_tres:
        if sum(s) == 0:
            sublistas.append(s)
    return sublistas
numeros = [-3, 2, 1, 7, -4, -1, -2, 7, 5, -3, 0, 11, -11]
resultado = elementos_suma_cero(numeros)
print(resultado)


# Ejercicio 712: Encontrar dos índices de números que suman un valor particular.
# Análisis:
# [1, 2, 3, 4, 5], 6
def encontrar_indices_suma(numeros, suma):
    numeros_indices = {}
    for i, n in enumerate(numeros):
        if suma - n in numeros_indices:
            return numeros_indices[suma - n], i
        numeros_indices[n] = i
numeros = [1, 2, 3, 4, 5]
suma = 6
resultado = encontrar_indices_suma(numeros, suma)
print(resultado)
# Prueba de escritorio:
# numeros_indices = {1: 0, 2: 1, 3: 2, }


# Ejercicio 713: Encontrar todos los subconjuntos únicos posibles de una lista.
def subconjuntos(numeros):
    return subconjuntos_recursivo([], sorted(numeros))
def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]
numeros = [1, 2, 3, 4, 5]
resultado = subconjuntos(numeros)
print(len(resultado)) # 2^n => 2^5 = 32
print(resultado)


# Ejercicio 714: Crear una función para comprobar si una cadena de paréntesis es válida.
# Análisis:
# '()[]{}' => True
# '()[]{}(' => False
# '(){][}' => False
def cadena_parentesis_valida(cadena):
    pila = []
    parentesis = {'{': '}', '(': ')', '[': ']'}
    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False
    return len(pila) == 0
print(cadena_parentesis_valida('()[]{}'))
print(cadena_parentesis_valida('()[]{}('))
print(cadena_parentesis_valida('((){][}'))


# Ejercicio 715: Crear función para convertir un número entero a un númeral romano.
def conversion_entero_romano(entero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numeral = ''
    i = 0
    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]
        i += 1
    return numeral
print(conversion_entero_romano(123)) # 'CXXIII'
# Prueba de escritorio:
# numeral = 'CXXIII'
# i = 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
# entero = 123, 23, 13, 3, 2, 1, 0


# Ejercicio 716: Crear una función para convertir un número romano a un número entero.
def romano_a_entero(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    entero = 0
    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            entero += romanos[romano[i]]
    return entero
print(romano_a_entero('CXXIII')) # 123
# Prueba de escritorio:
# romano = 'CXXIII'
# entero = 0, 100, 110, 120, 121, 122, 123


# Ejercicio 717: Crear una función para convertir grados a radianes.
from math import pi
def grados_radianes(grados):
    """
    Convierte una cantidad de grados en radianes.
    """
    radianes = grados * (pi / 180)
    return radianes
print(grados_radianes(180)) # 3.1415...
print(grados_radianes(90)) # 1.5708


# Ejercicio 718: Crear una función para convertir radianes a grados.
import math
def radianes_a_grados(radianes):
    grados = radianes * (180 / math.pi)
    return grados
print(radianes_a_grados(math.pi)) # 180
print(radianes_a_grados(math.pi/2)) # 90
print(radianes_a_grados(math.pi/3)) # 60


# Ejercicio 719: Crear una función personalizada para calcular el área de un trapezoide.
def area_trapezoide(B, b, h):
    """
    Calcula el área de un trapezoide.
    """
    area = (B + b) / 2 * h
    return area
print(area_trapezoide(5, 3, 7)) # 28.0


# Ejercicio 720: Crear una función para calcular el área de un paralelogramo.
def area_paralelogramo(b, h):
    """
    Calcula el área de un paralelogramo.
    """
    area = b * h
    return area
base = float(input('Digite la base del paralelogramo: '))
altura = float(input('Digite la altura del paralelogramo: '))
resultado = area_paralelogramo(base, altura)
print(f'El área del paralelogramo es igual a {resultado}.')


# Ejercicio 721: Crear funciones para calcular el área superficial y el volumen de un cilindro.
from math import pi
def volumen_cilindro(r, h):
    volumen = pi * r**2 * h
    return volumen
def area_superficial_cilindro(r, h):
    area = 2 * pi * r**2 + 2 * pi * r * h
    return area
radio = 5
altura = 7
print(f'Volumen del cilindro: {volumen_cilindro(radio, altura)}')
print(f'Área superficial del cilindro: {area_superficial_cilindro(radio, altura)}')


# Ejercicio 722: Crear funciones para calcular el área superficial y el volumen de una esfera.
from math import pi
def area_supeficial(r):
    area = 4 * pi * r ** 2
    return area
def volumen(r):
    resultado = 4/3 * pi * r**3
    return resultado
radio = 5
print(area_supeficial(radio))
print(volumen(5))


# Ejercicio 723: Crear una función para calcular la longitud de arco de un ángulo.
from math import pi
def longitud_arco(radio, angulo):
    resultado = 2 * pi * radio * (angulo/360)
    return resultado
print(longitud_arco(10, 45))


# Ejercicio 724: Crear una función para calcular el área de un sector de un círculo.
from math import pi
def area_sector_circulo(radio, radianes):
    area = 1/2 * radio ** 2 * radianes
    return area
print(area_sector_circulo(5, pi/2))


# Ejercicio 725: Crear función para calcular el número de soluciones de una fórmula cuadrática.
# a*x^2 + b*x + c => a, b, c
def discriminante(a, b, c):
    resultado = b**2 - 4 * a * c
    return resultado
def numero_soluciones(a, b, c):
    det = discriminante(a, b, c)
    if det > 0:
        return 2
    elif det == 0:
        return 1
    else:
        return 0
print(numero_soluciones(1, 0, 1))
print(numero_soluciones(1, 0, 0))
print(numero_soluciones(1, 0, -1))


# Ejercicio 726: Crear función para generar una lista de todos los divisores positivos de un número.
def divisores(numero):
    """
    Genera una lista de los divisores de un número.
    """
    resultado = [i for i in range(1, numero + 1) if numero % i == 0]
    return resultado
print(divisores(5))
print(divisores(10))
print(divisores(13))
print(divisores(17))


# Ejercicio 727: Diferencia suma de los cuadrados y cuadrado de la suma de los primeros n números.
def diferencia(n=2):
    suma_cuadrados = 0
    suma = 0
    for n in range(1, n + 1):
        suma_cuadrados += n**2
        suma += n
    suma = suma ** 2
    return suma - suma_cuadrados
print(diferencia(5))
print(diferencia(10))
print(diferencia(20))


# Ejercicio 728: Calcular la suma de los dígitos de la potencia de un número.
# 2^6 = 64 => 10
def suma_digitos_potencia(base, exponente):
    digitos_potencia = [int(d) for d in str(pow(base, exponente))]
    suma = sum(digitos_potencia)
    return suma
print(suma_digitos_potencia(2, 6))
print(suma_digitos_potencia(2, 100))
print(suma_digitos_potencia(3, 4))


# Ejercicio 729: Crear una función para determinar si un número dado es abundante.
# 12 => 1 + 2 + 3 + 4 + 6 => 16
# 13 => 1 => 1
def es_abundante(numero):
    factores = [f for f in range(1, numero) if numero % f == 0]
    suma = sum(factores)
    return suma > numero
print(es_abundante(12))
print(es_abundante(13))


# Ejercicio 730: Crear una función para determinar si un número es perfecto con lista de comprensión.
# 6 -> 1, 2, 3 => 1 + 2 + 3 = 6
# 28 -> 1 + 2 + 4 + 7 + 14 = 28
def es_numero_perfecto(numero):
    suma = sum([i for i in range(1, numero) if numero % i == 0])
    return suma == numero
print(es_numero_perfecto(6)) # 1 + 2 + 3 = 6
print(es_numero_perfecto(12)) # 1 + 2 + 3 + 4 + 6 = 16
print(es_numero_perfecto(28)) # 1 + 2 + 4 + 7 + 14 = 28
print(es_numero_perfecto(496))
print(es_numero_perfecto(8128))


# Ejercicio 731: Crear una función para obtener la suma de los divisores de un número.
def suma_divisores(n):
    divisores = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)
resultado = suma_divisores(12) # 1 + 2 + 3 + 4 + 6 + 12 = 28
print(resultado)
resultado = suma_divisores(13) # 1 + 13 = 14
print(resultado)
resultado = suma_divisores(20) # 1 + 2 + 4 + 5 + 10 + 20 = 42
print(resultado)
resultado = suma_divisores(29) # 1 + 29 = 30
print(resultado)


# Ejercicio 732: Crear una función para obtener la suma de los divisores de un número con lista de comprensión.
def suma_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    return sum(divisores)
resultado = suma_divisores(12) # 1 + 2 + 3 + 4 + 6 + 12 = 28
print(resultado)
resultado = suma_divisores(13) # 1 + 13 = 14
print(resultado)
resultado = suma_divisores(20) # 1 + 2 + 4 + 5 + 10 + 20 = 42
print(resultado)
resultado = suma_divisores(29) # 1 + 29 = 30
print(resultado)


# Ejercicio 733: Crear una función para dejar las vocales de una palabra al principio.
def vocales_primero(palabra):
    vocales = [c for c in palabra if c in 'aeiouAEIOU']
    consonantes = [c for c in palabra if c not in 'aeiouAEIOU']
    return ''.join(vocales) + ''.join(consonantes)
palabra = 'vocales'
print(vocales_primero(palabra)) # oaevcls
palabra = 'Python'
print(vocales_primero(palabra)) # oPythn


# Ejercicio 734: Crear una función para generar una lista de los números de la suerte.
def numeros_suerte(n):
    numeros = list(range(-1, n**2 + 9, 2))
    i = 2
    while numeros[i:]:
        numeros = sorted(set(numeros) - set(numeros[numeros[i]::numeros[i]]))
        i += 1
    return numeros[1:n+1]
if __name__ == "__main__":
    resultado = numeros_suerte(5)
    print(resultado)


# Ejercicio 735: Calcular la raíz cuadrada de un número por el método babilónico.
from math import sqrt
def metodo_babilonico_raiz_cuadrada(n):
    if n < 0:
        raise ValueError('El valor de n no puede ser negativo')
    elif n == 0:
        return 0
    else:
        x = 2.0
        cociente = n / x
        promedio = (x + cociente) / 2.0
        while abs(cociente - promedio) > 0.00000000001:
            x = promedio
            cociente = n / x
            promedio = (x + cociente) / 2.0
        return promedio
numero = 2
print('Raíz cuadrada con la función sqrt:', sqrt(numero))
print('Raíz cuadrada con el método babilónico:', metodo_babilonico_raiz_cuadrada(numero))


# Ejercicio 736: Multiplicar dos números sin usar el operador de multiplicación (*).
# Recursividad.
# a*b = a_1 + a_2 + a_3 + ... + a_b
def multiplicar(a, b):
    if b < 0:
        return -multiplicar(a, -b)
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicar(a, b - 1)
if __name__ == "__main__":
    resultado = multiplicar(3, -2)
    print(resultado)
    resultado = multiplicar(3, 2)
    print(resultado)


# Ejercicio 737: Crear una función para validar si una matriz es un cuadrado mágico.
from itertools import chain
def elementos_diferentes(matriz):
    numeros = list(chain(*matriz))
    return len(set(numeros)) == len(numeros)
def es_cuadrado_magico(matriz):
    if len(matriz) == len(matriz[0]):
        if elementos_diferentes(matriz):
            suma = sum(matriz[0])
            for i in range(1, len(matriz)):
                if suma != sum(matriz[i]):
                    return False
            for j in range(len(matriz[0])):
                suma_columna = sum([matriz[i][j] for i in range(len(matriz))])
                if suma != suma_columna:
                    return False
            suma_diagonal_principal = sum([matriz[i][i] for i in range(len(matriz))])
            if suma != suma_diagonal_principal:
                return False
            columnas = len(matriz[0]) - 1
            suma_diagonal_secundaria = 0
            for i in range(len(matriz)):
                suma_diagonal_secundaria += matriz[i][columnas]
                columnas -= 1
            return suma == suma_diagonal_secundaria
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    matriz = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    resultado = es_cuadrado_magico(matriz)
    print(resultado)
    matriz = [[8, 1, 6], [3, 5, 7], [4, 9, 2], [1, 2, 3]]
    resultado = es_cuadrado_magico(matriz)
    print(resultado)
    matriz = [[8, 1, 6], [3, 5, 7], [4, 9, 0]]
    resultado = es_cuadrado_magico(matriz)
    print(resultado)


# Ejercicio 738: Crear una función para generar números primos a partir de la criba de Eratóstenes.
def criba_eratostenes(n):
    primos = []
    no_primos = set()
    for i in range(2, n + 1):
        if i in no_primos:
            continue
        for j in range(i*2, n + 1, i):
            no_primos.add(j)
        primos.append(i)
    return primos
if __name__ == "__main__":
    resultado = criba_eratostenes(120)
    print(len(resultado))
    print(resultado)


# Ejercicio 739: Crear una función para encontrar el siguiente número palíndromo (capicúa).
# 191, 11, 1991, 1001, ...
# n = 191, 202
# n = 11, 22
import sys
def siguiente_palindromo(n):
    """
    Encuentra el siguiente número palíndromo (o capicúa).
    """
    for i in range(n + 1, sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
if __name__ == "__main__":
    print(siguiente_palindromo(191))
    print(siguiente_palindromo(11))
    print(siguiente_palindromo(1991))
    print(siguiente_palindromo(1001))


# Ejercicio 740: Crear una función para encontrar el anterior número palíndromo (capicúa).
# 191, 11, 1991, 1001, ...
# n = 191, 181
# n = 11, 9
import sys
def anterior_palindromo(n):
    """
    Encuentra el siguiente número palíndromo (o capicúa).
    """
    for i in range(n - 1, 0, -1):
        if str(i) == str(i)[::-1]:
            return i
if __name__ == "__main__":
    print(anterior_palindromo(191)) # 181
    print(anterior_palindromo(11)) # 9
    print(anterior_palindromo(1991)) # 1881
    print(anterior_palindromo(1001)) # 999


# Ejercicio 741: Usar itertools.permutations() para crear las permutaciones de una lista de números.
from itertools import permutations
colores = ['Rojo', 'Verde', 'Azul']
permutaciones = list(permutations(colores))
for p in permutaciones:
    print(p)
print('Cantidad de permutaciones: %i' % len(permutaciones))


# Ejercicio 742: Crear una función para obtener el n-ésimo número de Catalán.
def numero_catalan(n):
    if n <= 1:
        return 1
    resultado = 0
    for i in range(n):
        resultado += numero_catalan(i) * numero_catalan(n-i-1)
    return resultado
if __name__ == "__main__":
    for i in range(11):
        print(numero_catalan(i))


# Ejercicio 743: Imprimir un número usando la coma (,) como separador de millares.
numero = 1000000
print(numero)
print('{:,}'.format(numero))
print()
numero = 1000
print(numero)
print('{:,}'.format(numero))
print()
numero = 100
print(numero)
print('{:,}'.format(numero))


# Ejercicio 744: Calcular la distancia entre dos puntos definidos por la latitud y la longitud.
from math import acos, cos, sin, radians
def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))
    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))
    return distancia * 6371.01
if __name__ == "__main__":
    punto_1 = (4.6097100, -74.0817500)
    punto_2 = (55.7522202, 37.6155586)
    resultado = distancia_puntos(punto_1, punto_2)
    print('La distancia en kilómetros entre Bogotá y Moscú es de %f' % resultado)


# Ejercicio 745: Crear una función para calcular el área de un polígono regular.
from math import pi, tan
def area_poligono_regular(n, l):
    area = n * l**2 / (4 * tan(pi/n))
    return area
if __name__ == "__main__":
    n = 6
    l = 10
    resultado = area_poligono_regular(n, l)
    print(resultado)


# Ejercicio 746: Crear una función para calcular el índice de temperatura de sensación (o percibida).
def indice_temperatura_sensacion(t, v):
    """
    Computa el índice de temperatura de sensación o temperatura percibida.
    """
    indice = 13.12 + 0.6215*t - 11.37 * v**0.16 + 0.3965 * t * v**0.16
    return indice
if __name__ == "__main__":
    temperatura = 35
    velocidad = 120
    resultado = indice_temperatura_sensacion(temperatura, velocidad)
    print(f'La temperatura de sensación es igual {resultado}°C.')


# Ejercicio 747: Crear una función para encontrar las soluciones a una ecuación cuadrática.
from math import sqrt
# a*x**2 + b*x + c
def discriminante(a, b, c):
    return b**2 - 4 * a * c
def soluciones_ecuacion_cuadratica(a, b, c):
    d = discriminante(a, b, c)
    if d > 0:
        x_1 = (-b + sqrt(d)) / (2*a)
        x_2 = (-b - sqrt(d)) / (2*a)
        return x_1, x_2
    elif d == 0:
        x = -b / (2*a)
        return x,
    else:
        return tuple([])
if __name__ == "__main__":
    resultado = soluciones_ecuacion_cuadratica(1, 0, 1)
    print(resultado)
    resultado = soluciones_ecuacion_cuadratica(1, 0, 0)
    print(resultado)
    resultado = soluciones_ecuacion_cuadratica(1, 0, -1)
    print(resultado)


# Ejercicio 748: Crear una función para convertir un número binario en un número decimal.
def es_binario_validio(binario):
    conjunto_bits = set(list(binario))
    return ('0' in conjunto_bits or '1' in conjunto_bits) and len(conjunto_bits) in [1, 2]
def convertir_binario_a_decimal(binario):
    if es_binario_validio(binario):
        bits = list(binario)
        valor = 0
        for i in range(len(bits)):
            bit = bits.pop()
            if bit == '1':
                valor += pow(2, i)
        return valor
    else:
        raise ValueError('La cadena no representa un número binario válido.')
if __name__ == "__main__":
    binario = '1001' # 9 (10)
    print(convertir_binario_a_decimal(binario))
    binario = '10001' # 9 (10)
    print(convertir_binario_a_decimal(binario))
    binario = '11111111' # 9 (10)
    print(convertir_binario_a_decimal(binario))


# Ejercicio 749: Obtener la parte real e imaginaria de un número complejo.
# complejo = complex(5, 3)
complejo = 5+3j
print(complejo)
print(complejo.real)
print(complejo.imag)


# Ejercicio 750: Realizar las operaciones aritméticas básicas sobre números complejos.
numero_1 = 2 + 3j
numero_2 = -2 -5j
suma = numero_1 + numero_2
print(suma)
resta = numero_1 - numero_2
print(resta)
producto = numero_1 * numero_2
print(producto)
division = numero_1 / numero_2
print(division)


# Ejercicio 751: Computar la longitud y el ángulo de un número complejo.
import cmath
complejo = complex(2, 3)
print('Longitud: {}'.format(abs(complejo)))
print('Ángulo: {}'.format(cmath.phase(complejo)))


# Ejercicio 752: Calcular las coordenadas polares y rectangulares de un número complejo.
import cmath
complejo = complex(2, 3) # 2+3j
coordenadas_polares = cmath.polar(complejo)
print(coordenadas_polares)
print()
coordenadas_rectangulares = cmath.rect(coordenadas_polares[0], coordenadas_polares[1])
print(coordenadas_rectangulares)


# Ejercicio 753: Encontrar el mínimo y el máximo de un conjunto de números decimales.
from decimal import Decimal
cadena = '2.54 2.73 2.71 3.14 2.00 0.04 1.19'
lista = cadena.split()
decimales = list(map(Decimal, lista))
print(decimales)
minimo = min(decimales)
maximo = max(decimales)
print(minimo)
print(maximo)


# Ejercicio 754: Sumar y ordenar un conjunto de números decimales.
from decimal import Decimal
cadena = '2.54 2.73 2.71 3.14 2.00 0.04 1.19'
lista = cadena.split()
print(lista)
decimales = list(map(Decimal, lista))
print(decimales)
suma = sum(decimales)
decimales = sorted(decimales)
print()
print('Suma: %f' % suma)
print(decimales)


# Ejercicio 755: Calcular la raíz cuadrada y el exponente de un objeto Decimal.
from decimal import Decimal
numero = Decimal(1.79)
raiz = numero.sqrt()
exp = numero.exp()
print(raiz)
print(exp)


# Ejercicio 756: Obtener todas las propiedades públicas (contexto global) de los decimales.
import decimal
contexto = decimal.getcontext()
print('Exponencial máximo:', contexto.Emax)
print('Exponencial mínimo:', contexto.Emin)
print('Letra exponente e:', contexto.capitals)
print('Precisión:', contexto.prec)
print('Modo redondeo:', contexto.rounding)
print()
print('Banderas habilitadas:')
for k, v in contexto.flags.items():
    print('{}: {}'.format(k, v))
print()
print('Excepciones:')
for k, v in contexto.traps.items():
    print('{}: {}'.format(k, v))


# Ejercicio 757: Cambiar la precisión de un objeto Decimal con la propiedad prec.
import decimal
division = decimal.Decimal(1/7)
print(division)
print(decimal.getcontext().prec)
for i in range(1, 11):
    decimal.getcontext().prec = i
    print('Precisión: {} - Valor: {}'.format(i, division * 1))


# Ejercicio 758: Redondear objeto Decimal al piso o al techo con la propiedad rounding.
import decimal
contexto = decimal.getcontext()
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)
contexto.prec = 4
print()
contexto.rounding = getattr(decimal, 'ROUND_FLOOR')
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)
print()
contexto.rounding = getattr(decimal, 'ROUND_CEILING')
division = decimal.Decimal(1) / decimal.Decimal(17)
print('Valor actual de 1/17:', division)


# Ejercicio 759: Crear objetos Fraction para obtener la representación fraccionario de un decimal.
import fractions
decimales = [0.7, 2.5, 0.5, 9.32, 7e-1]
for d in decimales:
    fraccion = fractions.Fraction(d)
    print('{} = {}'.format(d, fraccion))


# Ejercicio 760: Convertir un objeto Decimal en un objeto Fraction (fracción).
from decimal import Decimal
from fractions import Fraction
decimales = [Decimal(0.5), Decimal(0.25), Decimal(1/7), Decimal('5.0')]
for d in decimales:
    print('{} = {}'.format(d, Fraction(d)))


# Ejercicio 761: Realizar operaciones aritméticas básicas con fracciones.
from fractions import Fraction
un_medio = Fraction(1, 2)
un_tercio = Fraction(1, 3)
print('{} + {} = {}'.format(un_medio, un_tercio, un_medio + un_tercio))
print('{} - {} = {}'.format(un_medio, un_tercio, un_medio - un_tercio))
print('{} * {} = {}'.format(un_medio, un_tercio, un_medio * un_tercio))
print('{} / {} = {}'.format(un_medio, un_tercio, un_medio / un_tercio))


# Ejercicio 762: Obtener diferentes aproximaciones racionales de la constante pi.
from fractions import Fraction
from math import pi
print('Valor de pi:', pi)
fraccion_pi = Fraction(str(pi))
print('fraccion_pi:', fraccion_pi)
print()
denominadores = [1, 5, 50, 90, 100, 500, 1000, 10000, 1000000]
for d in denominadores:
    fraccion = fraccion_pi.limit_denominator(d)
    print(fraccion)


# Ejercicio 763: Generar varios números reales aleatorios dentro de un rango específico.
import random
for i in range(10):
    print(random.uniform(0, 100))


# Ejercicio 764: Generar varios números enteros aleatorios dentro de un rango específico.
import random
for _ in range(10):
    print(random.randrange(0, 100))


# Ejercicio 765: Generar varios números enteros pares aleatorios dentro de un rango específico.
import random
for _ in range(10):
    print(random.randrange(0, 100, 2), end=' ')


# Ejercicio 766: Tomar de modo aleatorio un elemento de una colección con el método choice.
import random
from string import ascii_uppercase
numeros = [2, 3, 5, 7, 11, 13, 17, 19]
print(random.choice(numeros))
print(ascii_uppercase)
print(random.choice(ascii_uppercase))


# Ejercicio 767: Aleatorizar el contenido de una colección o secuencia con la función shuffle().
import random
from string import ascii_uppercase
numeros = [1, 2, 3, 4, 5]
print(numeros)
random.shuffle(numeros)
print(numeros)
print()
mayusculas = list(ascii_uppercase)
print(mayusculas)
random.shuffle(mayusculas)
print(mayusculas)


# Ejercicio 768: Usar el módulo random para generar 10000 lanzamientos de una moneda.
import random
resultados = {'sello': 0, 'cara': 0}
lados = list(resultados.keys())
for _ in range(10000):
    resultados[random.choice(lados)] += 1
print('Sellos:', resultados['sello'])
print('Caras:', resultados['cara'])


# Ejercicio 769: Usar la función fabs() para calcular el valor absoluto de un número de punto flotante.
# fabs() (módulo math): float absolute
from math import fabs
print(fabs(-3.3))
print(fabs(13.5))
print(fabs(0.0))
print(fabs(-0.0))


# Ejercicio 770: Imprimir en pantalla la mantisa y el exponente de una lista de valores.
from math import ldexp
# b * (2^e)
print('{:^7}  {:^9}  {:^14}'.format('Mantisa', 'Exponente', 'Punto flotante'))
print('{:-^8} {:-^9}  {:-^14}'.format('', '', ''))
valores = [(0.5, 7), (0.3, -3), (0.9, 5), (0.2, -8)]
for m, e in valores:
    resultado = ldexp(m, e)
    print('{:7.2f} {:7d}     {:7.2f}'.format(m, e, resultado))


# Ejercicio 771: Obtener la parte entera y fraccionaria de un división de punto flotante.
# /: división de punto flotante
# //: división entera
from math import modf
print('{}(F)  (I)'.format(' ' * 10))
for i in range(6):
    print('{}/3 = {} {}'.format(i, i/3, modf(i/3.0)))


# Ejercicio 772: Obtener el listado de variables creadas en un script.
def mostrar_listado_variables(variables):
    for v in variables:
        if not v.startswith('__'):
            print(v)
mostrar_listado_variables(dir())
print()
a = 2
b = 3
mostrar_listado_variables(dir())


# Ejercicio 773: Comprobar si una variable ha sido declarada.
print('x' in dir())
x = 100
print('x' in dir())


# Ejercicio 774: Usar el operador del para borrar una variable declarada.
print('x' in dir())
print()
x = 100
print('x' in dir())
print()
del x
print('x' in dir())
try:
    del x
except NameError as e:
    print(e)


# Ejercicio 775: Usar el operador % para pasar argumentos a una cadena de formato.
nombre = 'Edward'
apellido = 'Ortiz'
edad = 29
print('Nombre: ' + nombre + " - Apellido: " + apellido + " - Edad: " + str(edad))
print()
print('Nombre:', nombre, '- Apellido:', apellido, '- Edad:', edad)
print()
print('Nombre: %s - Apellido: %s - Edad: %i' % (nombre, apellido, edad))


# Ejercicio 776: Uso de la función isalnum() para validar si hay números en una cadena de caracteres.
cadena = 'Pythonv381'
print(cadena.isalnum())
print()
cadena = 'Niño123ß'
print()
print(cadena.isalnum())
cadena = 'Vacío123'
print(cadena.isalnum())


# Ejercicio 777: Uso de la función str.istitle() para validar si una cadena está capitalizada tipo título de libro.
# Crimen Y Castigo
titulo_libro = 'Crimen Y Castigo'
print(titulo_libro.istitle())
print()
titulo_libro = 'Fyodor Dostoevsky - Crimen Y Castigo'
print(titulo_libro.istitle())
print()
titulo_libro = 'Memorias del Subsuelo'
print(titulo_libro.istitle())
print()
titulo_libro = 'Memorias Del Subsuelo'
print(titulo_libro.istitle())


# Ejercicio 778: Uso de la función join() para concatenar un conjunto de valores tipo string.
# Conjunto -> Lista, tupla
nombres = ['Juan', 'Oliva', 'Daniela', 'Edward', 'Germán']
print('Contenido de la variable `nombres`:', nombres)
print()
formato = ', '.join(nombres)
print('Contenido de la variable `formato`:', formato)
print()
numeros = [2, 3, 5, 7, 11, 13, 17, 19]
print('Contenido de la variable `numeros`:', numeros)
print()
# formato = ', '.join(numeros) # TypeError
formato = ', '.join([str(n) for n in numeros])
print('Contenido de la variable `formato`:', formato)


# Ejercicio 779: Uso de la función swapcase() para alternar minúsculas y mayúsculas de un string.
escritor = 'Fyodor Dostoevsky'
print('Contenido de la variable `escritor`:', escritor)
escritor = escritor.swapcase()
print('Contenido de la variable `escritor`:', escritor)


# Ejercicio 780: Uso de la función format() para formatear una cadena de caracteres.
uno = 1
dos = 2
print('{}, {}'.format(uno, dos)) # 1, 2
print('{1}, {0}'.format(uno, dos)) # 2, 1
print('{1}, {0}'.format(dos, uno)) # 1, 2
print('{1}, {0}, {2}'.format(dos, uno, dos)) # 1, 2, 2
print('{1}, {0}, {0}'.format(dos, uno)) # 1, 2, 2


# Ejercicio 781: Utilizar el especificador de formato % sobre cadenas de caracteres.
nombre = 'Daniela Ortiz'
edad = 29
ahorros = 10000.79
casada = False
print('Nombre: ' + nombre + ' - Edad: ' + str(edad) + ' - Ahorros: $' + str(ahorros) + ' - Casada: ' + str(casada))
print()
print('Nombre: %s - Edad: %i - Ahorros: $%.2f - Casada: %s' % (nombre, edad, ahorros, casada))


# Ejercicio 782: Diferencia entre las funciones incorporadas str() y repr().
# str(): para obtener la representación "informal" en cadena de caracteres de una variable o una literal.
# repr(): para obtener la representación "formal" en cadena de caracteres de una variable o una literal.
numero = 5
print(str(numero))
print(repr(numero))
print()
nombre = 'Edward'
print(str(nombre))
print(repr(nombre))
print()
nombre = "Edward"
print(str(nombre)) # Edward
print(repr(nombre)) # 'Edward'
print()
colores = {'Red': 13, 'Verde': 101, 'Azul': 203}
print(str(colores))
print(repr(colores))


# Ejercicio 783: Usar un especificador de formato para las representación formal (repr) e informal (str) de un objeto.
# str(): obtenemos la representación informal de un objeto.
# repr(): obtenemos la representación formal de un objeto.
class Persona:
    def __str__(self):
        return 'Persona'
    def __repr__(self):
        return 'Persona <Persona>'
p = Persona()
# Mecanismo tradicional con %s o %r:
print('%s - %r' % (p, p))
print()
# Nuevo mecanismo - Función format()
print('{0!s} - {0!r}'.format(p))


# Ejercicio 784: Alinear cadenas de caracteres con especificadores de formato y la función format().
lenguaje = 'Python'
print(lenguaje)
print()
# Alinear a la derecha (>):
print('{:>24}'.format(lenguaje))
print()
version = '3.8.1'
# Alinear a la izquierda:
print(lenguaje, version)
print('{:<12}{}'.format(lenguaje, version))
print()
print('{:_<12}{}'.format(lenguaje, version))
print()
# Centrar el texto:
print('{:^12}'.format(lenguaje))
print('{:#^12}'.format(lenguaje))


# Ejercicio 785: Truncar una cadena de caracteres con especificadores de formato.
frase = '¡Python es tremendo!'
print(frase)
print('%s' % frase)
print('{0}'.format(frase))
print()
subcadena = frase[:7]
print(subcadena)
print()
# Mecanismo tradicional:
print('%.7s' % frase)
# Nuevo mecanismo:
print('{:.7}'.format(frase))


# Ejercicio 786: Truncar y agregar padding a una cadena de caracteres con especificadores de formato.
frase = 'Python es tremendo'
print(frase)
print('{:.6}'.format(frase))
print('{:<10.6}'.format(frase))
print('{:<10.6}es un lenguaje de programación'.format(frase))
print('{:>10.6}'.format(frase))
print('{:_>10.6}'.format(frase))
print('{:_^10.6}'.format(frase))


# Ejercicio 788: Agregar padding con especificadores de formato a valores numéricos.
entero = 1234
real = 3.141592653589793
print(entero)
print(real)
print()
# Mecanismo tradicional:
print('%d' % entero)
print('%f' % real)
print('%.10f' % real)
print()
# Mecanismo nuevo:
print('{:d}'.format(entero))
print('{:f}'.format(real))
print('{:.10f}'.format(real))
print()
# Padding a la izquierda:
print('{:<10d}entero'.format(entero))
print('{:<10f}real'.format(real))
print('{:<10.10f}real'.format(real))
# Padding a la derecha:
print()
print('{:>10d}entero'.format(entero))
print('{:>10f}real'.format(real))
print('{:>10.10f}real'.format(real))


# Ejercicio 789: Agregar con una cadena de formato el signo de un número.
entero = 1000
real = 13.19
print(entero)
print(real)
# Mecanismo tradicional:
print('%+d' % (entero,))
print('%+f' % (real,))
# Mecanismo nuevo:
print('{:+d}'.format(entero))
print('{:+f}'.format(real))
print()
entero = -1000
real = -13.19
# Mecanismo tradicional:
print('%+d' % (entero,))
print('%+f' % (real,))
# Mecanismo nuevo:
print('{:+d}'.format(entero))
print('{:+f}'.format(real))
print()
print(entero)
print(real)


# Ejercicio 790: Agregar padding al signo de un valor numérico en una cadena de formato.
# -13.19
# -    13.19
# 13.19
# +    13.19
numero = -13.19
print(numero)
print('{:=10.2f}'.format(numero))
print()
numero = 13.19
print(numero)
print('{:=+10.2f}'.format(numero))


# Ejercicio 791: Cadena de formato con placeholders (receptáculos) para atributos de datos.
persona = {'nombre': 'Daniela', 'apellido': 'Ortiz', 'edad': 29}
print(persona)
print()
# Mecanismo tradicional:
print('Nombre: %(nombre)s - Apellido: %(apellido)s - Edad: %(edad)d' % persona)
print('Nombre: %(nombre)s - Edad: %(edad)d - Apellido: %(apellido)s' % persona)
print()
# Mecanismo nuevo (format()):
print('{nombre} - {apellido} - {edad}'.format(**persona))
print('{nombre} - {edad} - {apellido}'.format(**persona))
print('Nombre: {nombre} - Edad: {edad} - Apellido: {apellido}'.format(**persona))
print()
print('Nombre: {nombre} - Apellido: {apellido}'.format(nombre=persona['nombre'], apellido=persona['apellido']))
print('Nombre: {name} - Apellido: {lastname}'.format(name=persona['nombre'], lastname=persona['apellido']))
print()
print('Nombre: {nombre} - Apellido: {apellido}'.format(apellido='Ortiz', nombre='Daniela'))


# Ejercicio 792: Usar accesores de una estructura de datos en una cadena de formato.
persona = {'nombre': 'Daniela', 'apellido': 'Ortiz', 'edad': 29}
print(persona)
print()
print('{p[nombre]} - {p[apellido]} - {p[edad]}'.format(p=persona))
print('Nombre: {p[nombre]} - Apellido: {p[apellido]} - Edad: {p[edad]}'.format(p=persona))


# Ejercicio 793: Usar accesores de una lista en una cadena de formato.
# numeros = [2, 3, 5, 7]
# numeros[0]
# numeros[1]
# numeros[-1]
numeros = [2, 3, 5, 7, 11, 13]
print(numeros)
print()
print(numeros[-1])
print('{l[1]}, {l[3]}, {l[5]}'.format(l=numeros))


# Ejercicio 794: Accesores para los atributos de una clase.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
punto = Punto(2, 3)
print(punto)
print()
print('x: {p.x} - y: {p.y}'.format(p=punto))


# Ejercicio 795: Usar una cadena de formato para un objeto fecha.
from datetime import datetime
fecha = datetime(2012, 10, 8, 7, 13, 43)
print(fecha)
print()
print('{:%Y/%m/%d %H:%M}'.format(fecha))


# Ejercicio 796: Calcular el valor de la constante e (Euler) con una serie infinita.
from math import e, fabs, factorial
def serie_infinita_e(epsilon):
    e = 0
    i = 3
    suma_1 = 2
    suma_2 = suma_1 + float(1/factorial(2))
    while fabs(suma_1 - suma_2) >= epsilon:
        suma_1 = suma_2
        suma_2 += float(1/factorial(i))
        i += 1
    return suma_2
print(serie_infinita_e(0.00000001))
print(e)


# Ejercicio 797: Parametrizar los especificadores de formato en una cadena.
lenguaje = 'Python'
print(lenguaje)
print('{:^10}'.format(lenguaje))
print()
padding = 10
print('{:^{p}}'.format(lenguaje, p=padding))
print()
alineacion = '>'
print('{:{a}{p}}'.format(lenguaje, p=padding, a=alineacion))
print()
alineacion = '<'
print('{:{a}{p}}'.format(lenguaje, p=padding, a=alineacion))


# Ejercicio 798: Parametrizar los especificadores de formato para valores numéricos.
nombre = 'Daniela'
ahorros = 1373.1719
print('Nombre:', nombre)
print('Ahorros:', ahorros)
print()
# Mecanismo tradicional (%) sin parametrizar:
print('Nombre: %s - Ahorros: %.2f' % (nombre[:4], ahorros))
# Mecanismo tradicional (%) sin parametrizar:
print('Nombre: %.4s - Ahorros: %.2f' % (nombre, ahorros))
cantidad_caracteres = 4
precision = 2
print('Nombre: %.*s - Ahorros: %.2f' % (cantidad_caracteres, nombre, ahorros))
print()
print('Nombre: {:.{c}} - Ahorros: {:.{p}f}'.format(nombre, ahorros, c=cantidad_caracteres, p=precision))


# Ejercicio 799: Parametrizar la cadena de formato de un objeto de tipo fecha (datetime).
from datetime import datetime
fecha = datetime(2002, 10, 8, 13, 19, 23)
print(fecha)
print()
# Parametrizar la salida de una fecha:
print('{:{formatoFecha} {formatoHora}}'.format(fecha, formatoFecha='%Y/%m/%d', formatoHora='%H:%M'))


# Ejercicio 800: Crear una función para generar un rango de valores reales (punto flotante).
def rango_valores_reales(inicio, final, salto=1.0):
    x = float(inicio)
    y = float(final)
    x_0 = x
    epsilon = salto / 2.0
    i = 0.0
    yield x
    while x + epsilon < y:
        i += 1.0
        x = x_0 + i * salto
        yield x
valores = list(rango_valores_reales(0.0, 1.0, 0.1))
print(valores)
print(len(valores))


# Ejercicio 801: Generar una fecha aleatoria para el año en curso.
from datetime import date
from random import randint
def fecha_aleatoria():
    fecha_inicio = date.today().replace(day=1, month=1).toordinal()
    fecha_final = date.today().toordinal()
    fecha = date.fromordinal(randint(fecha_inicio, fecha_final))
    return fecha
for _ in range(10):
    print(fecha_aleatoria())


# Ejercicio 802: Crear una función para calcular el máximo común divisor (MCD).
from math import floor
def mcd(x, y):
    if x < y:
        return mcd(y, x)
    while y != 0:
        x, y = y, x % y
    return x
print(mcd(3, 2))
print(mcd(8, 4))
print(mcd(150, 304))
print(mcd(13, 17))
print(mcd(19, 29))
print(mcd(1000, 10))


# Ejercicio 802: Crear una función para convertir un color RGB en HSV.
def rgb_a_hsv(r, g, b):
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    minimo = min(r, g, b)
    maximo = max(r, g, b)
    diferencia = maximo - minimo
    if minimo == maximo:
        h = 0
    elif maximo == r:
        h = (60 * ((g - b)/diferencia) + 360) % 360
    elif maximo == g:
        h = (60 * ((g - b)/diferencia) + 120) % 360
    elif maximo == b:
        h = (60 * ((g - b)/diferencia) + 240) % 360
    if maximo == 0:
        s = 0
    else:
        s = (diferencia / maximo) * 100
    v = maximo * 100
    return h, s, v
print(rgb_a_hsv(255, 0, 0))
print(rgb_a_hsv(255, 120, 30))


# Ejercicio 804: Encontrar los números cuadrados perfectos en un rango de valores.
def cuadrados_perfectos(a, b):
    cuadrados = []
    for i in range(a, b + 1):
        n = 1
        while n * n <= i:
            if n * n == i:
                cuadrados.append(i)
            n += 1
    return cuadrados
resultado = cuadrados_perfectos(1, 100)
print(resultado)


# Ejercicio 805: Calcular la distancia euclidiana entre dos puntos en un espacio tridimensional.
from math import sqrt
def distancia_euclidiana_3d(punto_1, punto_2):
    distancia = sqrt(sum([(a - b) ** 2 for a, b in zip(punto_1, punto_2)]))
    return distancia
punto_1 = (2, 3, 5)
punto_2 = (7, 3, 11)
resultado = distancia_euclidiana_3d(punto_1, punto_2)
# (2 - 7) ** 2 + (3 - 3) ** 2 + (5 - 11) ** 2
# 25 + 0 + 36 = 61
# sqrt(61) = 
print(resultado)


# Ejercicio 806: Convertir un número entero a un valor hexadecimal.
for n in range(10):
    print('Entero: {} - Hexadecimal: {}'.format(n, format(n, '#04x')))


# Ejercicio 807: Tomar un valor al azar desde una lista con la función shuffle().
from random import shuffle
numeros = list(range(1, 101))
print(numeros)
print()
shuffle(numeros)
print(numeros)
print()
numero = numeros.pop()
print(numero)


# Ejercicio 808: Leer el contenido completo de un archivo de texto plano.
ruta = 'Parte001/palabras_ingles.txt'
with open(ruta, 'r') as f:
    for l in f.readlines():
        print('Palabra: %s' % l)


# Ejercicio 809: Leer e imprimir las n primeras líneas de un archivo de texto plano.
from itertools import islice
def leer_n_lineas_archivo(archivo, n=20):
    with open(archivo, 'r') as f:
        for l in islice(f, n):
            print(l, end='')
nombre_archivo = 'Parte001/palabras_ingles.txt'
n = 50
leer_n_lineas_archivo(nombre_archivo, n)


# Ejercicio 810: Escribir contenido a un archivo de texto plano con la función write().
nombre_archivo = 'Parte001/ciudades.txt'
with open(nombre_archivo, 'w', encoding='utf-8') as f:
    while True:
        ciudad = input('Escriba un nombre de ciudad (TERMINAR para finalizar el ingreso de datos): ')
        if ciudad != 'TERMINAR':
            f.write(ciudad)
            f.write('\n')
        else:
            break
    print('Ha finalizado la escritura del archivo.')


# Ejercicio 811: Leer el contenido de un archivo por medio de la función readline().
nombre_archivo = 'Parte001/ciudades.txt'
with open(nombre_archivo, 'r', encoding='utf-8') as f:
    linea = f.readline()
    while linea:
        print(linea, end='')
        linea = f.readline()


# Ejercicio 812: Leer todo el contenido de un archivo con readlines() sobre una lista.
def leer_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError as e:
        print('El archivo no existe.')
nombre_archivo = 'Parte001/ciudades.txt'
resultado = leer_archivo(nombre_archivo)
print(resultado)
print()
resultado = [c.replace('\n', '') for c in resultado]
print(resultado)


# Ejercicio 813: Encontrar la palabra más larga almacenada en un archivo de texto plano.
def palabra_mas_larga(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.readline()
            palabras = contenido.split()
            print('Cantidad de palabras:', len(palabras))
            indice = 0
            palabra = palabras[indice]
            longitud = len(palabra)
            for i in range(1, len(palabras)):
                if len(palabras[i]) > longitud:
                    indice = i
                    palabra = palabras[i]
                    longitud = len(palabra)
            return palabra, indice
    except FileNotFoundError as e:
        print('El archivo especificado no existe.')
nombre_archivo = 'Parte001/lorem.txt'
resultado = palabra_mas_larga(nombre_archivo)
print(resultado)


# Ejercicio 814: Encontrar la frecuencia de palabras en una frase de un archivo de texto.
from collections import Counter
def encontrar_frecuencia(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.readline()
            palabras = contenido.split()
            return Counter(palabras)
    except FileNotFoundError:
        print('El archivo especificado no se ha encontrado.')
nombre_archivo = 'Parte001/lorem.txt'
conteo = encontrar_frecuencia(nombre_archivo)
print(conteo)


# Ejercicio 815: Encontrar el tamaño en bytes de un archivo de texto plano.
from os import stat
def calcular_tamagnio(archivo):
    try:
        informacion_archivo = stat(archivo)
        return informacion_archivo.st_size
    except FileNotFoundError:
        return None
nombre_archivo = 'Parte001/lorem.txt'
resultado = calcular_tamagnio(nombre_archivo)
print(resultado)


# Ejercicio 816: Escribir una lista de cadenas de caracteres en un archivo de texto plano.
def escribir_lista(archivo, lista):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for e in lista:
                f.write('{}\n'.format(e))
    except FileNotFoundError:
        print('El archivo indicado no existe.')
nombre_archivo = 'Parte001/colores.txt'
colores = ['Rojo', 'Verde', 'Azul', 'Blanco', 'Negro', 'Gris', 'Amarillo', 'Morado']
escribir_lista(nombre_archivo, colores)


# Ejercicio 817: Copiar un archivo con la función copyfile() del módulo shutil.
from shutil import copyfile
archivo_origen = 'Parte001/lorem.txt'
archivo_destino = 'Parte001/lorem_copia.txt'
copyfile(archivo_origen, archivo_destino)


# Ejercicio 818: Combinar dos archivos de texto plano en un único archivo.
def combinar_archivos(archivo_1, archivo_2, nuevo_archivo):
    try:
        with open(archivo_1, 'r', encoding='utf-8') as f1, open(archivo_2, 'r', encoding='utf-8') as f2, open(nuevo_archivo, 'w', encoding='utf-8') as f3:
            for l1, l2 in zip(f1, f2):
                f3.write(l1)
                f3.write('\n')
                f3.write(l2)
    except FileNotFoundError:
        print('Uno o ambos archivos no existen.')
faust = 'Parte001/faust.txt'
lorem = 'Parte001/lorem.txt'
nuevo_archivo = 'Parte001/faust_lorem.txt'
combinar_archivos(faust, lorem, nuevo_archivo)


# Ejercicio 819: Leer una línea aleatoria desde un archivo de texto plano con choice().
from random import choice
def linea_aleatoria(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.read().splitlines()
            return choice(lineas)
    except FileNotFoundError:
        return None
nombre_archivo = 'Parte001/ciudades.txt'
resultado = linea_aleatoria(nombre_archivo)
print(resultado)


# Ejercicio 820: Comprobar si un archivo está abierto con la propiedad closed.
nombre_archivo = 'Parte001/ciudades.txt'
archivo = open(nombre_archivo, 'r', encoding='utf-8')
print(archivo.closed)
archivo.close()
print(archivo.closed)


# Ejercicio 821: Remover los caracteres de salto de línea del contenido de un archivo.
def remover_saltos_linea(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            lineas = list(map(lambda l: l.rstrip('\n'), lineas))
            return lineas
    except FileNotFoundError:
        print('El archivo especificado no existe.')
resultado = remover_saltos_linea('Parte001/ciudades.txt')
print(resultado)


# Ejercicio 822: Listar todos los archivos de texto plano que hay en un directorio.
from glob import glob
def listar_archivos_texto_plano(ruta):
    listado_archivos = glob(ruta)
    return listado_archivos
directorio = 'Parte001/*.txt'
resultado = listar_archivos_texto_plano(directorio)
for f in resultado:
    print(f)


# Ejercicio 823: Generar 26 archivos de texto plano para las letras del abecedario.
# A.txt, B.txt, C.txt, ..., Z.txt
import string, os
def generar_archivos(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    for l in string.ascii_uppercase:
        with open(os.path.join(ruta, '%s.txt' % l), 'w', encoding='utf-8') as f:
            f.writelines(l)
ruta = 'Parte001/letras'
generar_archivos(ruta)


# Ejercicio 824: Comnprobar si una ruta corresponde con un directorio (carpeta).
import os
ruta = 'Parte001/ciudades.txt'
print(os.path.isdir(ruta))
print()
ruta = 'Parte001/'
print(os.path.isdir(ruta))


# Ejercicio 825: Comprobar si una cadena de caracteres únicamente contiene ciertos caracteres.
import re
def contiene_caracteres(texto):
    patron = re.compile(r'[a-zA-Z0-9.]')
    return bool(patron.search(texto))
cadena = 'Python'
print(contiene_caracteres(cadena))
print()
cadena = '#@/-*'
print(contiene_caracteres(cadena))


# Ejercicio 826: Comprobar si una cadena de caracteres representa un número entero positivo.
import re
def es_numero_entero_positivo(cadena):
    patron = '^[0-9]+$'
    return bool(re.search(patron, cadena))
texto = '123a'
print(es_numero_entero_positivo(texto))
print()
texto = '123'
print(es_numero_entero_positivo(texto))
print()
texto = '-123'
print(es_numero_entero_positivo(texto))


# Ejercicio 827: Comprobar si una cadena de caracteres representa un número entero.
import re
def es_entero(cadena):
    patron = '^[-]{0,1}[0-9]+$'
    return bool(re.search(patron, cadena))
texto = '1000a'
print(es_entero(texto))
print()
texto = '1000'
print(es_entero(texto))
print()
texto = '-1000'
print(es_entero(texto))
print()
texto = '--1000'
print(es_entero(texto))
print()
texto = '1000.101'
print(es_entero(texto))


# Ejercicio 828: Comprobar si una cadena de caracteres representa un número real.
import re
def es_real(cadena):
    patron = r'^-?[0-9]+\.[0-9]+$'
    return bool(re.search(patron, cadena))
texto = '123'
print(es_real(texto))
print()
texto = '123.456'
print(es_real(texto))
print()
texto = '-123'
print(es_real(texto))
print()
texto = '-123.456a'
print(es_real(texto))
print()
texto = '-123.456'
print(es_real(texto))


# Ejercicio 829: Comprobar si una cadena de caracteres representa un número entero o real.
import re
def es_numero(cadena):
    patron = r'^(\d+(\.\d+)?)$'
    return bool(re.search(patron, cadena))
texto = '123a'
print(es_numero(texto))
print()
texto = '123'
print(es_numero(texto))
print()
texto = '123.'
print(es_numero(texto))
print()
texto = '123.456a'
print(es_numero(texto))
print()
texto = '123.456'
print(es_numero(texto))


# Ejercicio 830: Comprobar si un cadena de caracteres es una fecha con formato AAAA/MM/DD.
import re
def es_fecha_valida(cadena):
    patron = '^20[0-9]{2}/(0\d|1[0-2])/(0\d|1[0-9]|2[0-9]|3[0-1])$'
    return bool(re.search(patron, cadena))
fecha = '2001/01/01'
print(es_fecha_valida(fecha))
print()
fecha = '1984/01/01'
print(es_fecha_valida(fecha))
print()
fecha = '2184/01/01'
print(es_fecha_valida(fecha))
print()
fecha = '2020/13/01'
print(es_fecha_valida(fecha))
print()
fecha = '2020/12/01'
print(es_fecha_valida(fecha))
print()
fecha = '2020/12/32'
print(es_fecha_valida(fecha))


# Ejercicio 831: Comprobar si una cadena es una fecha (usar cualquier separador).Python - Ejercicio 831: Comprobar si una Cadena es una Fecha (Usar Cualquier Separador)
# AAAA-MM-DD
# AAAA/MM/DD
# AAAA.MM.DD
import re
def es_fecha_valida(cadena):
    patron = '^20[0-9]{2}(\.|/|-)(0\d|1[0-2])(\.|/|-)(0\d|1\d|2\d|3[0-1])$'
    return bool(re.search(patron, cadena))
fecha = '2020/06/13'
print(es_fecha_valida(fecha))
print()
fecha = '2020-06-13'
print(es_fecha_valida(fecha))
print()
fecha = '2020.06.13'
print(es_fecha_valida(fecha))
print()
fecha = '2020.13.13'
print(es_fecha_valida(fecha))
print()
fecha = '2020/06/43'
print(es_fecha_valida(fecha))


# Ejercicio 832: Comprobar si una cadena empieza con a y termina con b.
# a...b
import re
def es_cadena_valida(cadena):
    patron = '^a.*?b$'
    return bool(re.search(patron, cadena))
texto = 'aadddd,,,,,d'
print(es_cadena_valida(texto))
print()
texto = 'ad'
print(es_cadena_valida(texto))
print()
texto = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssssb'
print(es_cadena_valida(texto))
print()
texto = 'a@     -#sslkñsklsjkljlksjklkljsb'
print(es_cadena_valida(texto))


# Ejercicio 833: Comprobar si un texto empieza con una palabra por medio de una expresión regular.
import re
def empieza_con_palabra(frase):
    patron = '^[a-zA-Z]+'
    return bool(re.search(patron, frase))
texto = '¡Python es tremendo!'
print(empieza_con_palabra(texto))
print()
texto = 'Python es tremendo!'
print(empieza_con_palabra(texto))
print()
texto = ' Python es tremendo!'
print(empieza_con_palabra(texto))
print()
texto = '3Python es tremendo!'
print(empieza_con_palabra(texto))
print()
texto = 'python es tremendo!'
print(empieza_con_palabra(texto))
print()
texto = '@Python es tremendo!'
print(empieza_con_palabra(texto))


# Ejercicio 834: Comprobar si un texto termina con una palabra por medio de una expresión regular.
import re
def termina_en_palabra(frase):
    patron = '[a-zA-Z]+$'
    return bool(re.search(patron, frase))
texto = 'Python 3.8.0'
print(termina_en_palabra(texto))
print()
texto = 'Python 3.8.0 es una de últimas versiones'
print(termina_en_palabra(texto))
print()
texto = 'John Ortiz Ordoñez'
print(termina_en_palabra(texto))
print()
texto = '¡Python es tremendo!'
print(termina_en_palabra(texto))


# Ejercicio 835: Comprobar si un texto termina con una palabra y puntuación opcional.
import re
def termina_palabra_puntuacion(frase):
    patron = '[a-zA-Z]+\S*$'
    return bool(re.search(patron, frase))
texto = 'Python es un lenguaje de programación.'
print(termina_palabra_puntuacion(texto))
print()
texto = 'Python es un lenguaje de programación'
print(termina_palabra_puntuacion(texto))
print()
texto = 'Python es un lenguaje de programación '
print(termina_palabra_puntuacion(texto))
print()
texto = 'Python v. 3.8.0.'
print(termina_palabra_puntuacion(texto))


# Ejercicio 836: Comprobar si existe una palabra que contenga el carácter z.
import re
def frase_palabra_caracter_z(frase):
    patron = '\w*(z|Z).?\w*'
    return bool(re.search(patron, frase))
texto = 'Python es tremendo'
print(frase_palabra_caracter_z(texto))
print()
texto = 'John Ortiz'
print(frase_palabra_caracter_z(texto))
print()
texto = 'JOHN ORTIZ'
print(frase_palabra_caracter_z(texto))
print()
texto = 'El zorro es un animal.'
print(frase_palabra_caracter_z(texto))


# Ejercicio 837: Verificar que exista una palabra donde la letra z no esté al inicio ni al final.
import re
def verificar_palabra(frase):
    patron = '\B(z|Z)\B'
    return bool(re.search(patron, frase))
texto = 'La zanahoria es de color naranja'
print(verificar_palabra(texto))
print()
texto = 'La zanahoria es una hortaliza'
print(verificar_palabra(texto))
print()
texto = 'LA ZANAHORIA ES UNA HORTALIZA'
print(verificar_palabra(texto))


# Ejercicio 838: Comprobar que una palabra esté compuesta por caracteres alfanuméricos y el carácter de guion al piso.
import re
def validar_palabra(palabra):
    patron = '^[a-zA-Z0-9_]+$'
    return bool(re.search(patron, palabra))
texto = 'Python 3.8.0'
print(validar_palabra(texto))
print()
texto = 'Python_3.8.0'
print(validar_palabra(texto))
print()
texto = 'Python_3_8_0'
print(validar_palabra(texto))
print()
texto = ' Python_3_8_0 '
print(validar_palabra(texto))


# Ejercicio 839: Comprobar que una cadena empiece con un número específico.
import re
def empieza_con_numero(cadena):
    patron = '^3'
    return bool(re.search(patron, cadena))
texto = 'TresCuatro'
print(empieza_con_numero(texto))
print()
texto = '2.1'
print(empieza_con_numero(texto))
print()
texto = ' 3.1'
print(empieza_con_numero(texto))
print()
texto = '\n3.1'
print(empieza_con_numero(texto))
print()
texto = '3.1'
print(empieza_con_numero(texto))


# Ejercicio 840: Comprobar si una cadena de caracteres empieza con un número.
import re
def empieza_con_numero(cadena):
    patron = '^[0-9]'
    return bool(re.search(patron, cadena))
texto = 'Python es tremendo'
print(empieza_con_numero(texto))
print()
texto = ' 5 lenguajes de programación'
print(empieza_con_numero(texto))
print()
texto = '\t5 lenguajes de programación'
print(empieza_con_numero(texto))
print()
texto = '5 lenguajes de programación'
print(empieza_con_numero(texto))


# Ejercicio 841: Remover los ceros al inicio de cada octeto de una dirección IP.
import re
def remover_ceros_al_inicio(ip):
    patron = '\.[0]*'
    return re.sub(patron, '.', ip)
direccion_ip = '192.168.013.001' # 192.168.13.1
print(remover_ceros_al_inicio(direccion_ip))


# Ejercicio 842: Comprobar si una cadena de caracteres termina con un número específico.
import re
def termina_en_numero(texto):
    patron = '3$'
    return bool(re.search(patron, texto))
cadena = 'Su número favorito es 7'
print(termina_en_numero(cadena))
print()
cadena = 'Su número favorito es 3.'
print(termina_en_numero(cadena))
print()
cadena = 'Su número favorito es 3\n'
print(termina_en_numero(cadena))
print()
cadena = 'Su número favorito es 3\t'
print(termina_en_numero(cadena))
print()
cadena = 'Su número favorito es 3'
print(termina_en_numero(cadena))


# Ejercicio 843: Comprobar si una cadena de caracteres termina en un número cualquiera.
import re
def termina_en_numero(texto):
    patron = '[0-9]$'
    return bool(re.search(patron, texto))
texto = 'La versión mayor de Python es la número 3.'
print(termina_en_numero(texto))
print()
texto = 'La versión mayor de Python es la número 3\n'
print(termina_en_numero(texto))
print()
texto = 'La versión mayor de PHP es la número 7'
print(termina_en_numero(texto))
print()
texto = 'El primer entero negativo es -1'
print(termina_en_numero(texto))
print()
texto = 'El primer entero negativo es -1\t'
print(termina_en_numero(texto))


# Ejercicio 844: Encontrar números enteros de hasta 3 cifras en una cadena de caracteres.
import re
frase = 'Algunos ejemplos de números primos: 1429, 11, 991, 67, 1033, 2, 3, y 5'
patron = r'\b\d{1,3}\b'
resultado = re.finditer(patron, frase)
for n in resultado:
    print(n.group(0))


# Ejercicio 845: Comprobar si una cadena contiene una lista de palabras.
import re
def contiene_palabras(palabras, frase):
    for p in palabras:
        if re.search(p, frase):
            print('La palabra `{}` se ha encontrado en la frase.'.format(p))
        else:
            print('La palabra `{}` NO se ha encontrado en la frase.'.format(p))
frase = 'Python es un lenguaje de programación multiparadigama. La versión actual es 3.8.2'
palabras = ['Python', 'versión', 'lenguaje', 'software', 'código']
contiene_palabras(palabras, frase)


# Ejercicio 846: Encontrar una palabra e indicar su posición de inicio y final en una frase.
import re
frase = 'Python es un lenguaje de programación multiparadigma.'
palabra = 'lenguaje'
resultado = re.search(palabra, frase)
inicio = resultado.start()
final = resultado.end()
print('La palabra {} se encontró al inicio {} y final {}.'.format(palabra, inicio, final))


# Ejercicio 847: Encontrar todas las ocurrencias de una palabra en una frase.
import re
frase = 'Ejercicios Python, Curso Python, Laboratorio Python'
palabra = 'Python'
for r in re.findall(palabra, frase):
    print('Encontrado: %s' % r)


# Ejercicio 848: Encontrar todas las ocurrencias de una palabra en una frase y su posición.
import re
frase = 'Ejercicios Python, Curso Python, Laboratorio Python'
palabra = 'Python'
for r in re.finditer(palabra, frase):
    inicio = r.start()
    final = r.end()
    palabra_encontrada = frase[inicio:final]
    print('Se ha encontrado la palabra `{}` en las posiciones desde {} hasta {}'.format(palabra_encontrada, inicio, final))


# Ejercicio 849: Reemplazar espacio en blanco en una cadena con la función replace().
frase = '      Python        es  un lenguaje        de programación                 .'
print(frase)
frase = frase.strip()
print(frase)
print()
palabras = frase.split()
print(palabras)
print()
frase = ' '.join([p for p in palabras if p != '.']) + '.'
print(frase)


# Ejercicio 850: Reemplazar espacio en blanco en una cadena con una expresión regular.
import re
frase = '      Python        es  un lenguaje        de programación                 .'
print(frase)
print(len(frase))
frase = frase.strip()[:-2].strip()
print(frase)
print()
remover_espacio_blanco = re.compile(r'\s+')
frase = remover_espacio_blanco.sub(' ', frase)
print(frase)
print(len(frase))


# Ejercicio 851: Extraer la fecha desde una dirección Web (URL) con una expresión regular.
import re
# https://ortizol.blogspot.com/2020/06/20/python-ejercicio-849-reemplazar-el.html
def extraer_fecha_url(url):
    patron = r'/(\d{4})/(\d{2})/(\d{2})/'
    return re.findall(patron, url)
direccion_web = 'https://ortizol.blogspot.com/2020/06/20/python-ejercicio-849-reemplazar-el.html'
fecha = extraer_fecha_url(direccion_web)
print(fecha[0])


# Ejercicio 852: Cambiar el formato de una fecha con una expresión regular (regex).
# Fuente: AAAA/MM/DD
# Destino: DD-MM-AAAA
import re
def cambiar_formato(fecha):
    patron = r'(\d{4})/(\d{2})/(\d{2})'
    return re.sub(patron, '\\3-\\2-\\1', fecha)
fecha_registro = '2003/03/13'
print('Fecha con el formato original:', fecha_registro)
fecha_nuevo_formato = cambiar_formato(fecha_registro)
print('Fecha con el formato modificado:', fecha_nuevo_formato)


# Ejercicio 853: Encontrar dos palabras que empiecen con la misma letra en un listado.
import re
lenguajes = ['C C++', 'Java JavaScript', 'Ruby R', 'Python PHP']
for l in lenguajes:
    resultado = re.match('(P\w+)\W(P\w+)', l)
    if resultado:
        print(resultado.groups())


# Ejercicio 854: Extraer los números de una cadena de caracteres con la función re.split().
from re import split
frase = 'Cinco 5, Diez 10, Catorce 14, Veinte 20'
resultado = split('\D+', frase)
for n in resultado:
    print(n)


# Ejercicio 855: Encontrar todas las palabras que empiecen con las vocales a y e.
import re
extracto = "Loca ligeros pensamiento tierra que quemadas comida. Para las alegrísima latido desnudo convexa pero abrir. De lenta abeja del por de subía la despenada, quedo ansioso borrachos es la que y, tierra hombrecillo se resonancia quedo todo. Es la muerte los sillas borrando, pulso ojos deja mujer la. De de tierra nunca las de gustada sus diana hombrecillo, brooklyn resonancia llenando lenguas golondrina, la tierra heridas con es. De que cosas musgos me que pulso, con mujer y para ligeros donde la con pies repartiendo, ciudades queman es sus el plata. Bajo apariencia la el los la escaleras quedo, amor."
patron = r'\b[AaEe]\w+\b'
resultado = re.findall(patron, extracto)
for p in resultado:
    print(p)


# Ejercicio 856: Extraer los números y posiciones desde una cadena de caracteres.
import re
frase = 'En el canal de YouTube hay aproximadamente 653 vídeos de Ejercicios de JavaScript. También se encuentra alrededor de 400 Ejercicios de Java. De manera análoga para el lenguaje de programación Python se pueden encontrar alrededor de 850 vídeos actualmente. En cuanto a Lodash, hay 10 ejercicios.'
patron = '\d+'
for r in re.finditer(patron, frase):
    print('Número:', r.group(0))
    print('Posición:', r.start())
    print()


# Ejercicio 857: Reemplazar todas las coincidencias de un valor en una cadena de caracteres.
import re
parrafo = 'Historia del Siglo XX. En el siglo pasado se inventaron diferentes dispositivos para el progreso de la humanidad. Uno de los inventos más sobresalientes es el computador. Esta invención cambió el mundo en Siglo XX: la economía, las relaciones humanas, la política, la educación y otros aspectos relevantes. El Siglo XX será recordado como un hito en la historia de la humanidad.'
patron = 'XX'
resultado = re.sub(patron, '20', parrafo)
print(resultado)


# Ejercicio 858: Reemplazar todas las coincidencias el punto, la coma y el punto y coma por dos puntos (:).
import re
parrafo = 'Historia del Siglo XX. En el siglo pasado se inventaron diferentes dispositivos para el progreso de la humanidad. Uno de los inventos más sobresalientes es el computador. Esta invención cambió el mundo en Siglo XX: la economía, las relaciones humanas, la política, la educación y otros aspectos relevantes. El Siglo XX será recordado como un hito en la historia de la humanidad; una nueva perspectiva del mundo.'
patron = '[.,;]'
resultado = re.sub(patron, ':', parrafo)
print(resultado)


# Ejercicio 859: Encontrar todas las palabras de cinco (5) letras en un texto.
import re
extracto = 'Al abrir luna el todo nube, criaturas y acaba los para me recodos que huevos aire, los la el diana ilesa en cosas los. La y ligeros borrachos signos, arcos con pisotean se las no que mudas es. Vilo huido resonancia nino la larga, hule vuelve de la ceniza vuelve resonancia. Los y diminutas helechos mármol que de de manteles me, arroyo el las yo los muertos donde con la de. Estremecidos desgarrados los la fría. Diana diana la arcos las tierra escaleras llanura que desnudo. Me vengo oh luna tierra osos muerte para de. El lentejas de y el...'
patron = r'\b\w{5}\b'
resultado = re.findall(patron, extracto)
print(len(resultado))
print(resultado)


# Ejercicio 860: Encontrar todas las palabras que tengan entre 3 y 5 letras en un texto.
import re
extracto = 'Al abrir luna el todo nube, criaturas y acaba los para me recodos que huevos aire, los la el diana ilesa en cosas los. La y ligeros borrachos signos, arcos con pisotean se las no que mudas es. Vilo huido resonancia nino la larga, hule vuelve de la ceniza vuelve resonancia. Los y diminutas helechos mármol que de de manteles me, arroyo el las yo los muertos donde con la de. Estremecidos desgarrados los la fría. Diana diana la arcos las tierra escaleras llanura que desnudo. Me vengo oh luna tierra osos muerte para de. El lentejas de y el...'
patron = r'\b\w{3,5}\b'
resultado = re.findall(patron, extracto)
print(len(resultado))
print()
for p in resultado:
    print(p)


# Ejercicio 861: Convertir el nombre de una variable de modo camel case a snake case.
# Camel case: NombreVariable
# Snake case: nombre_variable
import re
def conversion_case(nombre_variable):
    conversion = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', nombre_variable)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', conversion).lower()
print(conversion_case('NombreVariable'))


# Ejercicio 862: Convertir el nombre de una variable de modo snake case a camel case.
# Snake case: nombre_variable
# Camel case: NombreVariable
def conversion_case(nombre_variable):
    return ''.join(p.capitalize() for p in nombre_variable.split('_'))
print(conversion_case('nombre_variable'))
print(conversion_case('edad_persona'))


# Ejercicio 863: Extraer todas las palabras que se hallen entre comillas dobles desde una cadena de caracteres.
import re
texto = '"Python", "JavaScript", "C++", "Java"'
patron = r'"(.*?)"'
lenguajes = re.findall(patron, texto)
print(lenguajes)
print()
for l in lenguajes:
    print(l)


# Ejercicio 864: Remover el espacio intermedio que halla entre cada palabra de una frase.
from re import sub
texto = 'Python            es un                  lenguaje de            programación    multiparadigma.'
print(len(texto))
print(texto)
print()
patron = ' +'
resultado = sub(patron, ' ', texto)
print(len(resultado))
print(resultado)


# Ejercicio 865: Remover todo el espacio en blanco en una cadena de caracteres.
import re
texto = '       Python es un                lenguaje           de    programación           '
print(texto)
print()
patron = r'\s+'
resultado = re.sub(patron, '', texto)
print(resultado)


# Ejercicio 866: Remover todos los caracteres que representen símbolos en un texto.
import re
texto = 'Página oficial de Python (v. 3.8.0): https://www.python.org/.'
patron = '[\W]+'
regex = re.compile(patron)
resultado = regex.sub('', texto)
print(resultado)


# Ejercicio 867: Extraer enlaces (URLs) desde un texto con una expresión regular.
import re
texto = 'Página oficial de Python (v. 3.8.0): https://www.python.org/. URL corta de este canal: http://bit.ly/2SiCmCJ'
patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(patron, texto)
for u in urls:
    print(u)


# Ejercicio 868: Extraer las palabras que inician con mayúscula desde un texto.
import re
texto = 'PythonEsUnLenguajeDeProgramación'
patron = '[A-Z][^A-Z]*'
resultado = re.findall(patron, texto)
print(resultado)


# Ejercicio 869: Sustituir una cadena sin considerar mayúsculas ni minúsculas.
import re
texto = 'Python es un lenguaje de programación. Versión de PyThOn 3.8.0. ¡PYTHON es tremendo! python es multiparadigma.'
print(texto)
print()
regex = re.compile(re.escape('python'), re.IGNORECASE)
resultado = regex.sub('Python', texto)
print(resultado)


# Ejercicio 870: Extraer todas las direcciones de correo electrónico desde un texto.
import re
texto = """
Usuario 1: kronvold@verizon.net
Usuario 2: schumer@live.com
maneesh@outlook.com
richard@sbcglobal.net
daveewart@outlook.com
rfoley@aol.com
mjewell@mac.com
jgoerzen@comcast.net
raines@sbcglobal.net
marioph@outlook.com
jdhildeb@aol.com
janneh@optonline.net
"""
patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
emails = re.findall(patron, texto)
print(emails)


# Ejercicio 871: Encontrar los adverbios terminados en -mente e identificar su posición.
import re
frase = 'Hoy principalmente me he dedicado a subir vídeos al canal de YouTube. Hay un motivo implícito en lo institivo que me impulsa a hacer esto a diario, incansablemente. Lo mejor es aprender a diario... aprender constamente.'
patron = r'\w+mente'
for c in re.finditer(patron, frase):
    print('%s: %d-%d' % (c.group(0), c.start(), c.end()))


# Ejercicio 872: Obtener las palabras que se hallan separadas por múltiples delimitadores.
import re
texto = 'JavaScript;Python\nC++|Java,PHP;C*Perl'
patron = ';|\n|\||,|\*'
lenguajes = re.split(patron, texto)
print(lenguajes)


# Ejercicio 873: Comprobar si una cadena contiene un número decimal con precisión de 2.
import re
def es_decimal(cadena):
    patron = r'^[0-9]+(\.[0-9]{2})$'
    regex = re.compile(patron)
    return bool(regex.search(cadena))
print(es_decimal('987.1'))
print(es_decimal('987.12'))
print(es_decimal('98789877545.123'))
print(es_decimal('987.99'))


# Ejercicio 874: Remover desde un texto aquellas palabras que tengan una longitud específica.
import re
def remover_palabras(texto, cantidad_caracteres):
    patron = '\\b\\w{%d}\\b' % (cantidad_caracteres)
    regex = re.compile(patron)
    return regex.sub('', texto)
cadena = 'Python es un lenguaje de programación multiparadigma.'
longitud = 2
print(cadena)
print()
resultado = remover_palabras(cadena, longitud)
print(resultado)
resultado = re.sub('\s+', ' ', resultado)
print(resultado)


# Ejercicio 875: Remover el contenido textual que se encuentre dentro de paréntesis.
import re
texto = 'Python (v. 3.8.0) - Java (14) - C# (7) - JavaScript (ES6)'
patron = r'\([^)]+\)'
resultado = re.sub(patron, '', texto)
print(resultado)
resultado = re.sub(r'\s+', ' ', resultado)
print(resultado)


# Ejercicio 876: Agregar espacio en blanco entre palabras de una cadena de caracteres.
import re
def separar_palabras(frase):
    patron = r'(\w)([A-Z])'
    return re.sub(patron, r'\1 \2', frase)
cadena = 'PythonEsUnLenguajeDeProgramación'
print(cadena)
print()
resultado = separar_palabras(cadena)
print(resultado)


# Ejercicio 877: Remover los caracteres en minúscula desde una cadena usando una expresión regular.
import re
texto = 'AbCdefGHiJklmnOPQrstuvWXYz'
print(texto)
print()
patron = '[a-z]'
resultado = re.sub(patron, '', texto)
print(resultado)


# Ejercicio 878: Remover los caracteres en mayúscula desde una cadena usando una expresión regular.
import re
texto = 'AbCdefGHiJklmnOPQrstuvWXYz'
print(texto)
print()
patron = '[A-Z]'
resultado = re.sub(patron, '', texto)
print(resultado)


# Ejercicio 879: Establecer conexión con una base de datos SQLite y obtener su versión.
import sqlite3
try:
    conexion = sqlite3.connect('Parte001/bd_sqlite.db')
    cursor = conexion.cursor()
    print('Se ha creado la base de datos.')
    print('Se ha establecido una conexión con la base de datos.')
    sql = 'SELECT sqlite_version();'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print()
    print('Versión de SQLite:', resultado[0][0])
    cursor.close()
except sqlite3.Error as error:
    print('Se ha producido un error:', error)
finally:
    if conexion:
        conexion.close()
        print('\nLa conexión se ha cerrado de forma satisfactoria.')


# Ejercicio 880: Establecer conexión con una base de datos en memoria con SQLite.
import sqlite3
try:
    conexion = sqlite3.connect(':memory:')
    print('Se ha establecido una conexión con la base de datos en memoria.')
    sql = 'SELECT sqlite_version();'
    conexion.execute(sql)
    print('Versión de SQLite:', sqlite3.version)
    conexion.close()
except sqlite3.Error as error:
    print('Se ha producido un error:', error)


# Ejercicio 881: Crear una tabla sobre una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
if conexion:
    conexion.close()


# Ejercicio 882: Mostrar las tablas que se han creado en una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
conexion = crear_conexion('Parte001/usuarios.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
mostrar_tablas(conexion)
if conexion:
    conexion.close()


# Ejercicio 883: Insertar registros (datos) en una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_883.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
if conexion:
    conexion.close()


# Ejercicio 884: Obtener todos los registros (datos) de una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
def recuperar_productos(conexion):
    sql = "SELECT * FROM producto;"
    cursor = conexion.cursor()
    cursor.execute(sql)
    productos = cursor.fetchall()
    for p in productos:
        print(p)
conexion = crear_conexion('Parte001/usuarios_884.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
print()
print('Registros de la tabla `producto`:')
recuperar_productos(conexion)
if conexion:
    conexion.close()


# Ejercicio 885: Obtener un registro particular desde una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
def recuperar_productos(conexion):
    sql = "SELECT * FROM producto;"
    cursor = conexion.cursor()
    cursor.execute(sql)
    productos = cursor.fetchall()
    for p in productos:
        print(p)
def recuperar_producto_por_id(conexion, id):
    sql = "SELECT * FROM producto WHERE id = ?;"
    cursor = conexion.cursor()
    cursor.execute(sql, (id,))
    registros = cursor.fetchall()
    for r in registros:
        print(r)
conexion = crear_conexion('Parte001/usuarios_885.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
print()
print('Registros de la tabla `producto`:')
recuperar_productos(conexion)
print()
id_producto = 2002
print('Registro (producto) con ID %d:' % id_producto)
recuperar_producto_por_id(conexion, id_producto)
if conexion:
    conexion.close()


# Ejercicio 886: Contar la cantidad de registros de una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
def recuperar_productos(conexion):
    sql = "SELECT * FROM producto;"
    cursor = conexion.cursor()
    cursor.execute(sql)
    productos = cursor.fetchall()
    for p in productos:
        print(p)
def recuperar_producto_por_id(conexion, id):
    sql = "SELECT * FROM producto WHERE id = ?;"
    cursor = conexion.cursor()
    cursor.execute(sql, (id,))
    registros = cursor.fetchall()
    for r in registros:
        print(r)
def cantidad_productos(conexion):
    sql = 'SELECT * FROM producto;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    return len(cursor.fetchall())
conexion = crear_conexion('Parte001/usuarios_886.db')
sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
print()
print('Registros de la tabla `producto`:')
recuperar_productos(conexion)
print()
id_producto = 2002
print('Registro (producto) con ID %d:' % id_producto)
recuperar_producto_por_id(conexion, id_producto)
print()
print('Cantidad de productos actuales:', cantidad_productos(conexion))
if conexion:
    conexion.close()


# Ejercicio 887: Insertar un registro del usuario en una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario VALUES (?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_887.db')
sql = """
CREATE TABLE usuario (
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
while True:
    try:
        id_usuario = int(input('Ingrese el ID del usuario: '))
        if id_usuario > 0:
            break
        else:
            print('MENSAJE: Debe ingresar un valor entero positivo.')
    except ValueError:
        print('MENSAJE: Debe ingreser un valor entero.')
    print()
while True:
    nombre = input('Ingrese su nombre: ').strip()
    if len(nombre):
        break
    else:
        print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
    print()
while True:
    clave = input('Ingrese su clave: ').strip()
    if len(clave):
        break
    else:
        print('MENSAJE: Debe ingresar una cadena con un valor específico para la clave.')
    print()
crear_usuario(conexion, (id_usuario, nombre, clave))
if conexion:
    conexion.close()


# Ejercicio 888: Modificar un registro en una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario VALUES (?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def mostrar_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)
def solicitar_datos_usuario():
    while True:
        try:
            id_usuario = int(input('Ingrese el ID del usuario: '))
            if id_usuario > 0:
                break
            else:
                print('MENSAJE: Debe ingresar un valor entero positivo.')
        except ValueError:
            print('MENSAJE: Debe ingreser un valor entero.')
        print()
    while True:
        nombre = input('Ingrese su nombre: ').strip()
        if len(nombre):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
        print()
    while True:
        clave = input('Ingrese su clave: ').strip()
        if len(clave):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para la clave.')
        print()
    return id_usuario, nombre, clave
def actualizar_usuario(conexion, usuario):
    sql = 'UPDATE usuario SET nombre = ?, clave = ? WHERE id = ?;'
    cursor = conexion.cursor()
    cursor.execute(sql, (usuario[1], usuario[2], usuario[0]))
conexion = crear_conexion('Parte001/usuarios_888.db')
sql = """
CREATE TABLE usuario (
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)
mostrar_usuarios(conexion)
usuario = solicitar_datos_usuario()
actualizar_usuario(conexion, usuario)
mostrar_usuarios(conexion)
if conexion:
    conexion.close()


# Ejercicio 889: Eliminar un registro en una tabla de una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario VALUES (?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def mostrar_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)
def solicitar_datos_usuario():
    while True:
        try:
            id_usuario = int(input('Ingrese el ID del usuario: '))
            if id_usuario > 0:
                break
            else:
                print('MENSAJE: Debe ingresar un valor entero positivo.')
        except ValueError:
            print('MENSAJE: Debe ingreser un valor entero.')
        print()
    while True:
        nombre = input('Ingrese su nombre: ').strip()
        if len(nombre):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
        print()
    while True:
        clave = input('Ingrese su clave: ').strip()
        if len(clave):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para la clave.')
        print()
    return id_usuario, nombre, clave
def eliminar_usuario(conexion, id_usuario):
    sql = 'DELETE FROM usuario WHERE id = ?;'
    cursor = conexion.cursor()
    cursor.execute(sql, (id_usuario, ))
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_889.db')
sql = """
CREATE TABLE usuario (
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)
print()
usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)
mostrar_usuarios(conexion)
print()
while True:
    try:
        id_usuario = int(input('Ingrese el ID del usuario a eliminar: '))
        if id_usuario > 0:
            break
        else:
            print('MENSAJE: Debe ingresar un valor entero positivo.')
    except ValueError:
        print('MENSAJE: Debe ingreser un valor entero.')
    print()
eliminar_usuario(conexion, id_usuario)
mostrar_usuarios(conexion)
if conexion:
    conexion.close()


# Ejercicio 890: Crear una columna como llave primaria autoincremental en una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave) VALUES (?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def mostrar_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)
def solicitar_datos_usuario():
    while True:
        nombre = input('Ingrese su nombre: ').strip()
        if len(nombre):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
        print()
    while True:
        clave = input('Ingrese su clave: ').strip()
        if len(clave):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para la clave.')
        print()
    return nombre, clave
conexion = crear_conexion('Parte001/usuarios_890.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)
print()
usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)
print()
mostrar_usuarios(conexion)
if conexion:
    conexion.close()


# Ejercicio 891: Modificar con ALTER TABLE una tabla en una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def modificar_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_891.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = "ALTER TABLE usuario ADD COLUMN email TEXT NOT NULL DEFAULT '@';"
modificar_tabla(conexion, sql)
if conexion:
    conexion.close()


# Ejercicio 892: Crear una copia de seguridad de una base de datos tipo SQLite.
import sqlite3
import io
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
def crear_copia_seguridad(conexion, archivo):
    with io.open(archivo, 'w') as f:
        for d in conexion.iterdump():
            f.write('%s\n' % d)
conexion = crear_conexion('Parte001/usuarios_892.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
print()
archivo_copia = 'Parte001/copia_seguridad_usuarios.sql'
crear_copia_seguridad(conexion, archivo_copia)
if conexion:
    conexion.close()


# Ejercicio 893: Borrar todos los registros de una tabla de una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
def recuperar_productos(conexion):
    sql = "SELECT * FROM producto;"
    cursor = conexion.cursor()
    cursor.execute(sql)
    productos = cursor.fetchall()
    for p in productos:
        print(p)
def eliminar_productos(conexion):
    sql = 'DELETE FROM producto;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_893.db')
sql = """
CREATE TABLE producto (
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print()
print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)
print()
recuperar_productos(conexion)
print()
eliminar_productos(conexion)
recuperar_productos(conexion)
if conexion:
    conexion.close()


# Ejercicio 894: Borrar una tabla específica de una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()
    for t in tablas:
        print(t[0])
def eliminar_tabla(conexion, tabla):
    sql = 'DROP TABLE %s' % tabla
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_894.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)
sql = """
CREATE TABLE producto (
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
print()
eliminar_tabla(conexion, 'producto')
print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)
if conexion:
    conexion.close()


# Ejercicio 895: Restaurar una base de datos SQLite desde un archivo.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def restaurar_copia_seguridad(conexion, archivo):
    with open(archivo, 'r') as f:
        sql = f.read()
    try:
        cursor = conexion.cursor()
        cursor.executescript(sql)
        cursor.close()
    except sqlite3.Error as e:
        print('Se ha producido un error al restaurar la base datos:', e)
conexion = crear_conexion('Parte001/usuarios_895.db')
nombre_archivo = 'Parte001/copia_seguridad_usuarios.sql'
restaurar_copia_seguridad(conexion, nombre_archivo)
if conexion:
    conexion.close()


# Ejercicio 896: Crear un campo BLOB para almacenar archivos en una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_896.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    foto BLOB NOT NULL
);
"""
crear_tabla(conexion, sql)  
if conexion:
    conexion.close()


# Ejercicio 897: Insertar una imagen en una columna tipo BLOB en una base de datos tipo SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def convertir_a_binario(foto):
    with open(foto, 'rb') as f:
        blob = f.read()
    return blob
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, foto) VALUES (?, ?, ?, ?);'
    foto_binario = convertir_a_binario(usuario[-1])
    usuario = (usuario[0], usuario[1], usuario[2], foto_binario)
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_897.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    foto BLOB NOT NULL
);
"""
crear_tabla(conexion, sql)
print()
foto_archivo = 'Parte001/foto.png'
usuario = ('Germán', 'gaoojs', 'gaoojs@mail.co', foto_archivo)
crear_usuario(conexion, usuario)
print('El usuario se ha creado de forma satisfactoria.')
if conexion:
    conexion.close()


# Ejercicio 898: Leer una columna tipo BLOB desde una base de datos SQLite.
import sqlite3
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def convertir_a_binario(foto):
    with open(foto, 'rb') as f:
        blob = f.read()
    return blob
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, foto) VALUES (?, ?, ?, ?);'
    foto_binario = convertir_a_binario(usuario[-1])
    usuario = (usuario[0], usuario[1], usuario[2], foto_binario)
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def guardar_foto(id_usuario, foto):
    with open('Parte001/foto_{}.png'.format(id_usuario), 'wb') as f:
        f.write(foto)
def leer_usuario(conexion, id_usuario):
    sql = 'SELECT * FROM usuario WHERE id = ?;'
    cursor = conexion.cursor()
    cursor.execute(sql, (id_usuario, ))
    usuarios = cursor.fetchall()
    for u in usuarios:
        print('%d - %s' % (u[0], u[1]))
        guardar_foto(u[0], u[-1])
conexion = crear_conexion('Parte001/usuarios_898.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    foto BLOB NOT NULL
);
"""
crear_tabla(conexion, sql)
print()
foto_archivo = 'Parte001/foto.png'
usuario = ('Germán', 'gaoojs', 'gaoojs@mail.co', foto_archivo)
crear_usuario(conexion, usuario)
print('El usuario se ha creado de forma satisfactoria.')
print()
leer_usuario(conexion, 1)
print('Se han leído los datos del usuario con ID:', 1)
if conexion:
    conexion.close()


# Ejercicio 899: Crear un campo tipo fecha (TIMESTAMP) en una tabla de una base de datos SQLite.
import sqlite3
import datetime
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, fecha_registro) VALUES (?, ?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
conexion = crear_conexion('Parte001/usuarios_899.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_registro TIMESTAMP NOT NULL
);
"""
crear_tabla(conexion, sql)
nombre = 'Daniela'
clave = 'danny'
email = 'danny@mail.co'
fecha_registro = datetime.datetime.now()
usuario = (nombre, clave,  email, fecha_registro)
crear_usuario(conexion, usuario)
print('Se ha creado un nuevo registro en la tabla usuario.')


# Ejercicio 900: Recuperar un campo tipo fecha (TIMESTAMP) desde una tabla de una base de datos SQLite.
import sqlite3
import datetime
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, fecha_registro) VALUES (?, ?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def obtener_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for u in usuarios:
        print('ID:', u[0])
        print('Nombre:', u[1])
        print('Fecha registro:', u[-1])
        print('Fecha registro (tipo de dato):', type(u[-1]))
        # 2020-06-30 17:44:27.634409
        fecha = datetime.datetime.strptime(u[-1], '%Y-%m-%d %H:%M:%S.%f')
        print('Tipo fecha:', type(fecha))
        print()
conexion = crear_conexion('Parte001/usuarios_900.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_registro TIMESTAMP NOT NULL
);
"""
crear_tabla(conexion, sql)
nombre = 'Daniela'
clave = 'danny'
email = 'danny@mail.co'
fecha_registro = datetime.datetime.now()
usuario = (nombre, clave,  email, fecha_registro)
crear_usuario(conexion, usuario)
print('Se ha creado un nuevo registro en la tabla usuario.')
print()
obtener_usuarios(conexion)


# Ejercicio 901: Crear una función sobre una base de datos tipo SQLite.
import sqlite3
import datetime
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)
        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()
def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, fecha_registro) VALUES (?, ?, ?, ?);'
    cursor = conexion.cursor()
    cursor.execute(sql, usuario)
    conexion.commit()
def obtener_usuarios(conexion):
    sql = 'SELECT id, CONVERTIR_MAYUSCULA(nombre), clave, CONVERTIR_MAYUSCULA(email), fecha_registro FROM usuario;'
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for u in usuarios:
        print('ID:', u[0])
        print('Nombre:', u[1])
        print('Fecha registro:', u[-1])
        print('Fecha registro (tipo de dato):', type(u[-1]))
        # 2020-06-30 17:44:27.634409
        fecha = datetime.datetime.strptime(u[-1], '%Y-%m-%d %H:%M:%S.%f')
        print('Tipo fecha:', type(fecha))
        print()
def convertir_mayusculas(texto):
    return str(texto).upper()
def crear_funcion(conexion, nombre_funcion):
    conexion.create_function(nombre_funcion, 1, convertir_mayusculas)
conexion = crear_conexion('Parte001/usuarios_901.db')
sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_registro TIMESTAMP NOT NULL
);
"""
crear_tabla(conexion, sql)
nombre = 'Daniela'
clave = 'danny'
email = 'danny@mail.co'
fecha_registro = datetime.datetime.now()
usuario = (nombre, clave,  email, fecha_registro)
crear_usuario(conexion, usuario)
print('Se ha creado un nuevo registro en la tabla usuario.')
print()
crear_funcion(conexion, 'CONVERTIR_MAYUSCULA')
obtener_usuarios(conexion)
if conexion:
    conexion.close()


# Ejercicio 902: Leer un archivo de texto en formato CSV (Valores Separados por Comas).
import csv
nombre_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia.csv'
with open(nombre_archivo, newline='', encoding='utf-8') as f:
    datos = csv.reader(f, delimiter=',', quotechar=';')
    for r in datos:
        print(r)


# Ejercicio 903: Leer un archivo CSV donde el separador (delimitador) es el tabulador.
import csv
nombre_archivo = 'Parte001/paises.csv'
with open(nombre_archivo, newline='') as f:
    datos = csv.reader(f, delimiter='\t')
    for r in datos:
        print(', '.join(r))


# Ejercicio 904: Leer un archivo CSV sobre una estructura de datos lista.
import csv
nombre_archivo = 'Parte001/paises.csv'
with open(nombre_archivo, newline='') as f:
    datos = csv.reader(f, delimiter='\t')
    paises = list(datos)
print('El tipo de dato de la lista `paises` es:', type(paises))
print(paises)


# Ejercicio 905: Leer un archivo CSV sobre una estructura de datos tipo diccionario.
import csv
nombre_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia_100.csv'
with open(nombre_archivo, newline='', encoding='utf-8') as f:
    covid_19_colombia = csv.DictReader(f)
    for r in covid_19_colombia:
        print(r)


# Ejercicio 906: Leer un archivo CSV y remover el espacio en blanco después del delimitador.
import csv
nombre_archivo = 'Parte001/paises.csv'
with open(nombre_archivo, newline='', encoding='utf-8') as f:
    paises = csv.reader(f, delimiter='\t', skipinitialspace=True)
    for p in paises:
        print(p)


# Ejercicio 907: Registrar un dialecto (configuración) CSV con la función register_dialect().
import csv
csv.register_dialect('dialecto_basico', delimiter='\t', skipinitialspace=True)
ruta_archivo = 'Parte001/paises.csv'
with open(ruta_archivo, encoding='utf-8', newline='') as f:
    datos = csv.reader(f, dialect='dialecto_basico')
    for r in datos:
        print(r)


# Ejercicio 908: Imprimir el valor asociado a determinadas columnas de un archivo CSV.
import csv
ruta_archivo = 'Parte001/Casos_positivos_de_COVID-19_en_Colombia_100.csv'
with open(ruta_archivo, newline='', encoding='utf-8') as f:
    covid_colombia = csv.DictReader(f)
    for r in covid_colombia:
        print(r['ID de caso'], r['Fecha de notificación'], r['Ciudad de ubicación'], r['atención'])


# Ejercicio 909: Omitir el encabezado de un archivo CSV con la función next().
import csv
ruta_archivo = 'Parte001/paises.csv'
with open(ruta_archivo, newline='', encoding='utf-8') as f:
    paises = csv.reader(f, delimiter='\t', skipinitialspace=True)
    next(paises)
    for p in paises:
        print(p)


# Ejercicio 910: Crear un objeto iterable a partir de diferentes colecciones con itertools.chain().
from itertools import chain
numeros = [1, 2, 3]
letras = ['A', 'B', 'C', 'D', 'E']
primos = [11, 13, 17]
iterable = chain(numeros, letras, primos)
for e in iterable:
    print(e, end=' ')
print()
print()
iterable = chain(primos, numeros, letras)
for e in iterable:
    print(e, end=' ')
print()
print()
# Creación a partir de tuplas:
lenguajes = ('C', 'Go', 'PHP', 'C++')
paises = ('Colombia', 'Perú', 'Chile', 'Grecia', 'China')
ides = ('Visual Studio', 'Eclipse')
iterable = chain(lenguajes, paises, ides)
for e in iterable:
    print(e, end=' ')
print()
iterable = chain(paises, lenguajes, ides)
for e in iterable:
    print(e, end=' ')
print()
# Diferentes argumentos para la función chain():
iterable = chain(primos, lenguajes)
for e in iterable:
    print(e, end=' ')
print()
print()
nombre = 'Sonia'
iterable = chain(lenguajes, primos, nombre)
for e in iterable:
    print(e, end=' ')


# Ejercicio 911: Usar la función accumulate() de itertools para acumular la multiplicación sucesiva de números.
# (1, 3, 5, 7) => 1, 3, 15, 105
from itertools import accumulate
import operator
def multiplicacion_sucesiva(numeros):
    return accumulate(numeros, operator.mul)
resultado = multiplicacion_sucesiva((1, 3, 5, 7))
for r in resultado:
    print(r, end=' ')
print()
print()
resultado = multiplicacion_sucesiva([1, 3, 5, 7])
for r in resultado:
    print(r, end=' ')


# Ejercicio 912: Obtener el mínimo actual desde una colección (iterable) usando la función accumulate().
from itertools import accumulate
# (3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19)
# 3, 2, 1, 1, 0, 0, 0, -1, -1, -1
def minimo_actual(numeros):
    return accumulate(numeros, min)
resultado = minimo_actual((3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19))
for m in resultado:
    print(m, end=' ')
print()
print()
resultado = minimo_actual([3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19])
for m in resultado:
    print(m, end=' ')


# Ejercicio 913: Obtener el máximo actual desde una colección (iterable) usando la función accumulate().
from itertools import accumulate
# running minimum
# running maximum
# (2, 3, 5, 0, 13, 11, 7, 19, 5, 2)
# 2, 3, 5, 5, 13, 13, 13, 19, 19, 19
def maximo_actual(numeros):
    return accumulate(numeros, max)
resultado = maximo_actual((2, 3, 5, 0, 13, 11, 7, 19, 5, 2))
print(type(resultado))
for m in resultado:
    print(m, end=' ')
print()
print()
resultado = maximo_actual([2, 3, 5, 0, 13, 11, 7, 19, 5, 2])
print(type(resultado))
for m in resultado:
    print(m, end=' ')


# Ejercicio 914: Utilizar la función count() de itertools para generar un contador infinito.
from itertools import count
from time import sleep
inicio = 100
salto = 200
contador = count(inicio, salto)
for c in contador:
    print(c)
    if c > 100000:
        break
print('El contador ha finalizado.')
print()
contador = count(inicio, salto)
for c in contador:
    print(c)
    sleep(1)


# Ejercicio 915: Generar un ciclo infinito entre los elementos de un elemento iterable (lista o tupla).
# ['Python', 'C#', 'JavaScript', 'Java']
from itertools import cycle
from time import sleep
ciclo_lenguajes = cycle(['Python', 'C#', 'JavaScript', 'Java'])
for c in ciclo_lenguajes:
    print(c)
    sleep(1)


# Ejercicio 916: Eliminar números negativos de una colección mientras se cumpla una condición.
from itertools import dropwhile
numeros = [-4, -3, -2, -1, 0, 1, -7, 2, 3, 4, 5]
print(numeros)
resultado = list(dropwhile(lambda n: n < 0, numeros))
print(resultado)


# Ejercicio 917: Eliminar números negativos de una colección mientras se cumpla una condición (usar función nombrada).
from itertools import dropwhile
numeros = [-4, -3, -2, -1, 0, 1, -7, 2, 3, 4, 5]
print(numeros)
print()
def eliminar_negativos(n):
    return n < 0
resultado = list(dropwhile(eliminar_negativos, numeros))
print(resultado)


# Ejercicio 918: Eliminar números positivos desde una colección mientras se cumpla un predicado.
from itertools import dropwhile
numeros = [2, 3, 5, 7, -2, 3, 11, 19, -5, -13]
print(numeros)
print()
resultado = list(dropwhile(lambda n: n >= 0, numeros))
print(resultado)


# Ejercicio 919: Usar la función groupby() de itertools para agrupar datos de una colección.
from itertools import groupby
texto = 'AAAAABBCCCDDDEEEEEEEFFGHHHHHIIaaaa'
print(texto)
print()
grupos = groupby(texto)
for k, g in grupos:
    print(f'Llave: {k}')
    print(f'Grupo: {list(g)}')
    print()


# Ejercicio 920: Agrupar datos numéricos con la función groupby() del módulo incorporado itertools.
from itertools import groupby
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 9]
print(numeros)
print()
grupos_numeros = groupby(numeros)
for k, g in grupos_numeros:
    print(f'Llave: {k}')
    print(f'Grupo: {list(g)}')
    print()


# Ejercicio 921: Repetir n cantidad de veces una colección con la función tee() de itertools.
from itertools import tee
numeros = [1, 2, 3, 4, 5]
print(numeros)
print()
resultado = tee(numeros, 5)
for r in resultado:
    print(list(r))


# Ejercicio 922: Repetir n veces una cadena de caracteres como una lista de caracteres con la función tee().
from itertools import tee
lenguaje = 'Python'
print(lenguaje)
print()
resultado = tee(lenguaje, 5)
for r in resultado:
    print(list(r))


# Ejercicio 923: Usar la función permutations() para generar las permutaciones de una lista de letras.
from itertools import permutations
letras = ['A', 'B', 'C', 'D', 'E']
print(letras)
print()
permutaciones = permutations(letras, 3)
contador = 0
for p in permutaciones:
    print(p)
    contador += 1
print()
print(f'Cantidad de permutaciones generadas: {contador}.')
print()
permutaciones = permutations(letras, 5)
contador = 0
for p in permutaciones:
    print(p)
    contador += 1
print()
print(f'Cantidad de permutaciones generadas: {contador}.')


# Ejercicio 924: Usar la función combinations() para generar las combinaciones de una lista de letras.
from itertools import combinations
letras = ['P', 'y', 't', 'h', 'o', 'n']
print(letras)
print()
resultado = combinations(letras, 1)
for c in resultado:
    print(c)
print()
resultado = combinations(letras, 2)
for c in resultado:
    print(c)
print()
resultado = combinations('Python', 2)
for c in resultado:
    print(c)


# Ejercicio 925: Calcular el producto cartesiano de dos listas con la función product() de itertools.
from itertools import product
numeros = [[1, 2], [3, 4]]
# [1, 2] x [3, 4] = [(1, 3), (1, 4), (2, 3), (2, 4)]
print(numeros)
print()
resultado = list(product(*numeros))
print(resultado)
print()
resultado = list(product([], [11, 13]))
print(resultado)


# Ejercicio 926: Generar todas las combinaciones con repeticiones de colores con el módulo itertools.
from itertools import combinations_with_replacement
colores = ['Rojo', 'Verde', 'Azul']
print(colores)
print()
print(list(combinations_with_replacement(colores, 1)))
print()
print(list(combinations_with_replacement(colores, 2)))
print()
print(list(combinations_with_replacement(colores, 3)))


# Ejercicio 927: Generar todas las permutaciones posibles de n cantidad de objetos con la función permutations().
from itertools import permutations
print(list(permutations([1])))
print()
print(list(permutations([1, 2])))
print()
print(list(permutations([1, 2, 3])))


# Ejercicio 928: Crear un iterador a partir de un filtro de selección sobre los elementos de una lista.
# 1. 'Python'
# 2. [1, 0, 1, 0, 0, 1]
# Resultado: Ptn (Lista)
from itertools import compress
iterable = 'Python'
selector = [1, 0, 1, 0, 0, 1]
resultado = list(compress(iterable, selector))
print(resultado)
print()
iterable = ['P', 'y', 't', 'h', 'o', 'n']
resultado = list(compress(iterable, selector))
print(resultado)


# Ejercicio 929: Encadenar objetos iterables (colecciones) con la función chain().
from itertools import chain
cadena = 'Python'
numeros = [1, 2, 3, 4, 5, 6]
print(cadena)
print(numeros)
print()
resultado = list(chain(cadena, numeros))
print(resultado)
print()
reales = (3.1415, 2.7172, 1.4142)
resultado = list(chain(cadena, numeros, reales))
print(resultado)


# Ejercicio 930: Contar los elementos de los grupos identificados por la función groupby() de itertools.
from itertools import groupby
def contar_elementos_grupos(iterable):
    return [(k, len(list(e))) for k, e in groupby(iterable)]
cadena = 'ABBBCCDDDDDDEEFGHHHHHH'
resultado = contar_elementos_grupos(cadena)
print(resultado)


# Ejercicio 931: Crear un iterador con filterfalse() para obtener los elementos que no cumplen un predicado.
from itertools import filterfalse
# (0, 1, 2, ..., 8, 9)
# n % 2 == 0
# (0, 2, ...)
rango = list(range(10))
print(rango)
print()
resultado = list(filterfalse(lambda n: n % 2, rango))
print(resultado)
print()
# Nota: El valor cero (0) es semánticamente equivalente a False
print()
resultado = list(filterfalse(lambda n: n % 2 == 0, rango))
print(resultado)


# Ejercicio 932: Tomar elementos de datos de una colección con la funcion islice() de itertools.
from itertools import islice
letras = 'ABCDEFGHIJKLM'
resultado = list(islice(letras, 2))
print(resultado)
print()
resultado = list(islice(letras, 2, len(letras), 2))
print(resultado)
print()
resultado = list(islice(letras, 2, 8, 2))
print(resultado)
print()
resultado = list(islice(letras, 2, None))
print(resultado)


# Ejercicio 933: Calcular los valores parciales de la serie factorial usando el módulo itertools.
from itertools import accumulate, chain
from operator import mul
def factoriales(n):
    resultado = accumulate(chain([1], range(1, n + 1)), mul)
    return list(resultado)
print(factoriales(5)) # 1, 1, 2, 6, 24, 120
print()
print(factoriales(10))
print()
print(factoriales(50))


# Ejercicio 934: Crear un iterador para recorrer el resultado de aplicar una función sobre una colección de datos.
from itertools import starmap
from math import pow
datos = [(2, 3), (5, 2), (3, 9)]
resultado = list(starmap(pow, datos))
print(resultado)    # 8, 25, 19683


# Ejercicio 935: Usar la función accumulate() de itertools para multiplicar los valores de una lista.
from itertools import accumulate
from operator import mul
primos = [2, 3, 5, 7, 11]
resultado = list(accumulate(primos, mul))
print(resultado) # 2 6 30 210 2310
print()
producto = resultado[-1]
print(producto)
print()
resultado = list(accumulate(primos, mul, initial=100))
print(resultado) # 100 200 600 3000 21000 231000


# Ejercicio 936: Crear un iterador que junte elementos desde dos colecciones hasta donde sea posible.
# C1: ABCD
# C2: XY
# AX, BY, C*, D*
from itertools import zip_longest
resultado = list(zip_longest('ABCD', 'xy', fillvalue='*'))
print(resultado)
print()
resultado = list(zip_longest('xy', 'ABCD', fillvalue='*'))
print(resultado)
print()
resultado = list(zip_longest('xy', 'ABCD', ['M', 'N', 'O'], fillvalue='*'))
print(resultado)


# Ejercicio 937: Encontrar la hora más tarde a partir de 4 dígitos dados en una lista.
from itertools import permutations
def hora_mas_tarde(numeros):
    numeros = [n * -1 for n in numeros]
    numeros.sort()
    resultado = '00:00'
    for h1, h2, m1, m2 in permutations(numeros):
        horas = -(h1 * 10 + h2)
        minutos = -(m1 * 10 + m2)
        if 60 > minutos >= 0 and 24 > horas >= 0:
            resultado = '{:02}:{:02}'.format(horas, minutos)
            break
    return resultado
print(hora_mas_tarde([1, 2, 3, 4])) # 23:41
print()
print(hora_mas_tarde([8, 3, 9, 1])) # 19:38


# Ejercicio 938: Utilizar la función not_() para obtener las personas menores de edad desde una lista.
from operator import not_
class Estudiante:
    def __init__(self, codigo, nombre, carrera, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad
    def __str__(self):
        return f'Código: {self.codigo} - Nombre: {self.nombre}'
estudiantes = [
    Estudiante(1001, 'Angela Burgos', 'Sistemas', 17),
    Estudiante(1002, 'Carlos Tovar', 'Civil', 19),
    Estudiante(1003, 'Fabián Artunduaga', 'Sistemas', 20),
    Estudiante(1004, 'Sonia García', 'Industrial', 16),
]
estudiantes_menores_edad = list(filter(lambda e: not_(e.edad >= 18), estudiantes))
for e in estudiantes_menores_edad:
    print(e)


# Ejercicio 939: Usar la función truth() para validar si un conjunto de datos son equivalentes a True.
from operator import truth
datos = [True, False, 0, 'Cero', '', "", 1, None, """""", '        ']
print(datos)
print()
resultado = list(filter(truth, datos))
for r in resultado:
    print(r)
print()
resultado = list(filter(bool, datos))
for r in resultado:
    print(r)


# Ejercicio 940: Comprobar cuáles objetos de una lista son iguales a otro objeto con la función is_().
from operator import is_
class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
personas = []
personas.append(Persona(1001, 'Mario'))
personas.append(Persona(1002, 'Angela'))
personas.append(personas[0])
personas.append(Persona(1003, 'Fabián'))
personas.append(Persona(1004, 'Andrea'))
personas.append(personas[0])
primera_persona = personas[0]
resultado = list(filter(lambda p: is_(p, primera_persona), personas))
for r in resultado:
    print(r.id, r.nombre)
print()
print('Cantidad de elementos en el resultado:', len(resultado))


# Ejercicio 941: Comprobar cuáles objetos de una lista no son iguales a otro objeto con la función is_not().
from operator import is_not
class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
personas = []
personas.append(Persona(1001, 'Mario'))
personas.append(Persona(1002, 'Angela'))
personas.append(personas[0])
personas.append(Persona(1003, 'Fabián'))
personas.append(Persona(1004, 'Andrea'))
personas.append(personas[0])
primera_persona = personas[0]
resultado = list(filter(lambda p: is_not(p, primera_persona), personas))
for r in resultado:
    print(r.id, r.nombre)
print()
print('Cantidad de elementos en el resultado:', len(resultado))
print()
resultado = list(filter(lambda p: p is not primera_persona, personas))
for r in resultado:
    print(r.id, r.nombre)
print()
print('Cantidad de elementos en el resultado:', len(resultado))


# Ejercicio 942: Calcular la suma del valor absoluto de varios números con la función abs() de operator.
import operator
from itertools import accumulate
# from operator import abs
# from operator import __abs__
numeros = [-3, 5, 7, 2, -11, 13]
print(numeros)
print()
numeros = list(map(operator.abs, numeros))
print(numeros)
print()
suma = list(accumulate(numeros, operator.add))
print(suma) # 41
print()
print(sum(numeros))


# Ejercicio 943: Calcular la suma del precio de varios productos con la función add() de operator.
from operator import add
from itertools import accumulate
class Producto:
    def __init__(self, identificador, nombre, precio):
        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio
productos = []
productos.append(Producto(1001, 'Smartphone', 500))
productos.append(Producto(1002, 'Teclado gamer', 200))
productos.append(Producto(1003, 'Mouse gamer', 120))
productos.append(Producto(1004, 'Monitor 32"', 300))
suma = list(accumulate(list(map(lambda p: p.precio, productos)), add))[-1]
print(suma) # 1120


# Ejercicio 944: Usar la función and_() de operator para la operación de conjunción lógica.
from operator import and_
# and
print(and_(5 > 3, 2 > 0)) # True
print(5 > 3 and 2 > 0) # True
print()
class Computador:
    def __init__(self, identificador, ram, ssd):
        self.id = identificador
        self.ram = ram
        self.ssd = ssd
computadores = []
computadores.append(Computador(1001, 8, 128))
computadores.append(Computador(1002, 16, 256))
computadores.append(Computador(1003, 8, 512))
computadores.append(Computador(1004, 32, 1024))
resultado = list(filter(lambda c: and_(c.ram >= 16, c.ssd >= 128), computadores))
for c in resultado:
    print(c.id, c.ram, c.ssd)


# Ejercicio 945: Calcular la división entera con la función floordiv() del módulo operator.
from operator import floordiv
# floordiv(a, b) ~= a // b ~= __floordiv__(a, b)
print(3 // 2)   # 1
print(floordiv(3, 2))   # 1
print()
numeros_1 = [2, 3, 5, 7, 11]
numeros_2 = [3, 2, 4, 8, 9]
for e in zip(numeros_1, numeros_2):
    print(floordiv(*e))


# Ejercicio 946: Usar la función insert() para insertar un elemento en una posición específica de una lista.
numeros = [1, 2, 4, 5, 7]
print(numeros)
print(len(numeros))
print()
print(help(numeros.insert))
print()
numeros.insert(2, 3)
print(numeros)
print(len(numeros))
print()
numeros.insert(5, 6)
print(numeros)
print(len(numeros))


# Ejercicio 947: Demostrar el uso básico de la función pop() de un objeto de tipo lista.
lenguajes = ['Python', 'JavaScript', 'Go', 'Java', 'C++']
print(lenguajes)
print(len(lenguajes))
print()
# pop([indice])
resultado = lenguajes.pop()
print(resultado)
print(lenguajes)
print(len(lenguajes))
print()
resultado = lenguajes.pop(2)
print(resultado)
print(lenguajes)
print(len(lenguajes))
print()
# resultado = lenguajes.pop(5) # IndexError
# 0, 1, 2, -1, -2, -3


# Ejercicio 948: Llenar una matriz de nxn con valores aleatorios en el rango 1 a 100.
from random import randint
def llenar_matriz(n):
    matriz = []
    for r in range(n):
        fila = []
        for c in range(n):
            fila.append(randint(1, 100))
        matriz.append(fila)
    return matriz
resultado = llenar_matriz(5)
print(resultado)


# Ejercicio 949: Llenar una matriz de nxn con valores aleatorios en el rango 1 a 100 usando una lista de comprensión.
from random import randint
def llenar_matriz(n):
    return [[randint(1, 100) for j in range(n)] for i in range(n)]
resultado = llenar_matriz(5)
print(resultado)


# Ejercicio 950: Usar la función len() para calcular la longitud sobre diferentes datos iterables.
lenguaje = 'Python'
primos = [2, 3, 5, 7]
paises = ('Colombia', 'Perú', 'Boliva')
capitales = {'Colombia': 'Bogotá', 'Argentina': 'Buenos Aires'}
print(len(lenguaje))    # 6
print(len(primos))  # 4
print(len(paises))  # 3
print(len(capitales)) # 2
print()``
# print(len(1000))    # TypeError


# Ejercicio 951: Realizar las diferentes operaciones aritméticas con números complejos.
numero_complejo_1 = 3 + 2j # complex(3, 2)
numero_complejo_2 = 5 - 3j # complex(5, -3)
suma = numero_complejo_1 + numero_complejo_2
resta = numero_complejo_1 - numero_complejo_2
multiplicacion = numero_complejo_1 * numero_complejo_2
division = numero_complejo_1 / numero_complejo_2
print(suma) # (8 - 1j)
print(resta)    # (-2 + 5j)
print(multiplicacion)
print(division)


# Ejercicio 952: Definir una función para validar si al menos un elemento de una colección es verdadero.
def algun_elemento_verdadero(datos):
    for d in datos:
        if d:
            return True
    return False
coleccion = ['123', True, (1, 2), ['John', 'Oliva', 'Juan'], {'a': 1}]
print(algun_elemento_verdadero(coleccion))  # True
print()
coleccion = ['', False, 0, not True, """""", '''''']
print(algun_elemento_verdadero(coleccion))  # False


# Ejercicio 953: Usar la función any() para validar si al menos un elemento de una colección es verdadero.
coleccion = [0, '', '123', True, (1, 2), ['John', 'Oliva', 'Juan'], {'a': 1}]
print(any(coleccion))  # True
print()
coleccion = ['', False, 0, not True, """""", '''''']
print(any(coleccion))  # False


# Ejercicio 954: Agrupar datos similares a través de la función groupby() del módulo itertools.
from itertools import groupby
monedas = ['bitcoin_1', 'billete_1', 'billete_2', 'moneda_10', 'moneda_1000', 'moneda_200', 'bitcoin_3', 'billete_3']
monedas.sort()
print(monedas)
print()
resultado = [list(datos) for _, datos in groupby(monedas, lambda e: e.split('_')[0])]
print(resultado)


# Ejercicio 955: Obtener todas las combinaciones posibles de minúsculas y mayúsculas de un conjunto de caracteres.
from itertools import product
def obtener_combinaciones(caracteres):
    resultado = map(''.join, product(*((c.lower(), c.upper()) for c in caracteres)))
    return list(resultado)
frase = 'abc'
combinaciones = obtener_combinaciones(frase)
print(combinaciones)


# Ejercicio 956: Usar la función islice() de itertools para particionar una lista en un tamaño dado.
from itertools import islice
numeros = list(range(1, 21))
print(numeros)
print()
numeros_iterador = iter(numeros)
resultado = list(iter(lambda: tuple(islice(numeros_iterador, 3)), ()))
print(resultado)
print()
numeros_iterador = iter(numeros)
resultado = list(iter(lambda: tuple(islice(numeros_iterador, 5)), ()))
print(resultado)


# Ejercicio 957: Obtener el índice del primer elemento que sea mayor a un elemento dado usando el módulo itertools.
from itertools import takewhile
def primer_elemento(numeros, numero):
    return len(list(takewhile(lambda c: c[1] <= numero, enumerate(numeros))))
primos = [19, 23, 2, 5, 89, 61, 59, 43, 7, 13]
n = 83
resultado = primer_elemento(primos, n)
print(resultado)    # 4
resultado = primer_elemento(primos, 3)
print(resultado)    # 0


# Ejercicio 958: Usar las funciones chain() y zip_longest() para fusionar listas de diferente tamaño (longitud).
from itertools import chain, zip_longest
primos = [2, 3, 5, 7]
letras = ['A', 'B', 'C']
negativos = [-1, -2]
reales = [3.14, 2.71, 1.41, 0.73, 0.91]
# [2, 'A', -1, 3.14, 3, 'B', -2, 2.71, ...]
resultado = [e for e in chain(*zip_longest(primos, letras, negativos, reales)) if e is not None]
print(resultado)


# Ejercicio 959: Usar la función zip_longest() para sumar los elementos de dos listas índice a índice.
from itertools import zip_longest
primos = [2, 3, 5, 7]
impares = [1, 3, 5, 7, 9, 11]
print('Contenido de la lista primos:', primos)
print('Cantidad de elementos de la lista primos:', len(primos))
print()
print('Contenido de la lista impares:', impares)
print('Cantidad de elementos de la lista impares:', len(impares))
print()
resultado = [x + y for x, y in zip_longest(impares, primos, fillvalue=0)]
print(resultado)


# Ejercicio 960: Usar la función zip_longest() para sumar los elementos de dos listas índice a índice en sentido inverso.
from itertools import zip_longest
primos = [2, 3, 5, 7]
impares = [1, 3, 5, 7, 9, 11]
print('Contenido de la lista primos:', primos)
print('Cantidad de elementos de la lista primos:', len(primos))
print()
print('Contenido de la lista impares:', impares)
print('Cantidad de elementos de la lista impares:', len(impares))
print()
resultado = [x + y for x, y in zip_longest(reversed(impares), reversed(primos), fillvalue=0)]
print(resultado)
print(resultado[::-1])


# Ejercicio 961: Obtener todas las combinaciones de los tres colores primarios con el módulo itertools.
from itertools import combinations
colores = ['rojo', 'verde', 'azul']
print('El contenido de la variable colores es:', colores)
print()
combinaciones = []
for i in range(len(colores) + 1):
    combinaciones.append(list(combinations(colores, i)))
for c in combinaciones:
    print(c)


# Ejercicio 962: Sumar los dígitos de varios números contenidos en una lista usando la función chain() de itertools.
from itertools import chain
numeros = [10, 13, 19]
# Suma dígitos: 1 + 4 + 10 = 15
suma_digitos = sum(int(v) for v in (chain(*[str(n) for n in numeros])))
print(suma_digitos) # 15


# Ejercicio 963: Obtener los valores del producto mínimo y máximo de un conjunto de datos numéricos.
from itertools import combinations
def valores_min_max_producto(numeros):
    minimo = min(combinations(numeros, 2), key=lambda s: s[0] * s[1])
    maximo = max(combinations(numeros, 2), key=lambda s: s[0] * s[1])
    return minimo, maximo
numeros = [2, 3, 5, 11, 19, 17, 2, 3, 7]
# minimo = (2, 2)
# maximo = (11, 17)
resultado = valores_min_max_producto(numeros)
print(resultado)


# Ejercicio 964: Recorrer los grupos de datos identificados con la función groupby() de itertools.
from itertools import groupby
letras = ['B', 'A', 'C', 'A', 'A', 'B', 'D', 'C', 'B', 'B', 'B', 'B']
print(letras)
letras.sort()
print(letras)
print()
grupos_letras = groupby(letras)
print(grupos_letras)
print()
for g, d in grupos_letras:
    datos = list(d)
    print(g, '-->', datos, f'({len(datos)})')


# Ejercicio 965: Definir una función personalizada para calcular la suma de dos matrices.
def calcular_suma_matrices(A, B):
    if len(A) != len(B):
        raise Exception('Las dos matrices deben tener la misma cantidad de filas.')
    if len(A[0]) != len(B[0]):
        raise Exception('Las dos matrices deben tener la misma cantidad de columnas.')
    suma_matrices = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        suma_matrices.append(fila)
    return suma_matrices
A = [[1, 2, 3], [4, 5, 6]] # 2x3
B = [[2, 3, 5], [11, 7, 5]] # 2x3
resultado = calcular_suma_matrices(A, B)
print(resultado) # [[3, 5, 8], [15, 12, 11]]
print()
C = [[2, 3], [5, 7], [11, 13]]
try:
    resultado = calcular_suma_matrices(A, C)
    print(resultado)
except Exception as e:
    print(e)


# Ejercicio 966: Obtener la frecuencia de los elementos de los grupos identificados con groupby().
from itertools import groupby
def conteo_frecuencia(datos):
    resultado = [sum(1 for c in d) for _, d in groupby(datos)]
    return resultado
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(conteo_frecuencia(numeros)) # [1, 2, 3, 4, 5]
print()
numeros = [1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5]
print(conteo_frecuencia(numeros)) # [1, 2, 1, 4, 3]


# Ejercicio 967: Generar una lista con los valores intercalados procedentes de diferentes listas.
from itertools import chain
def elementos_intercalados(*datos):
    resultado = list(chain(*zip(*datos)))
    return resultado
numeros_1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
numeros_2 = [100, 200, 300, 400, 500]
numeros_3 = [10, 20, 30]
# [1000, 100, 10, 2000, 200, 20, 3000, 300, 30]
resultado = elementos_intercalados(numeros_1, numeros_2, numeros_3)
print(resultado)


# Ejercicio 968: Generar las combinaciones únicas a partir de un listado con diferentes colores.
from itertools import combinations
def combinacion_colores_unicos(colores, n):
    resultado = [' y '.join(c) for c in combinations(colores, r=n)]
    return resultado
datos = ['Rojo', 'Verde', 'Azul']
resultado = combinacion_colores_unicos(datos, 2)
print(resultado) # ['Rojo y Verde', 'Rojo y Azul', 'Verde y Azul']
print()
resultado = combinacion_colores_unicos(datos, 3)
print(resultado) # ['Rojo y Verde y Azul']


# Ejercicio 969: Obtener la mayor longitud de los grupos identificados por la función groupby().
from itertools import groupby
def mayor_longitud_grupo(texto):
    resultado = max(len(list(d)) for _, d in groupby(texto))
    return resultado
contenido = 'AAABBCCCCCDDD'
print(mayor_longitud_grupo(contenido))  # 5


# Ejercicio 970: Definir una función para validar si una matriz dada es identidad.
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
def es_matriz_identidad(matriz):
    if not isinstance(matriz, list):
        raise TypeError('El argumento debe ser una lista.')
    if len(matriz) != len(matriz[0]):
        raise Exception('La matriz debe ser cuadrada.')
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True
datos = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
print(es_matriz_identidad(datos))   # True
print()
datos[0][2] = 20
print(es_matriz_identidad(datos))   # False


# Ejercicio 971: Eliminar los valores que se hallen las posiciones pares de una lista.
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letras)
# [B, D, F, H, J]
print()
letras = [letras[i] for i in range(len(letras)) if i % 2 == 1]
print(letras)


# Ejercicio 972: Eliminar los valores que se hallen en las posiciones impares de una lista.
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letras)
print()
letras = [letras[i] for i in range(len(letras)) if i % 2 == 0]
print(letras) # ['A', 'C', 'E', 'G', 'I']


# Ejercicio 973: A partir de 4 dígitos dados en una lista generar la última hora en formato 24 horas.
from itertools import permutations
def ultima_hora(digitos):
    if not isinstance(digitos, list):
        raise TypeError('El argumento debe ser una lista.')
    if len(digitos) != 4:
        raise Exception('La lista debe contener cuatro elementos.')
    if not all([isinstance(e, int) for e in digitos]):
        raise TypeError('El argumento debe ser una lista con valores enteros.')
    if not all([d >= 0 for d in digitos]):
        raise Exception('Todos los elementos de la lista deben ser mayores o iguales 0.')
    digitos = [-d for d in digitos]
    digitos.sort()
    for h1, h2, m1, m2 in permutations(digitos):
        horas = -(10*h1 + h2)
        minutos = -(10*m1 + m2)
        if 60 > minutos >= 0 and 24 > horas >= 0:
            return '{:02}:{:02}'.format(horas, minutos)
    return None
print(ultima_hora([1, 3, 2, 7])) # 23:17
print(ultima_hora([5, 1, 2, 7])) # 17:51


# Ejercicio 974: Generar los valores parciales de la serie factorial usando chain() y accumulate().
# 5! => [1, 1, 2, 6, 24, 120] <
# 7! => [1, 1, 2, 6, 24, 120, 720, 5040]
from itertools import accumulate, chain
from operator import mul
def valores_parciales_factorial(n):
    if not isinstance(n, int):
        raise TypeError('El argumento debe ser un número entero.')
    if n < 0:
        raise Exception('El argumento debe ser un número entero positivo (>=0).')
    resultado = list(accumulate(chain([1], range(1, n + 1)), mul))
    return resultado
print(valores_parciales_factorial(5)) # [1, 1, 2, 6, 24, 120]
print(valores_parciales_factorial(7)) # [1, 1, 2, 6, 24, 120, 720, 5040]
print(valores_parciales_factorial(11)) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, ...]


# Ejercicio 975: Iterar una lista en sentido inverso con el ciclo for y usando la función range().
numeros = list(range(1, 11))
print(numeros)
print()
for i in range(len(numeros)):
    print(numeros[i], end=' ')
print()
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i], end=' ')


# Ejercicio 976: Iterar las posiciones pares de una lista en un ciclo for y while.
numeros = list(range(1, 11))
print(numeros)
print()
print('Iteración posiciones pares de la lista `numeros` utilizando un ciclo for:')
for i in range(0, len(numeros), 2):
    print(numeros[i], end=' ')
print()
print()
print('Iteración posiciones pares de la lista `numeros` utilizando un ciclo while:')
i = 0
while i < len(numeros):
    print(numeros[i], end=' ')
    i += 2


# Ejercicio 977: Iterar las posiciones impares de una lista en un ciclo for y while.
numeros = list(range(1, 11))
print(numeros)
print()
# [2, 4, 6, 8, 10]
print('Iteración con ciclo for:')
for i in range(1, len(numeros), 2):
    print(numeros[i], end=' ')
print()
print()
print('Iteración con ciclo while:')
i = 1
while i < len(numeros):
    print(numeros[i], end=' ')
    i += 2


# Ejercicio 978: Crear una copia completa de una lista con notación de slicing y la función copy().
letras = list('PYTHON')
print(letras) # ['P', 'Y', 'T', 'H', 'O', 'N']
print()
print('ID de la lista letras:', id(letras))
print()
letras_2 = letras[:]
print(letras_2)
print(id(letras_2))
print()
letras_3 = letras.copy()
print(letras_3)
print(id(letras_3))


# Ejercicio 979: Usar la función product() de itertools para calcular el producto de cartesiano de dos listas.
from itertools import product
numeros = [[1, 2], [3, 4]]
print(numeros)
print()
# => [(1, 3), (1, 4), (2, 3), (2, 4)]
resultado = list(product(*numeros))
print(resultado)


# Ejercicio 980: Definir una función personalizada para calcular el producto cartesiano de dos listas.
def producto_cartesiano(datos):
    lista_1 = datos[0]
    lista_2 = datos[1]
    resultado = []
    for d in lista_1:
        for e in lista_2:
            resultado.append((d, e))
    return resultado
datos = [[1, 2], [3, 4]]
print(producto_cartesiano(datos)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print()
datos = [[1, 2, 3], [4, 5, 6]]
print(producto_cartesiano(datos)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# Ejercicio 981: Calcular el producto cartesiano usando una lista de comprensión.
def producto_cartesiano(datos):
    return [(d, e) for d in datos[0] for e in datos[1]]
datos = [[1, 2], [3, 4]]
print(producto_cartesiano(datos)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print()
datos = [[1, 2, 3], [4, 5, 6]]
print(producto_cartesiano(datos)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# Ejercicio 982: Calcular la suma de cada una de las filas de una matriz.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# [6, 15, 24]
suma_filas = []
for f in matriz:
    suma_filas.append(sum(f))
print(suma_filas) # # [6, 15, 24]


# Ejercicio 983: Calcular la suma de cada una de las columnas de una matriz.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma = []
# [12, 15, 18]
for j in range(len(matriz[0])):
    suma_columna = 0
    for i in range(len(matriz)):
        suma_columna += matriz[i][j]
    suma.append(suma_columna)
print(suma)


# Ejercicio 984: Calcular el cuadrado, el cubo, y la raíz cuadrada para un rango de números.
from math import sqrt
while True:
    try:
        limite_inferior = int(input('Digite el valor para el límite inferior del rango: '))
        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    print()
print()
while True:
    try:
        limite_superior = int(input('Digite el valor para el límite superior del rango: '))
        if limite_superior <= limite_inferior:
            print('ADVERTENCIA: El límite superior debe ser mayor al límite inferior.')
            print()
            continue
        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    print()
print()
numeros = list(range(limite_inferior, limite_superior + 1))
for n in numeros:
    print(n**2, n**3, round(sqrt(n), 2))


# Ejercicio 985: Usar cadenas de formato para mejorar la presentación de datos del ejercicio no. 984.
from math import sqrt
while True:
    try:
        limite_inferior = int(input('Digite el valor para el límite inferior del rango: '))
        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    print()
print()
while True:
    try:
        limite_superior = int(input('Digite el valor para el límite superior del rango: '))
        if limite_superior <= limite_inferior:
            print('ADVERTENCIA: El límite superior debe ser mayor al límite inferior.')
            print()
            continue
        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    print()
print()
numeros = list(range(limite_inferior, limite_superior + 1))
print('{:>4}{:>12}{:>12}{:>12}'.format('n', 'Cuadrado', 'Cubo', 'Raíz'))
for n in numeros:
    print('{:4d}{:10d}{:12d}{:>15}'.format(n, n**2, n**3, round(sqrt(n), 2)))


# Ejercicio 986: Definir una función para encontrar el menor y el mayor entre un grupo de datos numéricos.
def encontrar_minimo_maximo(numeros):
    if not isinstance(numeros, (list, tuple)):
        raise TypeError('El argumento debe ser una lista o una tupla.')
    if len(numeros) == 0:
        return None
    minimo = numeros[0]
    maximo = numeros[0]
    for n in numeros:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    return minimo, maximo
primos = [13, 11, 2, 19, 5, 7, 23]
resultado = encontrar_minimo_maximo(primos)
print(resultado) # (2, 23)


# Ejercicio 987: Obtener las ternas en el rango 1 a 1000 que forman triángulos rectángulos.
# cateto adyacente (a)
# cateto opuesto (b)
# hipotenusa (c)
# a ^ 2 + b ^ 2 = c ^ 2
ternas = []
for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a**2 + b**2 == c**2:
                ternas.append((a, b, c))
print('Cantidad de ternas:', len(ternas))
for t in ternas:
    print(t)


# Ejercicio 988: Calcular el valor de la constante e (número de Euler) con la suma de serie infinita.
from math import factorial
import math
limite = 100
e = 0
for n in range(100):
    e += 1/factorial(n)
print('Constante de Euler (e):', e)
print('Constante de Euler (e):', math.e)


# Ejercicio 989: Definir una función para calcular el seno de un ángulo dado usando una serie infinita.
import math
x = math.pi / 2
seno = 0
for n in range(0, 50):
    seno += math.pow(-1, n) / math.factorial(2 * n + 1) * math.pow(x, 2*n + 1)
print('El seno de pi/2 es igual a:', seno)
print('El seno de pi/2 es igual a:', math.sin(x))


# Ejercicio 990: Definir una función para calcular el coseno de un ángulo usando una serie infinita.
from math import cos, factorial, pi, pow
x = pi / 2
coseno = 0
for k in range(0, 50):
    coseno += pow(-1, k)*pow(x, 2 * k) / factorial(2*k)
print('Coseno de pi/2 calculado con una serie infinita:', coseno)
print('Coseno de pi/2 calculado la función cos():', cos(x))


# Ejercicio 991: Calcular la tangente de un ángulo usando las series infinitas del seno y el coseno.
import math
x = math.pi / 4
seno = 0
for n in range(0, 50):
    seno += math.pow(-1, n) / math.factorial(2 * n + 1) * math.pow(x, 2*n + 1)
coseno = 0
for k in range(0, 50):
    coseno += math.pow(-1, k)*math.pow(x, 2 * k) / math.factorial(2*k)
tangente = seno / coseno
print('El coseno calculado a partir de las series infinitas del seno y el coseno:', tangente)
print('El coseno calculado a partir de la función math.tan():', math.tan(x))


# Ejercicio 992: Definir la función exponencial a partir de una serie infinita de Taylor.
import math
def funcion_exponencial(x):
    suma = 0
    for n in range(0, 50):
        suma += math.pow(x, n) / math.factorial(n)
    return suma
print('Resultado con la función funcion_exponencial:', funcion_exponencial(2))
print('Resultado con la función math.exp:', math.exp(2))


# Ejercicio 993: Sucesión de valores de la forma 0, 1, 1, 2, 4, 7, 13, 24, ... según N términos.
# 0, 1, 1
# 0, 1, 1, 2
# 0, 1, 1, 2, 4, ...
def sucesion_valores(n):
    sucesion = [0, 1, 1]
    for i in range(n):
        sucesion.append(sum(sucesion[-3:]))
    return ','.join(str(e) for e in sucesion)
print(sucesion_valores(10)) # 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504


# Ejercicio 995: Agregar una cantidad de segundos específica a un objeto de tipo datetime.
from datetime import datetime, timedelta
fecha_hora_actual = datetime.now()
print(fecha_hora_actual)
print()
nueva_fecha_hora = fecha_hora_actual + timedelta(0, 30)
print(nueva_fecha_hora)


# Ejercicio 996: Agregar una cantidad específica de días a un objeto de tipo datetime con timedelta.
from datetime import datetime, timedelta
fecha_hora_actual = datetime.now()
print(fecha_hora_actual)
print()
dias = 100
nueva_fecha_hora = fecha_hora_actual + timedelta(dias, 0)
print(nueva_fecha_hora)


# Ejercicio 997: Restar una cantidad de segundos específica a una fecha con un objeto timedelta.
from datetime import datetime, timedelta
fecha_hora_actual = datetime.now()
print(fecha_hora_actual)
print()
otra_fecha_hora = fecha_hora_actual - timedelta(0, 30)
print(otra_fecha_hora)


# Ejercicio 998: Restar una cantidad específica de días a un objeto de tipo datetime con timedelta.
from datetime import datetime, timedelta
fecha_hora_actual = datetime.now()
print(fecha_hora_actual)
print()
dias = 200
otra_fecha_hora = fecha_hora_actual - timedelta(dias, 0)
print(otra_fecha_hora)


# Ejercicio 999: Ordenar una lista de cadenas de caracteres según su longitud con la función sorted().
lenguajes = ['C#', 'Java', 'JavaScript', 'Python', 'PHP', 'Go', 'Kotlin']
print(lenguajes)
print()
# A-Z
lenguajes_ordenados = sorted(lenguajes)
print(lenguajes_ordenados)
print()
# Menor a mayor longitud (ascendente):
lenguajes_ordenados = sorted(lenguajes, key=len)
print(lenguajes_ordenados)
print()
# Mayor a menor longitud (descendente):
lenguajes_ordenados = sorted(lenguajes, key=len, reverse=True)
print(lenguajes_ordenados)
