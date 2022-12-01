# BLOQUE DE DEFINICIONES
# IMPORTACION DE FUNCIONES
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
# DEFINICION DE FUNCIONES

def calcular_tiempo_transcurrido(inicio, termino):
    '''
    Función que calcula el tiempo transcurrido entre un intervalo dado
    de elementos datetime
    Entrada: Dos objetos datetime
    Salida: Tiempo transcurrido en microsegundos
    '''
    return (termino - inicio).total_seconds() * 1000000

def lectura_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def calculo_dias_iterativo(a,b,c):
    dias = 0
    distancia = 0
    if c == 0:
        return 0
    elif b >= a:
        return -1
    else:
        while distancia < c:
            distancia = distancia + a
            dias = dias + 3
            if distancia < c:
                distancia = distancia - b
                dias = dias + 1
        return dias

def calculo_dias_recursivo(a,b,c,dias):
    if c == 0:
        return 0
    elif b >= a:
        return -1
    elif c > 0:
        c = c - a
        dias = dias + 3
        if c <= 0:
            return dias
        else:
            calculo_dias_recursivo(a,b,c+b,dias+1)

def escritura_archivo(nombre_archivo, lineas):
    archivo = open(nombre_archivo, "w")
    for linea in lineas:
        archivo.write(linea)
    archivo.close()
    return True
    

# DEFINICION DE CONSTANTES

# BLOQUE PRINCIPAL
# ENTRADA
lineas_archivo = lectura_archivo("entrada.txt")
lineas_archivo_salida = []
i = 0
tiempos_iterativos = []
tiempos_recursivos = []
lista_viajes = []
viajes_ordenados = []


while len(lineas_archivo) != len(lineas_archivo_salida):
    fila_actual = lineas_archivo[i]
    fila_actual = fila_actual.strip().split()
    j = 0
    while j < len(fila_actual):
        fila_actual[j] = int(fila_actual[j])
        j += 1
    a = fila_actual[0]
    b = fila_actual[1]
    c = fila_actual[2]
    numero = 0
    while numero < 2:
        if numero == 0:
            inicio = datetime.now()
            numero_dias = calculo_dias_iterativo(a,b,c)
            termino = datetime.now()
            tiempo = calcular_tiempo_transcurrido(inicio,termino)
            tiempos_iterativos.append(tiempo)
            fila_actual.append(numero_dias)
            fila_actual.append(tiempo)
            numero += 1
        elif numero == 1:
            numero_dias = 0
            inicio = datetime.now()
            numero_dias = calculo_dias_recursivo(a,b,c,numero_dias)
            termino = datetime.now()
            tiempos_recursivos.append(tiempo)
            fila_actual.append(tiempo)
            numero += 1
            
    cadena = ""
    k = 0
    while k < len(fila_actual):
        fila_actual[k] = str(fila_actual[k])
        if k == (len(fila_actual)-1):
            cadena = cadena + fila_actual[k] + "\n"
        else:
            cadena = cadena + fila_actual[k] + " "
        k += 1
    
    lineas_archivo_salida.append(cadena)
    lista_viajes.append("Viaje N°" + str(i+1))
    i += 1
tiempos_totales = []
b = 0
copia_tiempos = []
while b < len(tiempos_iterativos):
    tiempos = tiempos_iterativos[b] + tiempos_recursivos[b]
    tiempos_totales.append(tiempos)
    copia_tiempos.append(tiempos)
    b += 1

p = 0
print(tiempos_totales)
while p < len(lista_viajes):
    if tiempos_totales[p] == 0.0:
        viajes_ordenados.append(lista_viajes[p])
    p += 1

tiempos_ordenados_iterativos = []
largo_iterativos = len(tiempos_iterativos)
while len(tiempos_ordenados_iterativos) != largo_iterativos:
    u = 0
    minimo = tiempos_iterativos[u]
    while u < len(tiempos_iterativos):
        if tiempos_iterativos[u] < minimo:
            minimo = tiempos_iterativos[u]
        u += 1
    tiempos_iterativos.remove(minimo)
    tiempos_ordenados_iterativos.append(minimo)
print(tiempos_ordenados_iterativos)

tiempos_ordenados_recursivos = []
largo_recursivos = len(tiempos_recursivos)
while len(tiempos_ordenados_recursivos) != largo_recursivos:
    x = 0
    minimo = tiempos_recursivos[x]
    while x < len(tiempos_recursivos):
        if tiempos_recursivos[x] < minimo:
            minimo = tiempos_recursivos[u]
        x += 1
    tiempos_recursivos.remove(minimo)
    tiempos_ordenados_recursivos.append(minimo)
print(tiempos_ordenados_recursivos)

tiempos_ordenados_totales = []
largos_totales = len(tiempos_totales)
while len(tiempos_ordenados_totales) != largos_totales:
    r = 0
    minimo = tiempos_totales[r]
    while r < len(tiempos_totales):
        if tiempos_totales[r] < minimo:
            minimo = tiempos_totales[r]
        r += 1
    if minimo != 0.0:
        posicion = copia_total.index(minimo)
        viajes_ordenados.append(lista_viajes[posicion])
    tiempos_totales.remove(minimo)
    tiempos_ordenados_totales.append(minimo)
print(tiempos_ordenados_totales)

# SALIDA
escritura_archivo("salida_pep.txt", lineas_archivo_salida)
grafico = plt.plot(viajes_ordenados, tiempos_ordenados_iterativos)

plt.setp(grafico, "color", "r", "marker", "o", label = "Funcion iterativa")

grafico2 = plt.plot(viajes_ordenados, tiempos_ordenados_recursivos)
plt.setp(grafico2, "color", "g", "linestyle", "--", label = "Funcion recursiva")
plt.legend()
plt.xlabel("Viajes")
plt.ylabel("Tiempo [ms]")
plt.show()
