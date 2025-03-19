#Se le pide al usuario que ingrese la cantidad de segundos.
segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos // 3600#Calcular las horas.
minutos = (segundos % 3600) // 60#Calcular los minutos restantes.
segundosRestantes = segundos % 60#Calcular los segundos restantes.

#Se imprime el resultado en formato horas:minutos:segundos.
print(f"{segundos} segundos equivalen a:")
print(f"{horas}:{minutos}:{segundosRestantes}.")
