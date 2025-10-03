x1=int(input("Pasame el valor de x en el primer punto: "))
x2=int(input("Pasame el valor de x en el segundo punto: "))
y1=int(input("Pasame el valor de y en el primer punto: "))
y2=int(input("Pasame el valor de y en el segundo punto: "))

distancia=round((((x2-x1)**2+(y2-y1)**2)**0.5),2)
print(f"La distancia entre los valores es: {distancia}")