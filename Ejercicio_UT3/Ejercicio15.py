a=int(input("Introduce el numero de alumnos que quieren realiza el viaje: "))

if a >= 100:
    b = a * 65
    print(f"Los alumnos deberán pagar 65€ y deberá pagar un total de {b}€")
elif a >=50 and a < 100:
    c = a * 70
    print(f"Los alummnos deberán pagar 70€ y deberá pagar un total de {c}€")
elif a >=30 and a < 50:
    d = a * 95
    print(f"Los alumnos deberán pagar 95€ y deberá pagar un total de {d}€")
else:
    e = 2850/a
    print(f"Los alumnos deberán pagar cada uno {e}€ y deberá pagar un total de 2850€")