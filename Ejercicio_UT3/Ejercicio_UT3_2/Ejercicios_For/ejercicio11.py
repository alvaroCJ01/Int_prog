num=int(input("Introduzca un numero: "))
contador=0
for i in range(1,num+1):
    if num%i==0:
        contador += 1
else:
    if contador==2:
        print("Primo")
    else:
        print("No es primo")