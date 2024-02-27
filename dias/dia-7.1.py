# Día 7.1: Pedido de comida
# Este código permite al usuario ordenar comida (pizza o hamburguesa) y personalizar su pedido.

# Solicita al usuario que elija entre pizza o hamburguesa
orden = input("¿Qué te gustaría pedir: pizza o hamburguesa? ")

# Realiza acciones basadas en la elección del usuario
if orden == "hamburguesa":
    print("Tu orden es una hamburguesa")
    print("Gracias.")
    # Pregunta al usuario si quiere queso en su hamburguesa
    queso = input("¿Quieres queso?")
    if queso == "si":
        print("Lo tienes!")  # Añade queso si el usuario lo desea
    else:
        print("No, gracias.")  # No añade queso si el usuario no lo desea
elif orden == "pizza":
    print("Pizza en marcha.")
    # Pregunta al usuario si quiere pepperoni en su pizza
    toppings = input("¿Quieres pepperoni?")
    if toppings == "si":
        print("Agregaremos pepperoni.")  # Añade pepperoni si el usuario lo desea
    else:
        print("Tu pizza no tendrá pepperoni.")  # No añade pepperoni si el usuario no lo desea
else:
    print("Lo siento, no entendí tu pedido.")  # Mensaje si la orden no es clara o no es válida
