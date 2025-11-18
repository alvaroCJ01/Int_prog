while True:
    letra=input("Introduce una letra: ")
    if len(letra) != 1:
        print("Error: Introduzca un único carácter.")
        continue
    if letra == " ":
        break
    if letra in 'aeiouAEIOU':
        print("VOCAL")
    else:
        print("NO VOCAL")