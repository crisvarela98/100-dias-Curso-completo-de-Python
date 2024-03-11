def factorial(valor):
  # Caso base: Si el valor es 0 o 1, el factorial es 1
  if valor == 0 or valor == 1:
      return 1
  # Manejo de valores negativos
  elif valor < 0:
      return "Factorial no definido para valores negativos"
  else:
      resultado = 1
      # Iterar desde 1 hasta el valor y multiplicar cada número
      for i in range(2, valor + 1):
          resultado *= i
      return resultado

# Se imprime el factorial de 5
print(factorial(5))
