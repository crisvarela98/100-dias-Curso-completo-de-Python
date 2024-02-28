# Definición de la función para cambiar el color del texto en la terminal
def cambiarColor(color):
    if color == "r":
        print("\033[31m", end="")  # Cambiar el color a rojo
    elif color == " ":
        print("\033[0m", end="")   # Restablecer el color a su estado por defecto
    elif color == "b":
        print("\033[34m", end="")  # Cambiar el color a azul
    elif color == "y":
        print("\033[33m", end="")  # Cambiar el color a amarillo
    elif color == "g":
        print("\033[32m", end="")  # Cambiar el color a verde
    elif color == "p":
        print("\033[35m", end="")  # Cambiar el color a morado

# Solicitar al usuario la frase que desea convertir en arcoíris
frase = input("¿Qué frase quieres convertir en arcoíris?: ")

# Iterar sobre cada letra de la frase
for letra in frase:
    cambiarColor(letra.lower())  # Cambiar el color de la letra
    print(letra, end="")          # Imprimir la letra
print()  # Imprimir un salto de línea al final
