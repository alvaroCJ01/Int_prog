x1=float(input("Introduzca el primer valor de x: "))
x2=float(input("Introduzca el segundo valor de x: "))
y1=float(input("Introduzca el primer valor de y: "))
y2=float(input("Introduzca el segundo valor de y: "))
r1=float(input("Introduzca el radio de la primera circunferencia: "))
r2=float(input("Introduzca el radio de la segunda circunferencia: "))
d=((x2-x1)**2+(y2-y1)**2)**0.5
sr= r1+r2
dr=abs(r1-r2)

if d>sr:
    print("Las circunferencias son exteriores.")
elif d==sr:
    print("Las circunferencias son tangentes exteriores.")
elif dr < d < sr:
    print("Las circunferencias son secantes.")
elif d == dr:
    print("Las circunferencias son tengentes interiores.")
elif d < dr:
    print("Las circunferencias son interiores.")
elif d == 0 and r1 == r2:
    print("Las circunferencias son identicas.")
elif d == 0 and r1 != r2:
    print("Las circunferencias son cóncavas.")
else:
    print("Ha ocurrido un error inesperado.")