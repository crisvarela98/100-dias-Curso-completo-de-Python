# Mensaje de bienvenida al juego Adivina el Número
print("Bienvenido a Adivina el Número.")
print()
print("Adivina un número entre 1 y 10,000 y te diré si es demasiado bajo, demasiado alto o si lo has adivinado correctamente.")
print()
print("¡Vamos a jugar!")

# Importa el módulo random para generar un número aleatorio
import random

# Inicializa el contador de intentos
intentos = 1

# Genera un número aleatorio entre 1 y 10,000
miNumero = random.randint(1, 10000)

# Bucle principal del juego
while True: 
    # Solicita al usuario que elija un número entre 1 y 10,000
    numero_usuario = int(input("Elige un número entre 1 y 10,000: "))

    # Compara el número elegido por el usuario con el número aleatorio generado
    if numero_usuario < miNumero:
        print("Ese número es demasiado bajo. ¡Inténtalo de nuevo!")
        intentos += 1
    elif numero_usuario > miNumero:
        print("Ese número es demasiado alto. ¡Inténtalo de nuevo!")
        intentos += 1
    elif numero_usuario == miNumero:
        print("¡Eres un ganador! 🥳🥳")
        break 
    else:
        print("Ese no es un número que reconozca.")

# Imprime la cantidad de intentos necesarios para adivinar el número
print("Te tomó", intentos, "intentos para obtener la respuesta correcta.")
