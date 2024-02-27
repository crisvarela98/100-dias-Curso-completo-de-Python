# Variable para controlar la salida del bucle
salida = "no"

# Bucle principal que se ejecuta mientras el usuario no decida salir
while salida == "no":
    # Solicita al usuario el sonido del animal que desea escuchar
    sonido_animal = input("¿Qué sonido de animal quieres escuchar? ")

    # Comprueba qué sonido de animal solicitó el usuario y muestra el emoji correspondiente
    if sonido_animal == "vaca" or sonido_animal == "Vaca":
        print("🐮 Muu")
    elif sonido_animal == "cerdo" or sonido_animal == "Cerdo":
        print("🐷 Oink")
    elif sonido_animal == "oveja" or sonido_animal == "Oveja":
        print("🐑 Bee")
    elif sonido_animal == "pato" or sonido_animal == "Pato":
        print("🦆 Cuac")
    elif sonido_animal == "perro" or sonido_animal == "Perro":
        print("🐶 Guau")
    elif sonido_animal == "gato" or sonido_animal == "Gato":
        print("🐱 Miau")
    else:
        print("No conozco ese sonido de animal. Inténtalo de nuevo.")

    # Pregunta al usuario si desea salir del programa
    salida = input("¿Quieres salir? (si/no): ")
