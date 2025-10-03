sueldo_base=float(input("Introduzca su salario base: "))
venta1=float(input("Cual es el valor de tu primera venta?: "))
venta2=float(input("Cual es el valor de tu segunda venta?: "))
venta3=float(input("Cual es el valor de tu tercera venta?: "))

com1=venta1*0.1
com2=venta2*0.1
com3=venta3*0.1
total_com=com1+com2+com3
total=total_com+sueldo_base

print(f"Las comisiones para la primera venta sera: {com1}€")
print(f"Las comisiones para la segunda venta sera: {com2}€")
print(f"Las comisiones para la tercera venta sera: {com3}€")
print(f"El total percbido por comisiones será: {total_com}€")
print(f"El total a percibir con el salario base y comisiones será de {total}€")