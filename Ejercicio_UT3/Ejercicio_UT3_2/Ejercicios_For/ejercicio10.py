import random
numero=random.randint(1,100)
print(numero)
intentos = 10
print("Bienvenido al juego de adivinar el numero.")
print(f"Tienes un total de {intentos} intentos.")

for _ in range(1000000000000000000000000000000000000000000):
    res=int(input("Introduzca un numero: "))
    if numero == res:
        print(f"Has ganado el numero era {numero}.")
        break
    else:
        intentos=intentos-1
        if intentos > 0:
            print(f"Vuelve a intentarlo, te quedan {intentos} intentos.")
        else:
            print(f" Has perdido el numero ganador era: {numero}")
            break