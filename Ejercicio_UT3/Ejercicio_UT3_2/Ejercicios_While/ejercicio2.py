a=float(1)
iteracion=0
b=float(0)
while a != 0:
    a=float(input("Introduzca un numero (0 para salir): "))
    b=a+b
    if a != 0:
        iteracion=iteracion+1
print(f"El resultado de la suma de los números es: {b}")
print(f"La media de la suma de los números: {b/iteracion}")

