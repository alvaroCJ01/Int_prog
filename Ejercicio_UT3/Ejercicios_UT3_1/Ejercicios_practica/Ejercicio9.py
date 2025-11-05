a=int(input("Introduzca un numero: "))
b=int(input("Introduzca un numero: "))
c=int(input("Introduzca un numero: "))

if a > b and a > c:
    if b > c:
        print (f"{a},{b},{c}")
    elif c > b:
        print (f"{a},{c},{b}")
    else: 
        print (f"{a},{b},{c}")
elif b > a and b > c:
    if a > c:
        print (f"{b},{a},{c}")
    elif c > a:
        print (f"{b},{c},{a}")
    else: 
        print (f"{b},{a},{c}")
elif c > a and c > b:
    if a > b:
        print (f"{c},{a},{b}")
    elif b > a:
        print (f"{c},{b},{a}")
    else: 
        print (f"{c},{a},{b}")
else:
    print("Ha ocurrido un error inesperado.")