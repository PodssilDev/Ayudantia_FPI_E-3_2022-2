# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE: John Serrano Carrasco
# RUT:
# CARRERA: Ingeniería Civil Informática
# DESCRIPCIÓN DEL PROGRAMA: El programa recibe como entrada
# la lectura de un archivo de texto llamado "entrada.txt"
# el cual contiene los datos de a, que corresponde a
# cuantas millas nauticas avanza por 3 dias, b, que
# corresponde a cuantas millas nauticas retrocede por 1 dia
# y c, que corresponde al destino. El programa calcula los dias
# totales tanto de forma iterativa como recursiva, calcula
# el tiempo para cada funcion y junto a los dias deja la
# informacion en un archivo de texto llamado "salida.txt".
# Si nunca se llega al destino, se colocará un -1 como el total
# de dias.
# El programa también grafica los tiempos iterativos y recursivos,
# donde el eje X corresponde a los viajes de barco ordenados
# de menor a mayor y en el eje Y estan los tiempos de funciones.

# BLOQUE DE DEFINICION
# IMPORTACIONES
# Se importa datetime del módulo datetime
from datetime import datetime
# Se importa matplotlib.pyplot con el alias plt
import matplotlib.pyplot as plt
# CONSTANTES
# En este programa no hay constantes.
# DEFINICION DE FUNCIONES


def calcular_tiempo_transcurrido(inicio, termino):
    '''
    Función que calcula el tiempo transcurrido entre un intervalo dado
    de elementos datetime
    Entrada: Dos objetos datetime
    Salida: Tiempo transcurrido en microsegundos (float)
    '''
    return (termino - inicio).total_seconds() * 1000000


def lectura_archivo(nombre):
    '''
    Función que lee el archivo de texto y crea una lista que contiene
    las lineas del archivo en formato string
    Entrada: Nombre del archivo (str)
    Salida: Lista cuyos elementos son las lineas del archivo (list)
    '''
    # Se abre el archivo utilizando open y en modo lectura "r"
    archivo = open(nombre, "r")
    # Se guarda en lineas_archivo una lista con las lineas del
    # archivo
    lineas_archivo = archivo.readlines()
    # Se cierra el archivo de texto
    archivo.close()
    # Se retorna la variable lineas_archivo
    return lineas_archivo


def calculo_dias(a, b, c):
    '''
    Funcion que calcula los dias de forma iterativa
    Entrada: Los valores de a, b y c (int)
    Salida: Los dias totales que tomo en llegar al destino (int)
    '''
    # Declaro la variable dias = 0, para contar los dias totales
    dias = 0
    # Declaro la variable distancia = 0, para utilizar en el calculo
    # de los dias totales
    distancia = 0
    # Si el valor de c equivale a 0
    if c == 0:
        # Entonces la funcion inmediatamente devuelve 0
        return 0
    # Si el valor de b es mayor o igual al valor de a
    elif b >= a:
        # Entonces la funcion devuelve -1, ya que nunca llegará
        # al destino
        return -1
    # Si no pasa ninguna de las dos condiciones anteriores
    else:
        # Mientras el valor de distancia sea menor al valor de c
        while distancia < c:
            # A distancia se le suma el valor de a
            distancia = distancia + a
            # A dias se le suma 3
            dias = dias + 3
            # Si aun se cumple que la distancia sigue siendo menor que c
            if distancia < c:
                # Entonces a distancia se le resta el valor de b
                distancia = distancia - b
                # A dias se le suma 1
                dias = dias + 1
        # Una vez que la distancia es mayor o igual a C, la funcion
        # devuelve la cantidad de dias.
        return dias


