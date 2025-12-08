# Actividad Teórica 2 - Lenguajes 2025
# listas/diccionarios, funciones y control de flujo.

# 1) LISTAS Y DICCIONARIOS

numeros = [2, 4, 2, 6, 4]   # lista simple

# Diccionario para contar cuántas veces aparece cada número
conteo = {}
for n in numeros:
    if n in conteo:
        conteo[n] += 1
    else:
        conteo[n] = 1

print("Conteo de números:", conteo)
# Ejemplo salida: {2: 2, 4: 2, 6: 1}


# 2) FUNCIONES

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("Resultado de sumar 3 + 5:", resultado)


# CONTROL DE FLUJO (IF + FOR)

valores = [1, 2, 3, 4]

for v in valores:
    if v % 2 == 0:
        print(v, "es par")
    else:
        print(v, "es impar")