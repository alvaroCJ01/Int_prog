n1 = int(input("Introduzca un número entero: "))
resultado=n1
while n1 > 1 :
    n1 = n1-1
    resultado= resultado * n1
print(f"El resultado del factorial es: {resultado}")