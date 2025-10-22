a=float(input("Introduzca un numero: "))
b=float(input("Introduzca un numero: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")
elif b == a:
    print(f"{b} es igual a {a}")
else:
    print("Ha ocurrido un error inesperado.")