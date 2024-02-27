# Imprime el título del quiz
print("Quiz de 100 Días de Código")
print()

# Solicita al usuario que responda en qué lenguaje se está escribiendo
ans1 = input("¿En qué lenguaje estamos escribiendo? ")

# Verifica si la respuesta del usuario es "python"
if ans1 == "python":
    print("Correcto")
else:
    print("Incorrecto")

# Solicita al usuario que ingrese el número de la lección actual
ans2 = int(input("¿Qué número de lección es esta? "))

# Comprueba si el número de lección ingresado es mayor que 12
if ans2 > 12:
    print("Todavía no hemos llegado tan lejos")
# Comprueba si el número de lección ingresado es igual a 12
elif ans2 == 12:
    print("¡Correcto!")
else:
    print("¡Ya hemos pasado bastante eso!")
