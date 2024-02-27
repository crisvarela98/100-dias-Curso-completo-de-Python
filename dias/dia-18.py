# Secuencias de escape ANSI para cambiar el color del texto
ROJO = '\033[91m'
CELESTE = '\033[96m'
VERDE = '\033[92m'
FIN_COLOR = '\033[0m'

# Mensaje de bienvenida al juego
print("Bienvenido a Adivina el Número.")
print()
print("Adivina un número entre 1 y 1,000,000 y te diré si es demasiado " + ROJO + "bajo" + FIN_COLOR + ", demasiado " + CELESTE + "alto" + FIN_COLOR + " o si lo has adivinado correctamente.")
print()
print("¡Vamos a jugar!")

# Número correcto que el usuario debe adivinar
numero_correcto = 2300

# Inicialización del contador de intentos
intentos = 1

# Bucle principal del juego
while True:
    # Solicita al usuario que ingrese un número entre 1 y 10,000
    numero_usuario = int(input("Elige un número entre 1 y 10,000: "))

    # Verifica si el usuario ingresó un número negativo
    if numero_usuario < 0:
        print("¡Ahora nunca sabremos cuál es la respuesta!")
        exit()

    # Compara el número ingresado por el usuario con el número correcto
    if numero_usuario < numero_correcto:
        print("Ese número es demasiado " + ROJO + "bajo" + FIN_COLOR + ". ¡Inténtalo de nuevo!")
        intentos += 1
    elif numero_usuario > numero_correcto:
        print("Ese número es demasiado " + CELESTE + "alto" + FIN_COLOR + ". ¡Inténtalo de nuevo!")
        intentos += 1
    elif numero_usuario == numero_correcto:
        print(VERDE + "¡Eres un ganador! 🥳🥳" + FIN_COLOR)
        break 
    else:
        print("Ese no es un número que reconozca.")

# Muestra la cantidad de intentos necesarios para adivinar el número
print("Te tomó", intentos, "intentos para obtener la respuesta correcta.")

