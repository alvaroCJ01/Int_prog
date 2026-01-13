lista=[]
while len(lista) < 11:
    x=int(input("Introduzca un numero: "))
    if x < 0:
        break
    lista.append(x)


print(lista)