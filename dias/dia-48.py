import os, time

# Bucle principal del programa
while True:
    print("TABLA DE PUNTUACIONES MÁXIMAS")
    print()
    # Solicitar las iniciales del jugador
    iniciales = input("INICIALES > ").upper()
    # Solicitar la puntuación del jugador
    puntuacion = input("PUNTUACIÓN > ")
    print()

    # Abrir el archivo "high.score" en modo de escritura, si no existe, se creará
    archivo = open("high.score", "a+")
    # Escribir las iniciales y la puntuación del jugador en el archivo
    archivo.write(f"{iniciales} {puntuacion}\n")
    # Cerrar el archivo
    archivo.close()

    print("AGREGADO")
    # Esperar un segundo antes de limpiar la pantalla para la próxima entrada
    time.sleep(1)
    os.system("clear")

