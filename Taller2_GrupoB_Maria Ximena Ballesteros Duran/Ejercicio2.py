#Se le pide al usuario que ingrese las coordenadas.
x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))

x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))

#Calcular la diferencia entre las coordenadas.
diferencia_x = x2 - x1
diferencia_y = y2 - y1

#Calcular la distancia cuadrada.
distancia_cuadrada = (diferencia_x ** 2) + (diferencia_y ** 2)

#Se imprime el resultado de la distancia cuadrada.
print("La distancia cuadrada entre los puntos es:", distancia_cuadrada)
