import random
lista_numeros=[0]*10

for i in range(len(lista_numeros)):
    x=random.randint(1,10)
    lista_numeros[i]=x

for i in range(len(lista_numeros)):
    print(f"{lista_numeros[i]},{lista_numeros[i]**2},{lista_numeros[i]**3}")