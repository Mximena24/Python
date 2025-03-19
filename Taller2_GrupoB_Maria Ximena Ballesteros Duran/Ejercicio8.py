#Se le pide al usuario que ingrese un texto.
texto = input("Ingresa un texto: ")

#Eliminar los espacios en blanco del texto.
texto = texto.replace(" ", "")

#Invertir el texto.
texto_invertido = texto[::-1]

#Verificar si el texto es igual al texto invertido.
if texto == texto_invertido:
    print("El texto SI es un palíndromo.")

#Si la condicion no se cumple imprimir que el texto NO es un palíndromo.
else:
    print("El texto NO es un palíndromo.")
