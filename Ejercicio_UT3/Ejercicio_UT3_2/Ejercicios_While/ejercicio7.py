base=float(input("Introduce la base de la potencia: "))
exponente=int(input("Introduce el exponente de la potencia: "))
iteracion=0
resultado=base
if base < 0:
    print("Error, debe introducir un número positivo.")
    quit()
if exponente == 0:
    print(1.0)
    quit()
while exponente > iteracion+1:
    resultado=resultado*base
    iteracion+= 1
else:
    print(resultado)