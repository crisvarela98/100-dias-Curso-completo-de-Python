import random
import os
import time

# Lista de palabras
listaDePalabras = ["manzana", "naranja", "uvas", "pera"]
letrasElegidas = []
vidas = 6

# Se elige una palabra al azar de la lista
palabra = random.choice(listaDePalabras)

while True:
    time.sleep(1)
    os.system("clear")
    letra = input("Elige una letra: ").lower()

    if letra in letrasElegidas:
        print("Ya probaste esa letra antes")
        continue

    letrasElegidas.append(letra)

    if letra in palabra:
        print("Encontraste una letra")
    else:
        print("No, no está en la palabra")
        vidas -= 1

    todasLetras = True
    print()
    for letra_palabra in palabra:
        if letra_palabra in letrasElegidas:
            print(letra_palabra, end="")
        else:
            print("_", end="")
            todasLetras = False
    print()

    if todasLetras:
        print(f"¡Ganaste con {vidas} vidas restantes!")
        break

    if vidas <= 0:
        print(f"¡Te quedaste sin vidas! La palabra era {palabra}")
        break
    else:
        print(f"Quedan solo {vidas} vidas")
