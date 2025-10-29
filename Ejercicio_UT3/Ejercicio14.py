tipo=input("Introduce el tipo de uva:(A/B) ")
tamaño=int(input("Introduce el tamaño:(1/2) "))
precio=float(input("Introduce el precio de la uva: "))
cantidad=float(input("Introduce la cantidad de kilos: "))

if tipo == "A":
    if tamaño == 1:
        sumar=0.20
    elif tamaño == 2:
        sumar=0.30
elif tipo == "B":
    if tamaño == 1:
        sumar=-0.30
    elif tamaño == 2:
        sumar=-0.50

precio_final=precio+sumar
total=precio_final*cantidad
print(f"Este es el total: {total}€")