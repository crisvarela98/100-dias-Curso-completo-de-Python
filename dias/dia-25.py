import random

# Función para lanzar un dado con un número variable de caras
def lanzar_dado(caras):
    resultado = random.randint(1, caras)
    return resultado

# Función para lanzar dados de 6 y 8 caras y calcular la salud del personaje
def lanzar_6_y_8():
    lanzamiento_dado_6 = lanzar_dado(6)
    lanzamiento_dado_8 = lanzar_dado(8)
    salud = lanzamiento_dado_6 * lanzamiento_dado_8
    return salud

# Mensaje de bienvenida al generador de estadísticas de personajes
print("⚔️ Generador de estadísticas de personajes ⚔️")

# Variable para controlar si se desea crear otro personaje
crearPersonaje = "si"

# Bucle para crear personajes
while crearPersonaje == "si":
    nombre_personaje = input("Nombre de tu guerrero: ")
    salud = str(lanzar_6_y_8())
    print("Su salud es ", salud, "hp" ) 
    crearPersonaje = input("¿Quieres crear otro personaje?")
