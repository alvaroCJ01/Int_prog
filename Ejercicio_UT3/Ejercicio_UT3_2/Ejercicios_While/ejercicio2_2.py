iteracion=0
b=float(0)
while True:
    a=float(input("Introduzca un numero (0 para salir): "))
    if a == 0:
        break
    b=a+b
    iteracion=iteracion+1

    
print(f"El resultado de la suma de los números es: {b}")
print(f"La media de la suma de los números: {b/iteracion}")