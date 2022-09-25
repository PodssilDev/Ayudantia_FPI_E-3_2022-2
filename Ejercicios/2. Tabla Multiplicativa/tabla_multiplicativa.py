'''
Cree un programa en Python que reciba un número entero positivo y
calcule la tabla multiplicativa de un número hasta cierto número 
dado por entrada.
'''

# ENTRADA
numero1 = abs(int(input("Ingrese un numero entero positivo: ")))
numero2 = abs(int(input("Ingrese otro numero entero positivo: ")))
# PROCESAMIENTO
i = 0
while i <= numero2:
    print(numero1, "x", i, "=", numero1 * i)
    i += 1

# SALIDA
print("Programa terminado.")