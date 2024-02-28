import random

# Mensaje de bienvenida al juego Infinity Dice
print("Infinity Dice 🎲")

# Solicita al usuario el número de caras del dado
caras = int(input("¿Cuántas caras tiene el dado?: "))

# Variable para controlar si el juego continúa
jugar = "si"

# Función para lanzar el dado
def lanzar_dado(caras):
  print("Has lanzado el dado y obtuviste ", random.randint(1, caras))

# Bucle principal del juego
while jugar == "si":
    lanzar_dado(caras)
    jugar = input("¿Lanzar de nuevo?")
