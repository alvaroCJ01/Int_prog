num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero: "))

if num1 > num2 :
    while num1 >= num2:
        if num2 % 2 == 0:
            print(num2)
        num2 = num2 + 1
else:
    while num1 <= num2:
        if num1 % 2 == 0:
            print(num1)
        num1 = num1 + 1
