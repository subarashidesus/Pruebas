def suma_numeros_pares(lista):
    """
    Esta función calcula la suma de los números pares en una lista dada.
    
    Parámetros:
    lista (list): La lista de números.
    
    Retorna:
    int: La suma de los números pares en la lista.
    """
    suma = 0
    for numero in lista:
        if numero % 2 == 0:  # Verificar si el número es par
            suma += numero
    return suma

# Ejemplo de lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular la suma de los números pares utilizando la función
suma_pares = suma_numeros_pares(numeros)

# Mostrar el resultado
print("La suma de los números pares en la lista es:", suma_pares)
