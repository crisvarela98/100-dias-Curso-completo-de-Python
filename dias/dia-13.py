# Imprime el título del programa
print("Calculadora de Calificaciones de Examen")
print()

# Solicita al usuario el nombre del examen
name_of_exam = input("Nombre del examen: ")
print()

# Solicita al usuario la puntuación máxima posible y su puntuación obtenida
total_score = int(input("Puntuación máxima posible: "))
your_score = int(input("Tu puntuación: "))
print()

# Calcula el porcentaje de la puntuación obtenida
number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score) * 100, 2)

# Imprime el porcentaje obtenido
print("Obtuviste", final_perc, "%")

# Determina la calificación correspondiente al porcentaje obtenido
if final_number >= 0.90:
    print("Tu calificación es A+")
elif final_number >= 0.80 and final_number <= 0.89:
    print("Tu calificación es A-.")
elif final_number >= 0.70 and final_number <= 0.79:
    print("Tu calificación es B.")
elif final_number >= 0.60 and final_number <= 0.69:
    print("Tu calificación es C.")
elif final_number >= 0.50 and final_number <= 0.59:
    print("Tu calificación es D.")
elif final_number <= 0.49:
    print("Tu calificación es U.")
else:
    print("¡Inténtalo de nuevo!")
