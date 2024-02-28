print("30 Días Pasaron - ¿Qué opinas?")
print()

# Lista para almacenar las respuestas de los 30 días
respuestas = []

for i in range(1, 31):
    thought = input(f"Día {i}:\n")
    respuestas.append(thought)  # Agrega la respuesta a la lista
    print()

# Al finalizar los 30 días, imprime todas las respuestas juntas
print("Resumen de tus sentimientos en los últimos 30 días:")
print('\n'.join(respuestas))
print()

