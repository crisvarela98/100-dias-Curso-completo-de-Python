def inicio_sesion():
  # Bucle para solicitar el nombre de usuario y la contraseña
  while True:
      username = input("¿Cuál es tu nombre de usuario?: ")
      password = input("¿Cuál es tu contraseña? ")

      # Verifica si el nombre de usuario y la contraseña son correctos
      if username == "cris" and password == "1234":
          print("¡Bienvenido Cris!")
          break
      else:
          print("Ese no es el nombre de usuario o la contraseña correctos. ¡Inténtalo de nuevo!")
          continue

# Mensaje de bienvenida al sistema de inicio de sesión de Replit
print("SISTEMA DE INICIO DE SESIÓN DE REPLIT")
inicio_sesion()
