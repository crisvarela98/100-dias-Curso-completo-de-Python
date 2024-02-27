# Imprime el título del juego
print("B A T A L L A    É P I C A   2da parte")
print()
print("Selecciona tu movimiento (R, P o S)")
print()

# Inicializa las puntuaciones de los jugadores
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0

# Bucle principal del juego
while True: 
    # Solicita el movimiento del jugador 1
    jugador1Movimiento = input("Jugador 1 > ")
    print()

    # Solicita el movimiento del jugador 2
    jugador2Movimiento = input("Jugador 2 > ")
    print()

    # Compara los movimientos de los jugadores y determina el resultado
    if jugador1Movimiento == "R":
        if jugador2Movimiento == "R":
            print("Ambos eligieron Piedra, empate!")
        elif jugador2Movimiento == "S":
            print("¡El Jugador 1 hizo añicos las Tijeras del Jugador 2 con su Piedra!")
            puntuacion_jugador1 += 1
        elif jugador2Movimiento == "P":
            print("¡La Piedra del Jugador 1 es cubierta por el Papel del Jugador 2!")
            puntuacion_jugador2 += 1
    elif jugador1Movimiento == "P":
        if jugador2Movimiento == "R":
            print("¡El Papel del Jugador 1 cubre la Piedra del Jugador 2!")
            puntuacion_jugador1 += 1
        elif jugador2Movimiento == "S":
            print("¡El Papel del Jugador 1 es cortado en pedazos por las Tijeras del Jugador 2!")
            puntuacion_jugador2 += 1
        elif jugador2Movimiento == "P":
            print("Dos pedazos de papel se golpean entre sí. Decepcionante. Empate.")
    elif jugador1Movimiento == "S":
        if jugador2Movimiento == "R":
            print("La Piedra del Jugador 2 convierte las Tijeras del Jugador 1 en polvo metálico")
            puntuacion_jugador2 += 1
        elif jugador2Movimiento == "S":
            print("¡Ka-Shing! ¡Las Tijeras rebotan entre sí como una pelea de espadas dudosas! Empate.")
        elif jugador2Movimiento == "P":
            print("¡Las Tijeras del Jugador 1 convierten el papel del Jugador 2 en confeti!")
            puntuacion_jugador1 += 1

    # Muestra la puntuación de cada jugador
    print("El Jugador 1 tiene", puntuacion_jugador1, "victorias.")
    print("El Jugador 2 tiene", puntuacion_jugador2, "victorias.")

    # Verifica si un jugador ha alcanzado 3 victorias y finaliza el juego
    if puntuacion_jugador1 == 3 or puntuacion_jugador2 == 3:
        print("¡Gracias por jugar!")
        exit()
    else:
        continue
