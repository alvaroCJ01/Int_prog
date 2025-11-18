lim_in=int(input("Introduzca el limite inferior: "))
lim_sup=int(input("Introduzca el limite superior: "))
es_in=int(0) 
en_in=int(0)
no_in=int(0)
while True:
    num=int(input("Introduzca los numeros a comprobar: "))
    if num == 0:
        print("Saliendo...")
        break
    if num == lim_in or num == lim_sup:
        es_in+=1
    elif num in range(lim_in,lim_sup):
        en_in+=1
    else:
        no_in+=1
print(f"Has introducido {en_in} numeros dentro del intervalo.")
print(f"Has introducido {no_in} numeros fuera del intervalo.")
print(f"Has introducido {es_in} numeros en el limite del intervalo.")