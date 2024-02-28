from playsound import playsound
import pygame
import os
import time

# Inicializar Pygame
pygame.init()

def reproducir():
    # Cargar el archivo de audio
    pygame.mixer.music.load('dias/archivos/dia26/audio.wav')

    # Reproducir el archivo de audio
    pygame.mixer.music.play()

    while True:
        # Permite al usuario detener la reproducción en cualquier momento
        detener_reproduccion = input("Presiona 2 en cualquier momento para detener la reproducción y volver al menú: ")
        if detener_reproduccion == '2':
            pygame.mixer.music.stop() # Detener la reproducción del archivo de audio
            return # Salir de la función reproducir()
        else:
            continue

while True:
    os.system("clear")
    print("🎵 Reproductor de Música MyPOD")
    time.sleep(1)
    print("Presiona 1 para reproducir")
    time.sleep(1)
    print("Presiona 2 para salir")
    time.sleep(1)
    print("Presiona cualquier otra tecla para ver el menú nuevamente")
    entrada_usuario = input()

    if entrada_usuario == '1':
        print("¡Reproduciendo algunas melodías!")
        reproducir()
    elif entrada_usuario == '2':
        pygame.quit() # Finalizar Pygame antes de salir
        exit()
    else:
        continue
