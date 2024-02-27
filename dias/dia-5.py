# Día 5: ¿Qué personaje eres de 'Avengers'?
# Este código determina qué personaje del universo de 'Avengers' eres, según tus respuestas a algunas preguntas.

# Definición de códigos de color para resaltar los nombres de los personajes
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_END = "\033[0m"

# Muestra un mensaje de bienvenida
print("¿Qué personaje eres de 'Avengers'?")
print()
print("Responde estas preguntas y averigüemos.")
print()
print("Utilice S o N para sí y no..")

# Realiza una serie de preguntas al usuario para determinar qué personaje es
likeGreen = input("¿Te gusta el color verde?: ")
if likeGreen == "s":
    print(f"¡Debes ser {COLOR_GREEN}Hulk!{COLOR_END}")
elif likeGreen == "n":
    IronIsCool = input("¿Crees que construir robots es genial?: ")
    if IronIsCool == "s":
        print(f"Debes ser {COLOR_RED}Iron Man. ¡Genial traje!{COLOR_END}")
    else:
        TimeTravel = input("¿Te gusta viajar en el tiempo?: ")
        if TimeTravel == "s":
            print(f"¡Debes ser {COLOR_BLUE}el Capitán América!{COLOR_END}")
        else:
            Strong = input("¿Eres muy fuerte?: ")
            if Strong == "s":
                print(f"Debes ser {COLOR_YELLOW}Thor!{COLOR_END}")
            else:
                print("Supongo que no eres como nadie de 'Avengers.'")
else:
    print("Respuesta no válida.")
