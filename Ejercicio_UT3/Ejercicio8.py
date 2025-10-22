nota=int(input("Introduzca la nota: "))
edad=int(input("Introduzca la edad: "))
sexo=input("Introduzca su sexo(F/M): ")

if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("ACEPTADA")
    elif sexo == "M":
        print("POSIBLE")
    else:
        print("Introduzca correctamente el campo sexo.")
else:
    print("NO ACEPTADA.")