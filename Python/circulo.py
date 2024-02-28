import math

def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo dado su radio.
    
    Parámetros:
    radio (float): El radio del círculo.
    
    Retorna:
    float: El área del círculo.
    """
    area = math.pi * radio ** 2
    return area

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área del círculo utilizando la función
area_del_circulo = calcular_area_circulo(radio)

# Mostrar el resultado
print("El área del círculo con radio", radio, "es:", area_del_circulo)
