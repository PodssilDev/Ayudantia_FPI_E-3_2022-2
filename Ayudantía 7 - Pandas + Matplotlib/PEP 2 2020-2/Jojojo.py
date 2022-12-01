def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def escribir_archivo(nombre_archivo, lineas):
    archivo = open(nombre_archivo, "w")

    for linea in lineas:
        archivo.write(linea)

    archivo.close()

