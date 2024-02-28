def newPrint(color, word):
  # Comprueba el color y establece el código de color ANSI correspondiente
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    # Si el color no está definido, establece el color de texto a su valor predeterminado
    print("\033[0m", word, sep="", end="")

print("Super Subrutina")
print("Con mi ", end="")
newPrint("green", "nuevo programa")
newPrint("reset", " puedo simplemente llamar a 'and' en rojo ")
newPrint("red", "y se imprimirá en rojo ")
newPrint("blue", "o incluso azul")
print()
