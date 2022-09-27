'''
La NASA se encuentra en una misión super secreta. Para ello, lo
han contratado a usted para que construya un programa en Python
para encontrar un mensaje super secreto. Se le ha dado una lista
de listas con palabras, donde el objetivo es que usted decifre
un mensaje escondido en la primera letra de cada palabra.
Además, el mensaje esta encriptado, por lo que para desencriptarlo
usted debe invertir el orden del mensaje para finalmente encontrar
el verdadero mensaje super secreto.
¿Cual es el mensaje super secreto que busca la NASA?
'''
# BLOQUE DE DEFINICIÓN
# DEFINICIÓN DE CONSTANTES
LISTA_PALABRA = [["Nanai", "Orden",],
                ["Tormenta", "Insurreccion"],
                ["Arbol", "Patrulla"]]

# BLOQUE PRINCIPAL

# ENTRADA
# NO hay entrada para este programa

# PROCESAMIENTO
i = 0
mensaje_string = ""
mensaje_encriptado = []
while i < len(LISTA_PALABRA):
    sub_lista = LISTA_PALABRA[i]
    palabra1 = sub_lista[0]
    palabra2 = sub_lista[1]
    mensaje_encriptado.append(palabra1[0])
    mensaje_encriptado.append(palabra2[0])
    i = i + 1 # i += 1

mensaje_encriptado.reverse()
i = 0
while i < len(mensaje_encriptado):
    mensaje_string = mensaje_string + mensaje_encriptado[i]
    i += 1

# SALIDA
print(mensaje_encriptado)
print("El mensaje super secreto es: ", mensaje_string)