def dias_recursivo(a, b, c, dia):
    '''
    Funcion que calcula los dias de forma recursiva
    Entrada: Los valores de a, b, c y el valor de dia
    el cual siempre será inicialmente 0(int)
    Salida: Los dias totales que tomo en llegar al destino (int)
    '''
    # Si el valor de c es igual a 0
    if c == 0:
        # Entonces la funcion inmediatamente devuelve 0
        return 0
    # Si el valor de b mayor o igual al valor de a
    elif b >= a:
        # Entonces la funcion devuelve -1, ya que nunca llegará
        # al destino
        return -1
    # Pero si el valor de c sigue siendo positivo
    elif c > 0:
        # Entonces a c se le resta el valor de a
        c = c - a
        # A dias se le suma 3
        dia = dia + 3
        # Si luego de eso, c es negativo o igual a 0
        if c <= 0:
            # Se devuelve la cantidad de dias
            return dia
        # Si c sigue siendo positivo
        else:
            # Se vuelve a llamar a la funcion, donde ahora a dias se le
            # suma 1 y a c se le suma el valor de b (Recursion)
            return dias_recursivo(a, b, c+b, dia+1)


def escritura_archivo(archivo, lineas):
    '''
    Funcion que crea y escribe un archivo de texto nuevo
    Entrada: Nombre del archivo a escribir y las lineas a
    escribir (str y list)
    Salida: Escritura del archivo de texto (file)
    '''
    # Se abre el archivo en modo escritura "W"
    archivo = open(archivo, "w")
    # Se recorren las lineas del archivo
    for linea in lineas:
        # Se escribe cada linea en el archivo
        archivo.write(linea)
    # Se cierra el archivo de texto
    archivo.close()

# BLOQUE PRINCIPAL
# ENTRADA
# El programa recibe como entrada la lectura del archivo
lineas_archivo = lectura_archivo("entrada.txt")
# PROCESAMIENTO
# Se crea una lista vacia lineas_nuevo_archivo donde iran
# las lineas que se escribiran en el archivo salida.txt
lineas_nuevo_archivo = []
# Se crea un contador i = 0 para iterar
i = 0
# Se crea una lista vacia tiempos_iterativa donde se
# guardaran los tiempos de la funcion iterativa
tiempos_iterativa = []
# Se crea una lista vacia tiempos_recursion donde se
# guardaran los tiempos de la funcion recursiva
tiempos_recursion = []
# Se crea una lista lista_viajes donde se guardara
# un string que contiene "Viaje N°" junto con el
# numero de viaje, el cual depende de la linea del
# archivo de texto entrada.txt
lista_viajes = []
# Se crea una lista viajes_ordenados donde se ordenaran
# los elementos de lista_viajes de acuerdo al tiempo
# que obtuvieron los barcos.
viajes_ordenados = []
# Mientras el largo de la lista del archivo de entrada
# sea distinto al largo de la lista del archivo de salida
while len(lineas_archivo) != len(lineas_nuevo_archivo):
    # Se guarda en fila_actual la linea actual a analizar
    fila_actual = lineas_archivo[i]
    # Se utiliza un strip() para eliminar los saltos de linea
    fila_actual = fila_actual.strip()
    # Utilizamos un split() para trabajar con una lista
    fila_actual = fila_actual.split()
    # Se crea un contador j = 0 para iterar
    j = 0
    # Mientras j sea menor al largo de la lista de fila_actual
    while j < len(fila_actual):
        # Se transforma cada elemento de la lista a int
        fila_actual[j] = int(fila_actual[j])
        # Se aumenta el contador para poder seguir iterando
        j += 1
    # Se guarda en a el primer valor de fila_actual
    a = fila_actual[0]
    # Se guarda en b el segundo valor de fila_actual
    b = fila_actual[1]
    # Se guarda en c el segundo valor de fila_actual
    c = fila_actual[2]
    # Se crea una variable num = 0, esto nos ayudará para
    # el calculo del tiempo de cada funcion
    num = 0
    # Mientras num sea menor a 2
    while num < 2:
        # Si num equivale a 0
        if num == 0:
            # Se inicia el calculo del tiempo
            inicio = datetime.now()
            # Se llama a la funcion calculo_dias y se guarda
            # lo que devuelve en numero_dias
            numero_dias = calculo_dias(a, b, c)
            # Se termina el calculo del tiempo
            termino = datetime.now()
            # Se calcula el tiempo de la funcion iterativa
            tiempo = calcular_tiempo_transcurrido(inicio, termino)
            # Se agrega el tiempo a la lista tiempos_iterativa
            tiempos_iterativa.append(tiempo)
            # Se agrega a fila_actual el numero de dias
            fila_actual.append(numero_dias)
            # Se agrega a fila_actual el tiempo iterativo
            fila_actual.append(tiempo)
            # Se aumenta num en 1 para seguir con el ciclo while
            num = num + 1
        # Si num es igual a 1
        elif num == 1:
            # Se declara numero_dias = 0 para usarlo en la
            # funcion recursiva
            numero_dias = 0
            # Se inicia el calculo del tiempo
            inicio = datetime.now()
            # Se llama a la funcion dias_recursivo y se guarda el
            # resultado en numero_dias
            numero_dias = dias_recursivo(a, b, c, numero_dias)
            # Se termina el calculo del tiempo
            termino = datetime.now()
            # Se calcula el tiempo que se demoro la funcion recursiva
            tiempo = calcular_tiempo_transcurrido(inicio, termino)
            # Se agrega el tiempo a la lista tiempos_recursion
            tiempos_recursion.append(tiempo)
            # Se agrega a fila_actual el tiempo de la funcion recursiva
            fila_actual.append(tiempo)
            # Se aumenta num en 1 para salir del ciclo while
            num = num + 1
    # Se crea un string vacio para la escritura del archivo de texto
    cadena = ""
    # Se declara k = 0 para iterar
    k = 0
    # Mientras k sea menor a la lista fila_actual
    while k < len(fila_actual):
        # Se transforman los elementos de fila_actual a string
        fila_actual[k] = str(fila_actual[k])
        # Si el elemento a analizar es el ultimo de fila_actual
        if k == (len(fila_actual) - 1):
            # Se agrega al string cadena junto con un salto de linea
            cadena = cadena + fila_actual[k] + "\n"
        # Si el elemento a analizar no es el ultimo
        else:
            # Se agrega el string a cadena junto con un string vacio
            cadena = cadena + fila_actual[k] + " "
        # Se aumenta el contador para continuar iterando
        k += 1
    # Se agrega el string cadena a la lista lineas_nuevo_archivo
    lineas_nuevo_archivo.append(cadena)
    # Se agrega a la lista un string que contiene "Viaje N°" mas
    # un número
    lista_viajes.append("Viaje N°" + str(i+1))
    # Se aumenta el contador para continuar iterando
    i += 1
