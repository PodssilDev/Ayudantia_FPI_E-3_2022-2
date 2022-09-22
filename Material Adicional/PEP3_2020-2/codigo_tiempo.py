# Se importa datetime del módulo datetime
from datetime import datetime

def calcular_tiempo_transcurrido(inicio, termino):
    '''
    Función que calcula el tiempo transcurrido entre un intervalo dado
    de elementos datetime
    Entrada: Dos objetos datetime
    Salida: Tiempo transcurrido en microsegundos
    '''
    return (termino - inicio).total_seconds() * 1000000

# Se guarda el momento exacto de inicio de la ejecución a evaluar
inicio = datetime.now()
# Se ejecuta la evaluación
funcion() # INVOQUE AQUÍ A SU FUNCIÓN
# Se guarda el momento exacto del fin de la ejecución a evaluar
termino = datetime.now()
# Se obtiene el tiempo total transcurrido
tiempo = calcular_tiempo_transcurrido(inicio, termino)
