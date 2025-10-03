euros2=int(input("Cuantas monedas de 2 euros tienes?: "))
euros1=int(input("Cuantas monedas de 1 euro tienes?: "))
cent50=int(input("Cuantas monedas de 50 centimos tienes?: "))
cent20=int(input("Cuantas monedas de 20 centimos tienes?: "))
cent10=int(input("Cuantas monedas de 10 centimos tienes?: "))

c_e2=euros2*200
c_e1=euros1*100
c_c50=cent50*50
c_c20=cent20*20
c_c10=cent10*10

total_c=c_e2+c_e1+c_c10+c_c20+c_c50
euros_t=total_c//100
cent_t=total_c%100
print(f"Tienes {euros_t},{cent_t}€")