# Día 4: Simulador de Historias de Aventuras
# Este código crea una historia épica con el usuario como protagonista, usando colores para resaltar ciertos elementos.

# Definición de la clase 'color' que contiene códigos de escape ANSI para colores de texto
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

# Muestra un mensaje de bienvenida al simulador de historias de aventuras
print("Bienvenido a tu Simulador de Historias de Aventuras.")
print ()
print("Te haré un montón de preguntas y luego crearé una historia épica contigo como estrella.")
print()

# Solicita información al usuario para crear la historia
name = input("¿Cuál es tu nombre? ")
print()
enemyName = input("¿Cuál es el nombre de tu enemigo? ")
print()
superPower = input("¿Cuál es tu superpoder? ")
print()
live = input("¿Dónde vives?")
print()
food = input("¿Cuál es tu comida favorita?")
print()

# Imprime la historia épica con el usuario como protagonista y utilizando colores
print("Hola", color.BOLD + color.PURPLE + name + color.END,
  "Tu habilidad para", color.BOLD + color.BLUE + superPower + color.END,
  "se asegurará de que nunca tengas que mirar a", color.BOLD + color.RED + enemyName + color.END,
  "de nuevo. Ve a comer", color.BOLD + color.GREEN + food + color.END,
  "mientras caminas por las calles de", color.BOLD + color.YELLOW + live + color.END,
  "y usa", color.BOLD + color.BLUE + superPower + color.END,
  "para el bien y nunca para el mal!")
