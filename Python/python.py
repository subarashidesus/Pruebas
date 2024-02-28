def es_primo(numero):
    """
    Esta función verifica si un número dado es primo o no.
    
    Parámetros:
    numero (int): El número a verificar.
    
    Retorna:
    bool: True si el número es primo, False de lo contrario.
    """
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero positivo: "))

# Verificar si el número ingresado es primo utilizando la función
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
