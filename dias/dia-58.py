import random, os, time

# Variable para llevar el total de intentos
totalIntentos = 0

# Función del juego
def juego():
    intentos = 0
    # Generar un número aleatorio entre 1 y 100
    numero = random.randint(1, 100)
    while True:
        # Pedir al usuario que ingrese un número
        intento = int(input("Elige un número entre 1 y 100: "))
        if intento > numero:
            print("Demasiado alto")
            intentos += 1
        elif intento < numero:
            print("Demasiado bajo")
            intentos += 1
        else:
            print("¡Exacto!")
            print(f"{intentos} intentos en esta ronda")
            return intentos

# Bucle principal del programa
while True:
    # Menú de opciones
    opcion = int(input("1: Juego de adivinar el número aleatorio\n2: Puntuación Total\n3: Salir\n> "))
    if opcion == 1:
        totalIntentos += juego()
    elif opcion == 2:
        print(f"Has tenido {totalIntentos} intentos en total")
    else:
        break
