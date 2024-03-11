import random
import os
import time

# Inicializar la lista para el cartón de bingo
bingo = []

# Función para generar un número aleatorio entre 1 y 90
def generar_numero():
    number = random.randint(1, 90)
    return number

# Función para imprimir de manera legible el cartón de bingo
def imprimir_carton():
    for fila in bingo:
        for item in fila:
            print(item, end="\t|\t")
        print()

# Función para crear un nuevo cartón de bingo
def crear_carton():
    global bingo
    numeros = []
    for i in range(8):
        num = generar_numero()
        # Asegurarse de que no haya números repetidos en el cartón
        while num in numeros:
            num = generar_numero()
        numeros.append(num)

    numeros.sort()

    # Asignar los números al cartón de bingo
    bingo = [[numeros[0], numeros[1], numeros[2]],
             [numeros[3], "BG", numeros[4]],
             [numeros[5], numeros[6], numeros[7]]
            ]

# Crear un nuevo cartón de bingo
crear_carton()

# Bucle principal del juego
while True:
    # Imprimir el cartón de bingo actualizado
    imprimir_carton()
    # Solicitar al usuario el próximo número
    num = int(input("Próximo número: "))
    # Marcar el número en el cartón de bingo si está presente
    for fila in range(3):
        for item in range(3):
            if bingo[fila][item] == num:
                bingo[fila][item] = "X"

    # Contar la cantidad de "X" en el cartón de bingo
    exes = 0
    for fila in bingo:
        for item in fila:
            if item == "X":
                exes += 1

    # Verificar si el jugador ha completado el cartón
    if exes == 8:
        print("¡Has ganado!")
        break

    # Esperar un segundo antes de borrar la pantalla y continuar
    time.sleep(1)
    os.system("clear")
