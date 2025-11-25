horas_totales=0
for i in range(6):
    horas=int(input(f"Cuántas horas ha trabajado en el dia {i+1}: "))
    horas_totales+=horas
sueldo=int(input("Cuanto cobras la hora: "))
print(f"Ha trabajado {horas_totales} horas y ha cobrado {horas_totales*sueldo}€.")