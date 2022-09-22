# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE: John Patricio Serrano Carrasco
# RUT:
# CARRERA: Ingeniería Civil Informatica
# DESCRIPCIÓN DEL PROGRAMA: El programa crea el archivo "regalos.txt"
# que contiene en cada fila el nombre del niño y los regalos
# que debe recibir, basandose en su promedio de bondad, el cual
# se calcula gracias al archivo "bondad.txt" y en los regalos que pidio,
# los cuales estan registrados en "pedidos.txt".
# SE ASUME de que el orden de los niños en "pedidos.txt"  y "bondad.txt"
# es similar, por ejemplo, en el ejemplo dado, Aquiles Baeza no puede
# aparecer antes que Esteban Quito si en uno de los archivos
# Aquiles aparece antes, Esteban no puede salir despues de Elsa Payo si
# ya salio antes en algunos de los dos archivos y asi sucesivamente.

# BLOQUE DE DEFINICION
# IMPORTACIÓN DE MODULOS
# Se importa la función leer_archivo de Jojojo.py
from Jojojo import leer_archivo
# Se importa la función escrbir_archivo de Jojojo.py
from Jojojo import escribir_archivo
# DEFINICION DE FUNCIONES


def calculo_bondad(bondad_actual):
    '''Funcion que calcula la bondad promediode acuerdo a las notas del niño
    Entrada: Lista de notas del niño por mes (list)
    Salida: Promedio de las notas del niño (float)
    '''
    # Declaro j = 1 para poder recorrer bondad_actual sin considerar
    # el nombre en la posición 0
    j = 1
    # Declaro suma = 0 para poder sumar los elementos y
    # posteriormente sacar el promedio
    suma = 0
    # Mientras j sea menor al largo de bondad_actual
    while j < len(bondad_actual):
        # Se la nota de un mes guardada en bondad_actual
        suma = suma + bondad_actual[j]
        # Aumento el contador para poder seguir sumando elementos
        j += 1
    # Obtengo el promedio de la bondad
    suma = suma / (len(bondad_actual) - 1)
    # Retorna el promedio de la bondad
    return suma


def cantidad_nueva(regalos, i, pedidos_actual):
    '''Funcion que calcula la correcta cantidad de regalos que debe recibir
    el niño si es que pidio menos regalos de los que deberia recibir
    Entradas: Recibe como parametros la cantidad
    actual de regalos, el valor del contador i y la
    lista de pedidos actuales del niño (int, int, list)
    Salida: Devuelve la correcta cantidad de regalos que
    debe recibir el niño (int)
    '''
    # Si los regalos que debe recibir son mayores a los regalos que pidio
    if regalos > len(pedidos_actual) - 1:
        # Se saca la diferencia para obtener la verdadera cantidad de regalos
        regalos = regalos - (regalos - (len(pedidos_actual) - 1))
    # Devuelve la cantidad de regalos correcta
    return regalos

# BLOQUE PRINCIPAL
# ENTRADA
# Se guarda en bondad la lista que retorna la
# función leer_archivo usando "bondad.txt"
bondad = leer_archivo("bondad.txt")
# Se guarda en pedidos la lista que retorna la función
# leer_archivo usando "pedidos.txt"
pedidos = leer_archivo("pedidos.txt")
# PROCESAMIENTO
# Declaro i = 0 , para poder recorrer bondad
i = 0
# Declaro la lista lista_bondad para almacenar los
# promedios de bondad de los niños
lista_bondad = []
# Declaro la lista ninos_bondad para almacenar los nombres
# de los niños que tienen bondad
ninos_bondad = []
# Declaro la lista cantidad_regalos para almacenar la
# cantidad de regalos que debe recibir cada niño
cantidad_regalos = []
# Declaro la lista pidieron_regalos para almacenar los
# nombres de los niños que pidieron regalos
pidieron_regalos = []
# Declaro la lista listado_final para almacenar la
# lista final que se escribirá en el archivo
listado_final = []
# Mientras i sea menor al largo de bondad
while i < len(bondad):
    # Almaceno en bondad_actual el primer elemento de la lista bondad
    bondad_actual = bondad[i]
    # Utilizo split para que el string se convierta en
    # una lista, donde el primer elemento es  el nombre del
    # niño y los demas elementos son las notas por mes
    bondad_actual = bondad_actual.split(",")
    # Declaro j = 1 para poder recorrer la lista almacenada
    # en bondad_actual sin considerar el nombre, cuya posicion es el elemento 0
    j = 1
    # Mientras j sea menor al largo de la lista almacenada en bondad_actual
    while j < len(bondad_actual):
        # Transformo todas las notas de string a float, para
        # poder operar con ellas
        bondad_actual[j] = float(bondad_actual[j])
        # Incremento j en 1 para seguir transformando las notas
        j += 1
    # Agrego a la lista ninos_bondad el nombre del
    # niño almacenado en bondad_actual
    ninos_bondad.append(bondad_actual[0])
    # Obtengo el promedio de la bondad del niño, utilizando
    # la funcion calculo_bondad. El promedio se aproxima
    # a 1 decimal usando el modulo round
    promedio = round(calculo_bondad(bondad_actual), 1)
    # Agrego a la lista lista_bondad el promedio del niño
    lista_bondad.append(promedio)
    # Incremento i en 1 para continuar el ciclo while
    i += 1
