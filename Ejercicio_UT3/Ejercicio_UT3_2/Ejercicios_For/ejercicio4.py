for _ in range(1000000000000000000000000000000000000000000000000):
    letra=input('Introduzca una letra: ')
    if letra in 'aeiouAEIOU':
        print("Vocal")
    elif letra == ' ':
        print("Saliendo...")
        break
    else:
        print("No vocal")