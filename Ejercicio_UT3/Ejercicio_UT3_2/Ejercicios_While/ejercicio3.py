iteraciones=int(input("Cuantos numeros quiere introducir?: "))
cont_pos=0
cont_neg=0
cont_ig=0
while iteraciones > 0:
    numero=float(input("Introduzca un número: "))
    if numero > 0:
        cont_pos=cont_pos+1
    elif numero < 0:
        cont_neg=cont_neg+1
    else:
        cont_ig=cont_ig+1
    iteraciones=iteraciones-1
print(f"Se han introducido {cont_pos} numeros mayores que 0")
print(f"Se han introducido {cont_neg} numeros menores que 0.")
print(f"Se han introducido {cont_ig} numeros iguales a 0.")
