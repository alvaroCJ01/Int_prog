a=float(input("Introduzca el valor del primer lado: "))
b=float(input("Introduzca el valor del segundo lado: "))
c=float(input("Introduzca el valor del tercer lado: "))


if a==b==c:
    print("El triángulo es equilátero.")
elif a==b or b==c or c==a:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")

if a**2+b**2==c**2 or c**2+b**2==a**2 or a**2+c**2==b**2:
    print("El triángulo es rectángulo.")
else:
    print("No es rectangualo")