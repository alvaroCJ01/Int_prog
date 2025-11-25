a=int(input("Introduzca el numero de numeros a introducir: "))
cont_mas=0
cont_menos=0
cont_igual=0
for i in range(a):
    b=float(input("Introduzca un numero: "))
    if b < 0:
        cont_menos=cont_menos+1
    elif b > 0:
        cont_mas=cont_mas+1
    else:
        cont_igual=cont_igual+1

print(f"Has introducido {cont_menos} menores de 0")
print(f"Has introducido {cont_mas} mayores de 0")
print(f"Has introducido {cont_igual} iguales de 0")