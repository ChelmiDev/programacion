# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def bisiesto():
    anio: int = int(input("Introduce un año para saber si es bisiesto"))
    
    if anio % 4:
        print("El año:", anio, "no es bisiesto")

    else:
        print("El año:", anio, "es bisiesto")


bisiesto()
