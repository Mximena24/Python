#Se le pide al usuario que ingrese un número n y m.
n = int(input("Ingresa el número n: "))
m = int(input("Ingresa el número m: "))

#Verificar que m sea mayor que n.
if m <= n:
    print("Error: m debe ser mayor que n.")

else:
    #Inicializar la variable suma.
    suma = 0

    #Se utiliza un bucle para sumar los números entre n y m, sin incluir n y m.
    for i in range(n + 1, m):
        #Sumar el valor de i a la variable suma.
        suma += i
    #Se imprime el resultado de la suma de los numeros n y m.
    print(f"La suma de los números entre {n} y {m} es: {suma}")
