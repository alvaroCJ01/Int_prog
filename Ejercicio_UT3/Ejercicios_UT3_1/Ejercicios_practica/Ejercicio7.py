a=float(input("Introduzca la base: "))
b=float(input("Introduzca la potencia: "))

if b > 0:
    print(a**b)
elif b == 0:
    print("1")
elif b < 0:
    print(a**b)
else:
    print("Ha ocurrido un error inesperado.")