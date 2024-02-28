def colorChange(color):
  # Función que devuelve el código de escape ANSI para cambiar el color del texto en la terminal.
  if color == "red":
      return ("\033[31m")  # Rojo
  elif color == "white":
      return ("\033[0m")    # Blanco
  elif color == "blue":
      return ("\033[34m")   # Azul
  elif color == "yellow":
      return ("\033[33m")   # Amarillo
  elif color == "green":
      return ("\033[32m")   # Verde
  elif color == "purple":
      return ("\033[35m")   # Morado

# Título para la aplicación de música con colores
title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

# Imprimir el título centrado
print(f"        {title:^35}")

# Imprimir información de la canción y artista
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

# Definir opciones de control
prev = "prev"
next = "next"
pause = "pause"

# Imprimir opciones de control con colores correspondientes
print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")

print()  # Salto de línea

# Bienvenida al usuario
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>35}")
text = "Honest."
print(f"{colorChange('red')}{text:^35}")

# Solicitar nombre de usuario y contraseña
text = "Username: "
username = input(f"{colorChange('white')}{text:^35}")
text = "Password: "
password = input(f"{colorChange('white')}{text:^35}")
