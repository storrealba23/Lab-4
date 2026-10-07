"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

numero_secreto = 42  
while True:
    try:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print("¡Excelenteeeeee! Adivinaste el número.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")