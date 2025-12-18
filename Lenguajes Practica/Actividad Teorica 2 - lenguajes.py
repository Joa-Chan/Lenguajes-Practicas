# actividad teorica 2 - lenguajes de programacion
# conceptos: diccionarios, funciones y archivos csv

import csv

print("inicio del programa")

# concepto 1: diccionarios
print("\nconcepto 1: diccionarios\n")

# ejemplo: contar palabras en una frase
frase = "python es facil python es util"
palabras = frase.split()

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("frase:", frase)
print("conteo de palabras:")
for palabra, cantidad in contador.items():
    print(palabra, ":", cantidad)

# concepto 2: funciones
print("\nconcepto 2: funciones\n")

# funcion que calcula el promedio de una lista de notas
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

notas_alumno = [7, 8, 6, 9]
promedio = calcular_promedio(notas_alumno)

print("notas:", notas_alumno)
print("promedio:", promedio)

# concepto 3: archivos csv
print("\nconcepto 3: archivos csv\n")

# crear archivo csv
archivo = open('alumnos.csv', 'w', newline='', encoding='utf-8')
escritor = csv.writer(archivo)
escritor.writerow(['nombre', 'nota'])
escritor.writerow(['ana', 8])
escritor.writerow(['juan', 6])
escritor.writerow(['maria', 9])
archivo.close()

print("archivo alumnos.csv creado")

# leer archivo csv y mostrar aprobados
print("alumnos aprobados:")
archivo = open('alumnos.csv', 'r', encoding='utf-8')
lector = csv.DictReader(archivo)
for fila in lector:
    nota = int(fila['nota'])
    if nota >= 6:
        print(fila['nombre'], "- nota:", nota)
archivo.close()

print("fin del programa")