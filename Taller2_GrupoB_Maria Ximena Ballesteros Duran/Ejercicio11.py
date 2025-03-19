#Inicializa el contador de números ingresados.
total_numeros = 0

#Se utilica un bucle que continuará hasta que se cumpla alguna condición.
while True:
    numero = int(input("Ingresa un número positivo: "))
    
    #Verificar si el número es positivo.
    if numero > 0:
        #Incrementa el contador de números.
        total_numeros += 1
        
        #Si el número es par y se han ingresado 100 o más números, se sale del bucle.
        if numero % 2 == 0 and total_numeros >= 100:
            break
        
        #Si el número es 5 y se han ingresado 80 o más números, se sale del bucle.
        if numero == 5 and total_numeros >= 80:
            break
    
    #Si el número es negativo se imprime el número inválido,ingresa un número positivo..
    else:
        print("Número inválido, ingresa un número positivo.")

#Se imprime el total de números que se han ingresado.        
print(f"Se han leído {total_numeros} números.")
