
# DESCRIPCION DEL PROGRAMA: Programa que recibe como entrada un string compuesto por
# varios movimientos y retorna un tablero donde cada movimiento es asignado una casilla
# del tablero. Se analiza cada movimiento y de el se obtiene la fila y la columna para
# obtener las coordenadas de la casilla del tablero 

# ENTRADA
entradas = input("Ingrese los movimientos, separados por una coma (,) y sin espacios: ")
lista_entradas = entradas.split(",")

# PROCESAMIENTO
tablero = []
i = 0 # Iterador
while i < 8:
    fila = []
    j = 0
    while j < 8:
        fila.append("  ")
        j += 1
    tablero.append(fila)
    i += 1

i = 0

while i < len(lista_entradas):
    # Obtenemos un movimiento de la lista de movimientos (entrada)
    movimiento_actual = lista_entradas[i]

    # Obtenemos la columna del movimiento actual
    if(movimiento_actual[2] == "A"):
        columna = 0
    elif(movimiento_actual[2] == "B"):
        columna = 1
    elif(movimiento_actual[2] == "C"):
        columna = 2
    elif(movimiento_actual[2] == "D"):
        columna = 3
    elif(movimiento_actual[2] == "E"):
        columna = 4
    elif(movimiento_actual[2] == "F"):
        columna = 5
    elif(movimiento_actual[2] == "G"):
        columna = 6
    else:
        columna = 7
    # Obtenemos la fila respetando la figura del enunciado
    fila = int(movimiento_actual[3]) - 1
    # Definimos la fila correctamente
    if fila == 0:
        fila = 7
    elif fila == 1:
        fila = 6
    elif fila == 2:
        fila = 5
    elif fila == 3:
        fila = 4
    elif fila == 4:
        fila = 3
    elif fila == 5:
        fila = 2
    elif fila == 6:
        fila = 1
    else:
        fila = 0
        
    # Creamos la casilla a colocar en el tablero
    casilla = movimiento_actual[0] + movimiento_actual[1]
    # Ingresamos la casilla al tablero
    tablero[fila][columna] = casilla
    i += 1
    
# SALIDA

k = 0
while k < len(tablero):
    print(tablero[k])
    k += 1
