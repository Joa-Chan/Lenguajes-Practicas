# piedra_papel_tijerav2.py
# Juego mejorado contra la computadora: segunda versión
import random

# Configuración del juego
rondas_totales = 5  # Mejor de 5 rondas
opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print(f"Jugaremos al mejor de {rondas_totales} rondas.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0
rondas_para_ganar = (rondas_totales // 2) + 1  # Rondas necesarias para ganar

while ronda <= rondas_totales:
    print(f"\nRonda {ronda}")
    print(f"Puntos actuales - Tú: {puntos_usuario} | PC: {puntos_pc}")
    
    # Validación de entrada con bucle
    while True:
        jugada_usuario = input("Tu jugada: ").strip().lower()
        if jugada_usuario in opciones:
            break
        else:
            print("Entrada no válida. Debe ser piedra, papel o tijera. Intenta de nuevo.")
    
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")
    
    # Determinar ganador de la ronda
    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    
    
    # Terminación anticipada del juego
    # El juego termina antes si alguien ya alcanzó las rondas necesarias para ganar
    # En lugar de esperar a completar todas las rondas
    
    if puntos_usuario >= rondas_para_ganar:
        print(f"\n¡Ya ganaste el juego con {puntos_usuario} rondas!")
        break
    elif puntos_pc >= rondas_para_ganar:
        print(f"\nLa computadora ya ganó el juego con {puntos_pc} rondas.")
        break
    
    ronda += 1

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")
if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")