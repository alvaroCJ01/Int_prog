base = float(input("Introduzca la base: "))
exponente = int(input("Introduzca el exponente: "))

if exponente < 0:
    exponente = int(input("Introduzca un exponente positivo: "))

if exponente == 0:
    resultado = float(1)
else:
    resultado = float(1)
    for i in range(exponente):
        resultado = base * resultado
print(resultado)