# Se crea la lista de tiempos_totales, donde se guardará la suma
# de los tiempos iterativos y de recursion de cada viaje
tiempos_totales = []
# Se crea un contador b = 0 para poder iterar
b = 0
# Se crea una lista vacia copia_total donde se guardará
# exactamente el mismo contenido de tiempos_totales
copia_total = []
# Mientras b sea menor al largo de la lista tiempos_iterativa
while b < len(tiempos_iterativa):
    # Se guarda en tiempo la suma del tiempo iterativo con
    # el tiempo de recursion
    tiempo = tiempos_iterativa[b] + tiempos_recursion[b]
    # Se agrega el resultado a tiempos_totales
    tiempos_totales.append(tiempo)
    # Se agrega el mismo resultado a copia_total
    copia_total.append(tiempo)
    # Se aumenta el contador para poder continuar iterando
    b += 1

# Se crea el contador p para poder iterar
p = 0
# Mienteas p sea menor al largo de lista_viajes
while p < len(lista_viajes):
    # Si el elemento actual de tiempos_totales es 0.0
    if tiempos_totales[p] == 0.0:
        # Entonces se agrega el elemento de lista_viajes
        # que tiene la misma posicion a la lista viajes_ordenados
        viajes_ordenados.append(lista_viajes[p])
    # Se aumenta el contador en 1 para continuar iterando
    p += 1

