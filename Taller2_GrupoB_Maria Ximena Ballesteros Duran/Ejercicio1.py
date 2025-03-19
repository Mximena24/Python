#Solicitar al usuario que ingrese la masa del objeto en kg.
masa = float(input("Ingrese la masa del objeto en kilogramos (kg): "))

#L velocidad de la luz (3.0 * 10^8 m/s).
velocidad = 3.0e8

#Calcular la energía cinética utilizando la fórmula.
energia_cinetica = 0.5 * masa * velocidad * velocidad

#Se imprime el resultado de la energía cinética del objeto.
print(f"La energía cinética del objeto es: {energia_cinetica} Julios.")
