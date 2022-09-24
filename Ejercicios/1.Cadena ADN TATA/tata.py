'''
EJERCICIO PEP 1 2016-2:
Una caja TATA es una secuencia de ADN encontrada en varios 
organismos vivos. Comienza siempre con ”TATAAA”. Siempre sigue 
con tres o mas A’s en multiplos de tres, es decir, TATAAAAAA 
es una caja TATA, pues contiene 6 letras A, pero TATAAAAA no lo 
es, pues solo contiene 5.
Construya un programa en Python que reciba como entrada una 
secuencia de ADN como string y entregue la mayor secuencia de 
la caja TATA. Su solucion debe funcionar para cualquier secuencia 
de ADN.
'''

# ENTRADA
secuencia = input("Ingrese una secuencia de ADN: ")
# PROCESAMIENTO
secuencia_buscada = "TATAAA"
secuencia_encontrada = ""

while secuencia_buscada in secuencia:
    # ESTO ES PARTE DEL CICLO WHILE
    secuencia_encontrada = secuencia_buscada
    secuencia_buscada = secuencia_buscada + "AAA"

# ESTO NO ES PARTE DEL CICLO WHILE
# SALIDA
if(len(secuencia_encontrada) > 0):
    print("La secuencia de TATA encontrada es: ", secuencia_encontrada)
else:
    print("No se encontro una secuencia TATA")