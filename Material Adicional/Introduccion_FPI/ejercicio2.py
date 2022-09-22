'''
Usted es parte de Industrias Pythonia y se le ha asignado la tarea de
crear un programa en Python que diga si un año es bisiesto.
Matemáticamente un año es bisiesto si este es múltiplo de 4.
Si además es múltiplo de 100 no será bisiesto a no ser que sea múltiplo
de 400, que sí será bisiesto.

Hint: Ten en cuenta que 100 es múltiplo de 4 y por tanto cualquier número
que sea múltiplo de 100 también es múltiplo de 4
'''

# ENTRADA
agno = int(input("Ingrese un agno: "))

# PROCESAMIENTO
if agno % 4 == 0:
    if agno % 100 == 0:
        if agno % 400 == 0:
# SALIDAS
            print("El agno ingresado si es bisiesto!")
        else:
            print("El agno ingresado no es bisiesto!")
    else:
        print("El agno ingresado si es bisiesto!")
else:
    print("El agno ingresado no es bisiesto!")
