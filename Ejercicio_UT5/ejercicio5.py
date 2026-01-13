import random
lista=[]
for _ in range(10):
    lista.append(random.randint(0,9))

lista_ordenada=sorted(lista)
print("Lista desordenada: ",lista)
print("Lista ordenada: ",lista_ordenada)