# Se le pide al usuario que ingrese las notas.
n1 = float(input("Introduce la nota 1 (15%): "))
n2 = float(input("Introduce la nota 2 (20%): "))
n3 = float(input("Introduce la nota 3 (15%): "))
n4 = float(input("Introduce la nota 4 (30%): "))
n5 = float(input("Introduce la nota 5 (20%): "))

#Calcular la nota final.
notaFinal = (n1 * 0.15) + (n2 * 0.20) + (n3 * 0.15) + (n4 * 0.30) + (n5 * 0.20)
print(f"La nota final es: {notaFinal}")#Imprimir el resultado de la nota final.

#Clasificar el resultado basado en la nota final.
if notaFinal < 2.0:
    print("No puedes habilitar.")

elif notaFinal < 3.0:
    print("Reprobaste.")

elif 3.0 <= notaFinal <= 4.5:
    print("Aprobaste.")

else:
    print("Felicitaciones por tu nota.")
