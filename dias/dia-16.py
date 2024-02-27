# Imprime el mensaje de bienvenida al juego
print("Bienvenido a Adivina la Letra de la Canción")
print()
print("¡Descubre la palabra faltante lo más rápido posible!")
print()

# Inicializa el contador de intentos
contador = 1

# Bucle principal del juego
while True:
    # Solicita al usuario que complete la letra de la canción
    letra = input("No quiero ______ nada. ")

    # Verifica si la respuesta del usuario es correcta
    if letra == "extrañar" or letra == "Extrañar":
        print("¡Lo lograste!")
    else:
        print("¡Incorrecto! ¡Inténtalo de nuevo!")
        contador += 1

    # Si el usuario completa la letra correctamente, sale del bucle
    if letra == "extrañar":
        break

# Imprime un mensaje de agradecimiento al usuario por jugar
print("¡Gracias por jugar!")

# Imprime el número de intentos que el usuario tomó para completar la letra correctamente
print("Obtuviste la letra correcta en", contador, "intentos.")
