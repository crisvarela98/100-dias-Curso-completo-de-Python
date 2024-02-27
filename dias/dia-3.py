# Día 3: Preparación de la cena
# Este código solicita al usuario información sobre una cena específica y luego la muestra.

# Solicita al usuario que ingrese información sobre la cena
food = input("Nombra un tipo de comida: ")
plant = input("Nombra verdura/s: ")
cookingType = input("¿Cuál es una forma de cocinarlo?")
burntFood = input("¿Qué tan cocido?")

print()
print("La cena de esta noche:")
print()
# Muestra la cena que se va a preparar utilizando la información ingresada por el usuario
print("Para la cena vamos a preparar", food, cookingType, burntFood, "con", plant)
