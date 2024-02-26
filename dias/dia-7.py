print ("¿Eres un superfan de 'The Big Bang Theory' o un falso fan?")
print()
print("Responde estas preguntas para descubrirlo.")

Gafas = input("¿Alguien usa gafas?")
if Gafas == "si":
  print("Correcto!")
else:
  print("Respuesta equivocada")
  QuienGafas = input("¿Y quién usa gafas?")
  if QuienGafas == "Leonard":
    print("Lo entendiste")
  else:
    print("¡Intentar otra vez!")