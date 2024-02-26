orden = input("¿Qué te gustaría pedir: pizza or hamburguesa? ")
if orden == "hamburguesa":
    print("Tu orden es una hamburguesa")
    print("Gracias.")
    queso = input("¿Quieres queso?")
    if queso == "si":
        print("Lo tienes!")
    else:
        print("No, gracias.")
elif orden == "pizza":
    print("Pizza en marcha.")
    toppings = input("¿Quieres pepperoni?")
    if toppings == "si":
        print("Agregaremos pepperoni.")
    else:
        print("Tu pizza no tendrá pepperoni.")
else:
    print("Lo siento, no entendí tu pedido.")
