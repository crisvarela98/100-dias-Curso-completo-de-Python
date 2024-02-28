# Mensaje de bienvenida al juego de Matemáticas
print("Bienvenido al Juego de Hechos Matemáticos")
print()
print("¿Qué tan bien conoces tus hechos matemáticos? Elige un número y te daré 10 hechos matemáticos para resolver.")
print()

# Solicita al usuario que elija un número para generar los hechos matemáticos
familia_hechos = int(input("Indica tus múltiplos: "))
print()

# Inicializa un contador para contar las respuestas correctas
contador = 0

# Bucle para generar y resolver 10 hechos matemáticos
for i in range(1, 11):
    # Calcula la respuesta correcta para el hecho matemático actual
    respuesta_correcta = i * familia_hechos

    # Imprime el hecho matemático actual y solicita al usuario que ingrese su respuesta
    print(i, "x", familia_hechos)
    respuesta = int(input("> "))

    # Compara la respuesta del usuario con la respuesta correcta y proporciona retroalimentación
    if respuesta == respuesta_correcta:
        print("¡Lo has acertado!")
        contador += 1
    else:
        print("Eso no es correcto. Debería haber sido", respuesta_correcta)

# Verifica si el usuario obtuvo todas las respuestas correctas y proporciona un mensaje adecuado
if contador == 10:
    print("¡Wow! ¡Una puntuación perfecta! 🥳")
else:
    print("Obtuviste", contador, "de 10 correctas.")
