from replit import db  # Importa la base de datos desde Replit
import datetime  # Importa la biblioteca para manejar fechas y horas
import os  # Importa el módulo para interactuar con el sistema operativo
import time  # Importa el módulo para pausar la ejecución por un tiempo determinado

def agregarTweet():
  tweet = input("🐥 > ")  # Solicita al usuario que ingrese un tweet
  timestamp = datetime.datetime.now()  # Obtiene la fecha y hora actual
  key = f"mes{timestamp}"  # Crea una clave basada en el mes y el momento en que se ingresó el tweet
  db[key] = tweet  # Almacena el tweet en la base de datos con la clave generada
  time.sleep(1)  # Espera un segundo
  os.system("clear")  # Limpia la pantalla

def verTweets():
  matches = db.prefix("mes")  # Obtiene todos los tweets almacenados con claves que comienzan con "mes"
  matches = matches[::-1]  # Invierte el orden de los tweets para mostrar los más recientes primero
  contador = 0  # Inicializa un contador para llevar el control de los tweets mostrados
  for i in matches:
    print(db[i])  # Imprime el tweet
    print()
    time.sleep(0.3)  # Espera 0.3 segundos antes de mostrar el siguiente tweet
    contador += 1  # Incrementa el contador de tweets mostrados
    if contador % 10 == 0:  # Si se han mostrado 10 tweets
      continuar = input("¿Mostrar los próximos 10?: ")  # Pregunta al usuario si desea ver más tweets
      if continuar.lower() == "no":  # Si el usuario responde "no"
        break  # Sale del bucle
  time.sleep(1)  # Espera un segundo
  os.system("clear")  # Limpia la pantalla

while True:
  print("Tweeter")  # Muestra el título de la aplicación
  menu = input("1: Agregar Tweet\n2: Ver Tweets\n> ")  # Solicita al usuario que elija una opción
  if menu == "1":
    agregarTweet()  # Si elige 1, llama a la función para agregar un tweet
  else:
    verTweets()  # Si elige cualquier otra cosa, llama a la función para ver los tweets
