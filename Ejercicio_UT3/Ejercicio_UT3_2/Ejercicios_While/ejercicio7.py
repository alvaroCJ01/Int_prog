base=float(input("Introduce la base de la potencia: "))
exponente=int(input("Introduce el exponente de la potencia: "))
iteracion=0
resultado=base
while exponente < 0:
    print("Introduzca una exponente positivo.")
    exponente=int(input("Introduce el exponente de la potencia: "))
if exponente == 0:
    print(1.0)
else:
    while exponente > iteracion+1:
        resultado=resultado*base
        iteracion+= 1
    else:
        print(resultado)