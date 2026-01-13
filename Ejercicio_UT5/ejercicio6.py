mes=int(input("Introduce un mes (1-12): "))
meses_31=[1,3,5,7,8,10,12]
meses_30=[4,6,9,11]
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

while mes < 13 and mes > 0:
    if mes in meses_31:
        print(f"{meses[mes-1]} tiene 31 dias.")
    elif mes in meses_30:
        print(f"{meses[mes-1]} tiene 30 dias.")
    else:
        print("Febrero tiene 28 dias.")
    break