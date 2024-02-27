# Día 7: Cuestionario para determinar si eres un superfan de 'The Big Bang Theory'
# Este código realiza preguntas al usuario para determinar su nivel de conocimiento sobre la serie.

# Muestra un mensaje de bienvenida al cuestionario
print("¿Eres un superfan de 'The Big Bang Theory' o un falso fan?")
print()
print("Responde estas preguntas para descubrirlo.")

# Realiza la primera pregunta al usuario
Gafas = input("¿Alguien usa gafas?")

# Verifica si la respuesta del usuario es correcta y continúa con las preguntas adicionales si es necesario
if Gafas == "si":
    print("Correcto!")
else:
    print("Respuesta equivocada")
    # Solicita al usuario que identifique quién en la serie usa gafas
    QuienGafas = input("¿Y quién usa gafas?")
    if QuienGafas == "Leonard":
        print("Lo entendiste")  # Muestra un mensaje si el usuario responde correctamente
    else:
        print("¡Intenta otra vez!")  # Muestra un mensaje si el usuario responde incorrectamente
