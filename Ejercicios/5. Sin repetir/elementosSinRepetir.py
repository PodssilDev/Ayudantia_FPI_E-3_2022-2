'''
Escriba un programa en Python que reciba como entrada una secuencia de palabras 
separadas por comas e imprima las palabras sin repeticiones en forma ordenada 
(alfabeticamente).
Ejemplo:
Entrada: rojo, blanco, negro, rojo, verde, negro
Salida: blanco, negro, rojo, verde
Recomendación: el método sort() ordena una lista
'''
# CODIGO ASCII

# ENTRADA
entradas = input("Ingrese palabras separadas solamente por coma (,): ")
lista_entradas = entradas.split(",")
# PROCESAMIENTO
lista_entradas.sort()
i = 0 # ITERADOR 
largo_lista = len(lista_entradas)
contador = 0
while i < largo_lista:
    elemento_actual = lista_entradas[i]
    contador = lista_entradas.count(elemento_actual)
    while contador > 1: # Mientras haya un elemento actual repetido
        lista_entradas.remove(elemento_actual)
        contador = lista_entradas.count(elemento_actual)
    largo_lista = len(lista_entradas)
    i += 1
# SALIDA
print("La lista sin elemento repetidos es: ", lista_entradas)
