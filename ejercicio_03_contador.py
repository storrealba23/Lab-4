"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
frase = input("Ingrese una frase: ")
contador_vocales = 0
for letra in frase:
    if letra.lower() in 'aeiou':
        contador_vocales += 1
print(f"La frase '{frase}' tiene {contador_vocales} vocales.")
