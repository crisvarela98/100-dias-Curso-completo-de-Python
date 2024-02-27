
  # Saluda al usuario y solicita su nombre.
  print("Hola. Bienvenido a tu generador de afirmaciones diarias.")
  name = input("¿Cómo te llamas?")

  # Comprueba si el nombre del usuario coincide con "Cris" o "Cris" y proporciona afirmaciones diarias personalizadas.
  if name =="cris" or name == "Cris":
      DOW = input("¿Cuál es el día de la semana?")
      # Imprime una afirmación personalizada dependiendo del día de la semana ingresado.
      if DOW == "lunes" or DOW == "Lunes":
          print("Va a ser un gran lunes", name)
      if DOW == "martes" or DOW == "Martes":
          print("¡Qué maravilloso martes es!", name)
      if DOW == "miércoles" or DOW == "Miércoles":
          print("Vamos mitad de semana", name)
      if DOW == "jueves" or DOW == "Jueves":
          print(name,"¡Tu semana casi termina!")
      if DOW == "viernes" or DOW == "Viernes":
          print(name, "¡Es viernes!")

  # Comprueba si el nombre del usuario coincide con "David" o "david" y proporciona afirmaciones diarias personalizadas en inglés.
  elif name == "David" or name== "david":
      DOW = input("What is the day of the week?")
      # Imprime una afirmación personalizada en inglés dependiendo del día de la semana ingresado.
      if DOW == "monday" or DOW == "Monday":
          print("It is going to be a great Monday", name)
      if DOW == "tuesday" or DOW == "Tuesday":
          print("You look great in that color", name)
      if DOW == "wednesday" or DOW == "Wednesday":
          print("You look chipper today", name)
      if DOW == "thursday" or DOW == "Thursday":
          print(name,"you are doing a great job!")
      if DOW == "friday" or DOW == "Friday":
          print(name, "it's FRIDAY!")

  # Si el nombre del usuario no coincide con ninguno de los casos anteriores, imprime un mensaje genérico.
  else:
      print("¡No sé tu nombre, pero espero que estés pasando un gran día!")
      print("I do not know your name, but I hope you are having a great day!")