# Declaro nuevamente i = 0, para poder recorrer la lista lista_bondad
i = 0
# Mientras i sea menor al largo de la lista lista_bondad
while i < len(lista_bondad):
    # Si la bondad promedio esta entre 1.0 y 3.9 (limites incluidos)
    if lista_bondad[i] < 4.0:
        # Se agrega un 0 a la lista de cantidad_regalos
        cantidad_regalos.append(0)
    # Si la bondad promedio esta entre 4.0 y 4.9 (limites incluidos)
    elif lista_bondad[i] < 5.0:
        # Se agrega un 1 a la lista de cantidad_regalos
        cantidad_regalos.append(1)
    # Si la bondad promedio esta entre 5.0 y 5.4 (limites incluidos)
    elif lista_bondad[i] < 5.5:
        # Se agrega un 2 a la lista de cantidad_regalos
        cantidad_regalos.append(2)
    # Si la bondad promedio esta entre 5.5 y 5.9 (limites incluidos)
    elif lista_bondad[i] < 6.0:
        # Se agrega un 3 a la lista de cantidad_regalos
        cantidad_regalos.append(3)
    # Si la bondad promedio esta entre 6.0 y 6.4 (limites incluidos)
    elif lista_bondad[i] < 6.5:
        # Se agrega un 4 a la lista de cantidad_regalos
        cantidad_regalos.append(4)
    # Si la bondad promedio esta entre 6.5 y 7.0 (limites incluidos)
    else:
        # Se agrega un 5 a la lista de cantidad_regalos
        cantidad_regalos.append(5)
    # Incremento i en 1 para continuar recorriendo la lista
    i += 1

# Declaro otra vez i = 0 para poder recorrer la lista de pedidos
i = 0
# Mientras i sea menor al largo de la lista de pedidos
while i < len(pedidos):
    # Almaceno en pedidos_actual el elemento actual de pedidos
    pedidos_actual = pedidos[i]
    # Utilizo split para que el string se transforme en una lista
    pedidos_actual = pedidos_actual.split(",")
    # Si el nombre del niño no esta en la lista de ninos_bondad
    if pedidos_actual[0] not in ninos_bondad:
        # Entonces se elimina el nombre del nino y sus
        # pedidos de la lista de pedidos
        pedidos.pop(i)
    # Si el nombre del nino esta en la lista de ninos_bondad
    else:
        # Se agrega el nombre del niño a la lista de los que pidieron regalos
        pidieron_regalos.append(pedidos_actual[0])
    # Incremento i en 1 para continuar recorriendo la lista
    i += 1

# Declaro i = 0 para poder recorrer la lista de ninos_bondad
i = 0
# Mientras i sea menor al largo de la lista de ninos_bondad
while i < len(ninos_bondad):
    # Si el niño no pidio regalos pero tiene una bondad mayor o igual a 4.0
    if ninos_bondad[i] not in pidieron_regalos and cantidad_regalos[i] >= 1:
        # Se agrega el nombre del niño y el regalo de bicicleta a la lista de
        # listado_final
        listado_final.append(ninos_bondad[i]+","+"bicicleta\n")
        # Se elimina de la lista la cantidad de
        # regalos que debia recibir el niño
        cantidad_regalos.pop(i)
        # Se elimina el nombre del niño de la lista de ninos_bondad
        ninos_bondad.pop(i)
    # Incremento i en 1 para continuar recorriendo la lista
    i += 1

