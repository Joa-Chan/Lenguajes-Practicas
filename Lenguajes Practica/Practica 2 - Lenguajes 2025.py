# Practica 2 - Lenguajes 2025

import csv
from datetime import datetime
import json
import os

print("Iniciando analisis de entrenamientos...")
print()

# Leo el archivo CSV
entrenamientos = []
archivo = open('actividad_2.csv', 'r', encoding='utf-8')
lector = csv.DictReader(archivo)
for fila in lector:
    entrenamientos.append(fila)
archivo.close()

print(f"Se cargaron {len(entrenamientos)} registros del archivo")
print()

# Agrego el dia de la semana a cada entrenamiento
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

for entreno in entrenamientos:
    fecha = datetime.strptime(entreno['timestamp'], '%Y-%m-%d %H:%M')
    numero_dia = fecha.weekday()
    entreno['dia_semana'] = dias[numero_dia]

print("Dias de la semana identificados")
print()

# Cuento cuantos entrenamientos hay por dia
conteo_por_dia = {}
for dia in dias:
    conteo_por_dia[dia] = 0

for entreno in entrenamientos:
    dia = entreno['dia_semana']
    conteo_por_dia[dia] = conteo_por_dia[dia] + 1

print("Entrenamientos por dia:")
for dia in dias:
    print(f"  {dia}: {conteo_por_dia[dia]}")
print()

# Busco el dia con mas entrenamientos
maximo = 0
dia_mas_entrenamientos = ""
for dia in conteo_por_dia:
    if conteo_por_dia[dia] > maximo:
        maximo = conteo_por_dia[dia]
        dia_mas_entrenamientos = dia

print(f"El dia con mas entrenamientos es {dia_mas_entrenamientos} con {maximo} entrenamientos")
print()

# Calculo los dias entre el primero y el ultimo entrenamiento
fecha_inicio = datetime.strptime(entrenamientos[0]['timestamp'], '%Y-%m-%d %H:%M')
fecha_fin = datetime.strptime(entrenamientos[-1]['timestamp'], '%Y-%m-%d %H:%M')
diferencia = fecha_fin - fecha_inicio
dias_totales = diferencia.days

print(f"Primer entrenamiento: {entrenamientos[0]['timestamp']}")
print(f"Ultimo entrenamiento: {entrenamientos[-1]['timestamp']}")
print(f"Dias transcurridos: {dias_totales}")
print()

# Cuento entrenamientos por campeon
conteo_campeones = {}
for entreno in entrenamientos:
    campeon = entreno['campeon']
    if campeon in conteo_campeones:
        conteo_campeones[campeon] = conteo_campeones[campeon] + 1
    else:
        conteo_campeones[campeon] = 1

# Busco el campeon con mas entrenamientos
max_entrenamientos = 0
campeon_ganador = ""
for campeon in conteo_campeones:
    if conteo_campeones[campeon] > max_entrenamientos:
        max_entrenamientos = conteo_campeones[campeon]
        campeon_ganador = campeon

print(f"El campeon que mas entreno es {campeon_ganador} con {max_entrenamientos} entrenamientos")
print()

# Muestro el promedio por dia (en este caso es el total ya que es un solo periodo)
print("Promedio de entrenamientos por dia de la semana:")
for dia in dias:
    print(f"  {dia}: {conteo_por_dia[dia]}")
print()

# Busco el campeon que mas entrena los fines de semana
entrenamientos_finde = {}
for entreno in entrenamientos:
    if entreno['dia_semana'] == 'Sabado' or entreno['dia_semana'] == 'Domingo':
        campeon = entreno['campeon']
        if campeon in entrenamientos_finde:
            entrenamientos_finde[campeon] = entrenamientos_finde[campeon] + 1
        else:
            entrenamientos_finde[campeon] = 1

# Busco el maximo del fin de semana
max_finde = 0
campeon_finde = ""
for campeon in entrenamientos_finde:
    if entrenamientos_finde[campeon] > max_finde:
        max_finde = entrenamientos_finde[campeon]
        campeon_finde = campeon

print(f"El campeon que mas entrena los fines de semana es {campeon_finde} con {max_finde} entrenamientos")
print()

# Creo la carpeta salida si no existe
if not os.path.exists('salida'):
    os.mkdir('salida')

# Genero el archivo CSV con la cantidad de entrenamientos por campeon
archivo_csv = open('salida/entrenamientos_por_campeon.csv', 'w', newline='', encoding='utf-8')
escritor = csv.writer(archivo_csv)
escritor.writerow(['campeon', 'cantidad'])
for campeon in conteo_campeones:
    escritor.writerow([campeon, conteo_campeones[campeon]])
archivo_csv.close()

print("Archivo CSV generado en salida/entrenamientos_por_campeon.csv")
print()

# Preparo el JSON con el resumen por dia
datos_json = {
    'total_registros': len(entrenamientos),
    'dias': {}
}

# Inicializo los dias
for dia in dias:
    datos_json['dias'][dia] = {}

# Lleno con los datos de cada campeon por dia
for entreno in entrenamientos:
    dia = entreno['dia_semana']
    campeon = entreno['campeon']
    if campeon in datos_json['dias'][dia]:
        datos_json['dias'][dia][campeon] = datos_json['dias'][dia][campeon] + 1
    else:
        datos_json['dias'][dia][campeon] = 1

# Guardo el JSON
archivo_json = open('salida/resumen_por_dia.json', 'w', encoding='utf-8')
json.dump(datos_json, archivo_json, indent=2, ensure_ascii=False)
archivo_json.close()

print("Archivo JSON generado en salida/resumen_por_dia.json")
print()

print("Analisis completado!")
print()
print("Resumen:")
print(f"- Total de registros: {len(entrenamientos)}")
print(f"- Dia con mas entrenamientos: {dia_mas_entrenamientos} ({maximo})")
print(f"- Dias transcurridos: {dias_totales}")
print(f"- Campeon que mas entreno: {campeon_ganador} ({max_entrenamientos})")
print(f"- Campeon top fin de semana: {campeon_finde} ({max_finde})")