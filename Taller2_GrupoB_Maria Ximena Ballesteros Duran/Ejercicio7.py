#Se le pide al usuario que ingrese tres números.
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

#Verificar si lo numeros estan incrementando.
if a < b and b < c:
    print("Los números están incrementando.")

#Verificar si los numeros estan disminuyendo.
elif a > b and b > c:
    print("Los números están disminuyendo.")

#Si no se cumplen las condiciones imprimir que los números no se incrementan ni disminuyen.
else:
    print("Los números ni incrementan ni disminuyen.")