# Declaro i = 0 para poder recorrer la lista de ninos_bondad
i = 0
# Mientras i sea menor al largo de la lista de ninos_bondad
while i < len(ninos_bondad):
    # Si la cantidad de regalos del niño es 0
    if cantidad_regalos[i] == 0:
        # Entonces su promedio bondad es menor a 4.0 y por lo
        # tanto recibe carbon como regalo
        # Se agrega a listado_final el nombre del niño y su
        # regalo como una nueva fila
        listado_final.append(ninos_bondad[i]+","+"carbon\n")
        # Se elimina el 0 de la cantidad de regalos del niño de
        # la lista de cantidad_regalos
        cantidad_regalos.pop(i)
        # Se elimina el nombre del niño de la lista de ninos_bondad
        ninos_bondad.pop(i)
        # Se elimina el nombre del niño de la lista de pidieron_regalos
        pidieron_regalos.pop(i)
        # Se elimina el nombre del niño y sus pedidos de la lista de pedidos
        pedidos.pop(i)
    # Incremento i en 1 para poder continuar recorriendo la lista
    i += 1
# Declaro i = 0 por ultima vez, para poder recorrer la lista cantidad_regalos
i = 0
# Mientras i sea menor al largo de la lista cantidad_regalos
while i < len(cantidad_regalos):
    # Almaceno en regalos la cantidad de regalos de los niños
    # que aun no tienen regalos asignados
    regalos = cantidad_regalos[i]
    # Almaceno en pedidos_actual el string de pedidos del niño
    pedidos_actual = pedidos[i]
    # Utilizo split() para poder transformar el string a una lista
    pedidos_actual = pedidos_actual.split(",")
    # Almaceno en regalos la cantidad correcta de regalos que
    # debe recibir el niño, utilizando la funcion cantidad_nueva
    regalos = cantidad_nueva(regalos, i, pedidos_actual)
    # Guardo en la cantidad de regalos el valor actualizado de regalos que
    # debe recibir el niño
    cantidad_regalos[i] = regalos
    # Almaceno en la variable fila el string del nombre
    # del niño junto con una ,
    fila = pedidos_actual[0]+","
    # Si la cantidad de regalos es igual al largo de pedidos_actual - 1
    if cantidad_regalos[i] == len(pedidos_actual) - 1:
        # Declaro j = 1 para poder realizar el ciclo while
        j = 1
        # Mientras j sea menor o igual a la cantidad de regalos
        while j <= regalos:
            # Si j es exactamente igual a la cantidad de regalos
            if j == regalos:
                # Entonces se agrega a la variable fila el ultimo pedido
                # del niño, el cual ya tiene "\n" en el string
                # del ultimo regalo
                fila = fila + pedidos_actual[j]
            # Si j es menor a la cantidad de regalos
            else:
                # Entonces se almacena otro regalo del niño junto con una ,
                fila = fila + pedidos_actual[j]+","
            # Aumento j en 1 para que se almacene en fila todos
            # los regalos correspondientes
            j += 1
        # Agrego en la lista listado_final el contenido de la
        # variable fila, la cual contiene un string que primero tiene al
        # nombre del niño y luego sus regalos, todos separados por ,
        listado_final.append(fila)
    # Si la cantidad de regalos no es igual al largo de pedidos_actual - 1
    else:
        # Declaro j = 1 para poder realizar el ciclo while
        j = 1
        # Mientras j sea menor o igual a la cantidad de regalos
        while j <= regalos:
            # Si j es exactamente igual a la cantidad de regalos
            if j == regalos:
                # Entonces en la variable fila se agrega el ultimo
                # pedidos del niño junto con el string "\n"
                fila = fila + pedidos_actual[j]+"\n"
            # Si j es menor a la cantidad de regalos
            else:
                # Se agrega a la variable fila el pedido actual
                # del niño junto con una ,
                fila = fila + pedidos_actual[j]+","
            # Aumento j en 1 para que el ciclo while pueda continuar
            j += 1
        # Agrego en la lista listado_final la variable fila, la cual
        # corresponde a un string que contiene primero al nombre del niño y
        # luegos sus regalos, todos separados por ,
        listado_final.append(fila)
    # Aumento i en 1, para que se continue recorriendo la lista y
    # todos los niños que faltan tengan sus regalos asignados
    i += 1
# SALIDA
# Como salida, el programa utiliza la funcion escribir_archivo
# cuyos parametros son el nombre del archivo a crear y una
# lista que contiene los contenidos del archivo a escribir.
# En este caso el programa crea el archivo "regalos.txt" que
# contiene en cada fila el nombre de cada niño  y los regalos que debe recibir.
escribir_archivo("regalos.txt", listado_final)
