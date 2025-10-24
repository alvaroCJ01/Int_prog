dia=int(input("Introduzca el dia deseado: "))
mes=int(input("Introduzca el mes deseado: "))
año=int(input("Introduzca el año deseado: "))

if (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
    print("El dia o el mes son incorrectos.")
else:
    if mes == 2:
        if dia > 29:
            print("La fecha es incorrecta, febrero no tiene tantos dias.")
        elif dia == 29:
            if (año%4 == 0 and año%100 != 0) or (año%400 == 0):
                print("La fecha es correcta.")
            else:
                print("La fecha es incorrecta.")
        elif dia > 28:
            print("La fecha es incorrecta, febrero tiene 28 dias.")
        else:
            print("La fecha es correcta")
    elif mes in[4,6,9,11] and dia > 30:
        print("El dia es incorrecto, el mes no tiene 31 dias.")
    else:
        print("La fecha es correcta.")