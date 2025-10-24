a=float(input("Introduzca el valor del primer lado: "))
b=float(input("Introduzca el valor del segundo lado: "))
c=float(input("Introduzca el valor del tercer lado: "))


if a**2+b**2==c**2:
    print("El triángulo es rectángulo.")
elif a==b or b==c or c==a:
    print("El triángulo es isósceles.")
elif a==b and b==c:
    print("El triángulo es equilátero.")
else:
    print("El triángulo es escaleno.")