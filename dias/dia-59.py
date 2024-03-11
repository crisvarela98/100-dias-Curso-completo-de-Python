def palindrome(palabra):
  # Caso base: Si la longitud de la palabra es menor o igual a 1, es un palíndromo
  if len(palabra) <= 1:
      return True
  # Si el primer y último caracter de la palabra no son iguales, no es un palíndromo
  if palabra[0] != palabra[-1]:
      return False
  # Llamada recursiva: Comprobación del palíndromo sin el primer y último caracter
  return palindrome(palabra[1:-1])

# Imprimir el resultado de comprobar si "racecar" es un palíndromo
print(palindrome("racecar"))
