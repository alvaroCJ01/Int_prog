año=int(input("Introduzca el año deseado: "))

if año%4 == 0:
    if año%100 == 0 and año%400 == 0:
        print("El año es bisiesto.")
    elif año%100 != 0:
        print("El año es bisiesto.")
    elif año%100 == 0 and año%400 != 0:
        print("El año no es bisiesto.")
else:
    print("El año no es bisiesto.")