def cargar_fecha():
    dd = int(input("Ingresar numero de día: "))
    mm = int(input("Ingresar num-ero de mes: "))
    aa = int(input("Ingresar numero de año: "))
    return(dd, mm, aa)


def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")

# BLOQUE PRINCIPAL DEL PROGRAMA
fecha = cargar_fecha()
imprimir_fecha(fecha)