# Se crea la lista ordenada_iterativa donde se guardaran los tiempos
# iterativos de forma creciente
ordenada_iterativa = []
# Se guarda en la variable largo el largo de la lista tiempos_iterativa
largo = len(tiempos_iterativa)
# Mientras el largo de ordenada_iterativa sea distinto al valor de largo
while len(ordenada_iterativa) != largo:
    # Se declara el contador u = 0 para poder iterar
    u = 0
    # Se guarda en minimo el primer elemento de la lista
    minimo = tiempos_iterativa[u]
    # Mientras u sea menor al largo de tiempos_iterativa
    while u < len(tiempos_iterativa):
        # Si el elemento actual es menor al minimo
        if tiempos_iterativa[u] < minimo:
            # Entonces se declara a minimo como el elemento actual
            minimo = tiempos_iterativa[u]
        # Se aumenta i en 1 para continuar iterando
        u += 1
    # Se elimina el minimo de la lista tiempos_iterativa
    tiempos_iterativa.remove(minimo)
    # Se agrega el minimo a la lista ordenada_iterativa
    ordenada_iterativa.append(minimo)

# Se crea la lista ordenada_recursiva donde se guardaran
# los tiempos recursivos de forma creciente
ordenada_recursiva = []
# Mientras el largo de ordenada_recursiva sea distinto al valor
# de la variable largo
while len(ordenada_recursiva) != largo:
    # Se declara x = 0 para poder iterar
    x = 0
    # Se declara al minimo como el primer elemento de la lista
    minimo = tiempos_recursion[x]
    # Mientras x sea menor al largo de tiempos_recursion
    while x < len(tiempos_recursion):
        # Si el elemento actual es menor al minimo
        if tiempos_recursion[x] < minimo:
            # Entonces el minimo se declara como el elemento actual
            minimo = tiempos_recursion[x]
        # Se aumenta el contador para continuar operando
        x += 1
    # Se elimina el minimo de la lista tiempos_recursion
    tiempos_recursion.remove(minimo)
    # Se agrega el minimo a la lista ordenada_recursiva
    ordenada_recursiva.append(minimo)

# Se crea la lista ordenada_total donde iran los tiempos de
# tiempos_totales de forma creciente
ordenada_total = []
# Mientras el largo de ordenada_total sea distinto al valor de largo
while len(ordenada_total) != largo:
    # Se declara r = 0 para poder iterar
    r = 0
    # Se declara minimo como el primer elemento de tiempos_totales
    minimo = tiempos_totales[r]
    # Mientras r sea menor al largo de tiempos_totales
    while r < len(tiempos_totales):
        # Si el elemento actual es menor al minimo
        if tiempos_totales[r] < minimo:
            # Se declara minimo como el elemento actual
            minimo = tiempos_totales[r]
        # Se aumenta r en 1 para continuar iterando
        r += 1
    # Si minimo es distinto de 0.0
    if minimo != 0.0:
        # Se guarda la posicion de minimo en copia_total
        posicion = copia_total.index(minimo)
        # Se agrega a viajes_ordenados el elemento de lista_viajes
        # que tiene la misma posicion que el minimo distinto de 0.0
        viajes_ordenados.append(lista_viajes[posicion])
    # Se elimina minimo de tiempos_totales
    tiempos_totales.remove(minimo)
    # Se agrega minimo a la lista ordenada_total
    ordenada_total.append(minimo)

# SALIDA
# Se crea el archivo salida.txt tal como se detallo en el enunciado
# del problema
escritura_archivo("salida.txt", lineas_nuevo_archivo)
# Se dibuja el grafico de la funcion iterativa
grafico = plt.plot(viajes_ordenados, ordenada_iterativa)
# Se configura el estilo de la grafica de la funcion iterativa
plt.setp(grafico, 'marker', 'o', 'color', 'g',
         'linewidth', 2.0, label="Funcion Iterativa")
# Se dibuja el grafico de la funcion recursiva
grafico2 = plt.plot(viajes_ordenados, ordenada_recursiva)
# Se configura el estilo de la grafica de la funcion recursiva
plt.setp(grafico2, 'linestyle', '--', 'color',
         'b', 'linewidth', 2.0, label="Funcion Recursiva")
# Se muestran por pantalla los labels
plt.legend()
# Se agrega el titulo del grafico
plt.title("Grafico de Tiempos Iterativos y Recursivos de cada viaje.")
# Se agrega el nombre del eje X del grafico
plt.xlabel("Número de viajes.")
# Se agrega el nombre del eje Y del grafico
plt.ylabel("Tiempo(en ms).")
# Se muestra por pantalla el grafico
plt.show()
