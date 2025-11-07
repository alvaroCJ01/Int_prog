iteracion=1
num1=int(input("Introduce un numero: "))
print(f"============ TABLA DEL {num1} ============")
while iteracion <= 10:
    num2=num1*iteracion
    print(f"{iteracion} x {num1} = {num2}")
    iteracion= iteracion+1