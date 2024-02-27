

# Imprime el título del juego
print("B A T A L L A    É P I C A    🪨  📄 ✂️")
print()
print("Selecciona tu movimiento (R, P o S)")
print()

# Solicita el movimiento del jugador 1
player1Move = input("Jugador 1 > ")
print()

# Solicita el movimiento del jugador 2
player2Move = input("Jugador 2 > ")
print()

# Compara los movimientos de los jugadores y determina el resultado
if player1Move == "R":
    if player2Move == "R":
        print("¡Ambos eligieron Piedra, empate!")
    elif player2Move == "S":
        print("¡El Jugador 1 hizo añicos las Tijeras del Jugador 2 con su Piedra!")
    elif player2Move == "P":
        print("¡La Piedra del Jugador 1 es cubierta por el Papel del Jugador 2!")
    else:
        print("¡Movimiento inválido del Jugador 2!")
elif player1Move == "P":
    if player2Move == "R":
        print("¡El Papel del Jugador 1 cubre la Piedra del Jugador 2!")
    elif player2Move == "S":
        print("¡El Papel del Jugador 1 es cortado en pedazos por las Tijeras del Jugador 2!")
    elif player2Move == "P":
        print("Dos pedazos de papel se golpean entre sí. Decepcionante. Empate.")
    else:
        print("¡Movimiento inválido del Jugador 2!")
elif player1Move == "S":
    if player2Move == "R":
        print("La Piedra del Jugador 2 convierte las Tijeras del Jugador 1 en polvo metálico")
    elif player2Move == "S":
        print("¡Ka-Shing! ¡Las Tijeras rebotan entre sí como una pelea de espadas dudosas! Empate.")
    elif player2Move == "P":
        print("¡Las Tijeras del Jugador 1 convierten el papel del Jugador 2 en confeti!")
    else:
        print("¡Movimiento inválido del Jugador 2!")
else:
    print("¡Movimiento inválido del Jugador 1!")
