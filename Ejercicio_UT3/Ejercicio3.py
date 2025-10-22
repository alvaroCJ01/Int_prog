a=int(input("Introduzca un numero: "))

if a%2 == 0:
    print(f"{a} es par")
elif a%2 != 0:
    print(f"{a} es impar")
else:
    print("Ha ocurrido un error inesperado")