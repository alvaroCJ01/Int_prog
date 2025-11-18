print("1. Entrar\n2. Opciones\n3. Sistema\n4. Salir")
while True:
    opt=int(input("Introduzca la opción a elegir: "))
    if opt not in range(1,5):
        continue
    elif opt == 4:
        print("Saliendo...")
        break
    if opt== 1:
        print("Has elegido la opcion 1.")
    elif opt == 2:
        print("Has elegido la opcion 2.")
    elif opt == 3:
        print("Has elegido la opción 3.")