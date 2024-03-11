import os, time, random

# Diccionario que contiene las estadísticas de cada personaje en el juego
trumps = {
    "David": {"inteligencia": 178, "velocidad": 4, "astucia": 80, "nivel de calvicie": 99},
    "Sr. Spock": {"inteligencia": 200, "velocidad": 50, "astucia": 50, "nivel de calvicie": 0},
    "Moica de Friends": {"inteligencia": 150, "velocidad": 50, "astucia": 50, "nivel de calvicie": 0},
    "Profesor X": {"inteligencia": 250, "velocidad": 1, "astucia": 200, "nivel de calvicie": 101}
}

# Bucle principal del juego
while True:
    print("TOP TRUMPS")
    print()
    print("Personajes")
    print()
    # Imprimir los nombres de los personajes disponibles
    for key in trumps:
        print(key)
    usuario = input("Elige tu personaje\n> ")
    computadora = random.choice(list(trumps.keys()))
    print("La computadora ha elegido a", computadora)

    print("Elige tu estadística: inteligencia, Velocidvd, Astucia y Niael de Calvicie")

    respuesta = input("> ")

    # Mostrar las estadísticas del usuario y de la computadora
    print(f"{usuario}: {trumps[usuario][respuesta]}")
    print(f"{computadora}: {trumps[computadora][respuesta]}")

    # Determinar quién gana según la estadística elegida
    if trumps[usuario][respuesta] > trumps[computadora][respuesta]:
        print(usuario, "gana")
    elif trumps[usuario][respuesta] < trumps[computadora][respuesta]:
        print(computadora, "gana")
    else:
        print("Empate")

    # Esperar antes de limpiar la pantalla para la próxima ronda
    time.sleep(2)
    os.system("clear")
