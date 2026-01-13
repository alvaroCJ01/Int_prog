lista1=[]
for i in range(5):
    lista1[i]=input(f"Introduce un valor para añadir a la lista ({i+1}/5)")

lista2=lista1[::-1]
print(lista2)