from replit import db  # Importa la base de datos desde Replit
import datetime  # Importa la biblioteca para manejar fechas y horas
import os  # Importa el módulo para interactuar con el sistema operativo
import time  # Importa el módulo para pausar la ejecución por un tiempo determinado

def agregarEntrada():
  time.sleep(1)  # Pausa la ejecución por un segundo
  os.system("clear")  # Limpia la pantalla
  timestamp = datetime.datetime.now()  # Obtiene la fecha y hora actual
  print(f"Entrada de diario para {timestamp}")  # Imprime la fecha y hora actual para la entrada de diario
  print()
  entrada = input("> ")  # Solicita al usuario que ingrese una entrada para el diario
  db[timestamp] = entrada  # Almacena la entrada en la base de datos con la marca de tiempo como clave

def verEntrada():
  claves = db.keys()  # Obtiene todas las claves de la base de datos
  for clave in claves:
    time.sleep(1)  # Pausa la ejecución por un segundo
    os.system("clear")  # Limpia la pantalla
    print(f"""{clave}
    {db[clave]}""")  # Imprime la clave y su valor asociado (la entrada del diario)
    print()
    opt = input("¿Siguiente o salir? > ")  # Pregunta al usuario si desea continuar viendo entradas o salir
    if opt.lower()[0] == "s":  # Si el usuario elige continuar
      continue  # Continúa con el siguiente bucle
    else:
      break  # Sale del bucle

contraseña = input("Contraseña: ")  # Solicita al usuario que ingrese la contraseña
if contraseña != "1234":  # Verifica si la contraseña es correcta
  print("Incorrecta")  # Imprime un mensaje de contraseña incorrecta
  exit()  # Sale del programa
while True:
  os.system("clear")  # Limpia la pantalla
  menu = input("1: Agregar\n2: Ver\n> ")  # Solicita al usuario que elija una opción
  if menu == "1":
    agregarEntrada()  # Si elige 1, llama a la función para agregar una entrada
  else:
    verEntrada()  # Si elige cualquier otra cosa, llama a la función para ver las entradas
