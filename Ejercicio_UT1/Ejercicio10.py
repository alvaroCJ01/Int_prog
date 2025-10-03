parcial1=float(input("Cual es tu nota de tu primer parcial?: "))
parcial2=float(input("Cual es tu nota de tu segundo parcial?: "))
parcial3=float(input("Cual es tu nota de tu tercer parcial?: "))
ex_fin=float(input("Cual es la nota de tu examen final?: "))
trab_fin=float(input("Cual es la nota de tu trabajo final?: "))

parc_fin=parcial1+parcial2+parcial3/3
pond_parc=parc_fin*0.55
pond_ex=ex_fin*0.3
pond_trab=trab_fin*0.15

not_fin=pond_ex+pond_parc+pond_trab

print(f"Tu nota final de Algoritmos es: {not_fin}")
