c=0
b=0
for _ in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    a=int(input("Introduzca un numero: "))
    c=a+c
    if a == 0:
        break
    b=b+1

print(f"La suma de los numeros es {c}")
print(f"La media de los numeros es {c/b}")