'''
Construya un programa en Python que transforme una cantidad de días  a segundos.
Tenga en consideración que cada hora tiene 3600 segundos.
'''

# CONSTANTE
SEGUNDOS_POR_HORAS = 3600
HORAS_POR_DIA = 24

# ENTRADA
dias = int(input("Ingrese una cantidad de dias: "))

# PROCESAMIENTO
resultado = dias * HORAS_POR_DIA
resultado = SEGUNDOS_POR_HORAS * resultado

# SALIDA
print(dias, "dias transformado a segundos son: ", resultado, "segundos")
