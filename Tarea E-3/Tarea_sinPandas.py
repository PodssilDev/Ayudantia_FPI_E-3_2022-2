# BLOQUE DE DEFINICIONES

# IMPORTACION DE FUNCIONES
import numpy as np
import matplotlib.pyplot as plt

# DEFINICION DE FUNCIONES
'''
Entrada: Un nombre de un archivo (string)
Salida: Una lista que contiene las lineas de un archivo (list)
Descripcion: Funcion que obtiene las lineas de un archivo de texto,
guardando el resultado en una lista que contiene listas, donde cada
sublista contiene los elementos de una fila del archivo.
'''
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas_archivo = []
    for linea in archivo:
        linea = linea.strip()
        linea = linea.split(",")
        lineas_archivo.append(linea)
    archivo.close()
    return lineas_archivo


'''
Entrada: Una lista de listas que contiene las lineas de un archivo
Salida: Una lista que contiene las clasificaciones del archivo
Descripcion: Funcion que recorre las lineas del archivo y retorna una
lista que solo contiene las clasificaciones del archivo.
'''
def obtener_clasificaciones(lineas_archivo):
    clasificaciones = []
    for linea in lineas_archivo:
        clasificaciones.append(linea[3])
    return clasificaciones


'''
Entrada: Una lista de listas que contiene las lineas de un archivo
Salida: Una lista que contiene las coordenadas x del archivo
Descripcion: Funcion que recorre las lineas del archivo y retorna una
lista que solo contiene las coordenadas x del archivo.
'''
def obtener_coordenadas_x(lineas_archivo):
    coordenadas_x = []
    for linea in lineas_archivo:
        coordenadas_x.append(linea[1])
    return coordenadas_x


'''
Entrada: Una lista de listas que contiene las lineas de un archivo
Salida: Una lista que contiene las coordenadas y del archivo
Descripcion: Funcion que recorre las lineas del archivo y retorna una
lista que solo contiene las coordenadas y del archivo.
'''
def obtener_coordenadas_y(lineas_archivo):
    coordenadas_y = []
    for linea in lineas_archivo:
        coordenadas_y.append(linea[2])
    return coordenadas_y


# DEFINICION DE CONSTANTES
# No se necesitan constantes para este codigo.


# BLOQUE PRINCIPAL

# ENTRADA
lineas_archivo = leer_archivo("Ruta.txt")

# PROCESAMIENTO
# Obtenemos las clasificaciones del archivo de texto
clasificaciones = obtener_clasificaciones(lineas_archivo)
# Obtenemos las coordenadas del eje x del archivo
coordenadas_x = obtener_coordenadas_x(lineas_archivo)
# Obtenemos las coordenadas del eje y del archivo
coordenadas_y = obtener_coordenadas_y(lineas_archivo)

# Ahora debemos filtrar estas coordenadas, ya que hay coordenadas que no
# corresponden a la ruta.
ruta_x = []
ruta_y = []

# Se inicializa un contador para iterar. Se inicia desde 1 ya que no nos
# interesa acceder al string "Clasificaciones", el cual es el primer elemento
# de la lista de clasificaciones
i = 1
while i < len(clasificaciones):
    # Si la clasificación es B, entonces corresponde a un punto de servicio
    # el cual no es parte de la ruta
    if clasificaciones[i] != "B":
        # Agregamos a ruta_x y ruta_y a todas las coordenadas cuya clasificacion
        # no sea B
        ruta_x.append(int(coordenadas_x[i]))
        ruta_y.append(int(coordenadas_y[i]))
    # Se aumenta el contador para seguir iterando.
    i += 1

# Se agrega el punto inicial al final de las listas de ruta, ya que el punto
# inicial debe ser igual al punto final
ruta_x.append(ruta_x[0])
ruta_y.append(ruta_y[0])

# Ahora podemos realizar el grafico de la ruta
ruta = plt.plot(ruta_x, ruta_y, label = "Ruta")
# Configuramos el color para que la ruta sea de color rojo
plt.setp(ruta, "color", "r")

# Iniciamos un contador en 1, por la misma razon anterior
j = 1
while j < len(clasificaciones):
    # Si la clasificacion es R, entonces es un punto de retiro
    if clasificaciones[j] == "R":
        # Graficamos el punto de retiro como un cuadrado azul
        retiro = plt.plot(int(coordenadas_x[j]), int(coordenadas_y[j]), "s")
        plt.setp(retiro, "color", "b")
        
    # Si la clasificacion es E, entonces es un punto de entrega
    if clasificaciones[j] == "E":
        # Graficamos el punto de entrega como un cuadrado verde
        entrega = plt.plot(int(coordenadas_x[j]), int(coordenadas_y[j]), "s")
        plt.setp(entrega, "color", "g")
        
    # Si la clasificacion es B, entonces es un punto de servicio
    if clasificaciones[j] == "B":
        # Graficamos el punto de servicio como un asterisco amarillo
        servicios = plt.plot(int(coordenadas_x[j]), int(coordenadas_y[j]), "*")
        plt.setp(servicios, "color", "y")
        
    # Si la clasificacion es C, corresponde al centro de despacho
    if clasificaciones[j] == "C":
        # Graficamos el centro de despacho como un cuadrado rojo
        centro = plt.plot(int(coordenadas_x[j]), int(coordenadas_y[j]), "s")
        plt.setp(centro, "color", "r")
        
    # Aumentamos el contador para que se pueda iterar toda la lista
    j += 1

# Se configuran las leyendas. Es importante hacer esto fuera del ciclo while,
# de lo contrario la leyenda mostrara etiquetas repetidas.
plt.setp(centro, label = "Centro de despacho")
plt.setp(entrega, label = "Puntos de entrega")
plt.setp(retiro, label = "Puntos de retiro")
plt.setp(servicios, label = "Servicios")

# Se configura el titulo del grafico
plt.title("Ruta de despacho")

# Se configuran el nombre del eje x y eje y
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")

# SALIDA
# Es necesario colocar plt.legend() para que se puedan mostrar las etiquetas
plt.legend()
# Es necesario colocar plt.show() para que se pueda mostrar el grafico.
plt.show()