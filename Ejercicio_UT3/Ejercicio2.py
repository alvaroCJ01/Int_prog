a=float(input("Introduzca un numero: "))

if a > 0:
    print(f"{a} es positivo")
elif a < 0:
    print(f"{a} es negativo")
elif a == 0:
    print(f"{a} es 0")
else:
    print("Ha ocurrido un error inesperado")