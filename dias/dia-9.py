# Solicita al usuario su año de nacimiento.
birthYear = int(input("¿En qué año naciste?"))

# Determina la generación del usuario basándose en su año de nacimiento.
if birthYear <= 1946:
    print("Eres un tradicionalista.")
elif birthYear >= 1947 and birthYear <= 1964:
    print("¡Hola, baby boomers! ¿Cómo estás?")
elif birthYear >= 1965 and birthYear <= 1981:
    print("Generación X! ¿Qué pasa?")
elif birthYear >= 1982 and birthYear <= 1995:
    print("¡Millennials! ¡La era de la tecnología!")
elif birthYear >= 1996:
    print("¡Hola, Generación Z! ¿mucho TikTok?")
else: 
    # En caso de que el año de nacimiento no esté dentro de los rangos esperados, imprime un mensaje de error.
    print(birthYear, "no es un año válido")
