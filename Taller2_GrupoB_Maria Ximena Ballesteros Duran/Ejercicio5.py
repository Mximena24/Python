#Se le pide al usuario que ingrese un número.
numero = int(input("Introduce un número: "))

if numero > 0:#Si el número es positivo.

    if numero % 2 == 0:#Si es divisible entre 2, es par positivo.
        print("El número es par positivo.")
    
    else:#Si no es divisible entre 2, es impar positivo.
        print("El número es impar positivo.")

elif numero < 0:#Si el número es negativo.
    
    if numero % 2 == 0:# Si es divisible entre 2, es par negativo.
        print("El número es par negativo.")
    
    else:# Si no es divisible entre 2, es impar negativo.
        print("El número es impar negativo.")

else:#Si el número es 0.
    print("El número cero no es ni positivo ni negativo.")
