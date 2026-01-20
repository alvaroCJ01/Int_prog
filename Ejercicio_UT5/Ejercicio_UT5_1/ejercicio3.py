notas=[0.0]*5
for i in range(5):
    x=float(input("Introduce tu nota:"))
    if x < 0 or x > 10:
        print("Has introducido un valor que no entra en los parametro establecidos, 0-10")
        break
    notas[i]=x

for i in range(5):
    print(f"Nota {i+1}: {notas[i]}")

media=sum(notas)/len(notas)
nota_alta=max(notas)
nota_baja=min(notas)
print(f"Tu media es: {media} \n Tu nota más alta ha sido: {nota_alta}\n Tu nota más baja ha sido: {nota_baja}")