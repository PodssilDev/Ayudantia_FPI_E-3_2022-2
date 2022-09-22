'''
Construya un programa donde al usuario se le pregunte su año y se le entregue
su edad de acuerdo al año actual
'''

# CONSTANTES
AGNO = 2022

# ENTRADA
agno_nacimiento = int(input("Ingrese su agno de nacimiento: "))

# PROCESAMIENTO
# Calcula la diferencia entre el agno actual y el agno de nacimiento
resultado = AGNO - agno_nacimiento

# SALIDA
print("Su edad en el", AGNO, "deberia ser: ", resultado, "agnos")
