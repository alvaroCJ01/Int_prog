hora=int(input("Hora de salida: "))
minutos=int(input("Minutos de salida: "))
segundos=int(input("Segundos de salida: "))
t=int(input("segundos que tarda en llegar: "))

segundos3=(hora*3600)+(minutos*60)+segundos
segundos2=segundos3+t
hora_ll=(segundos2//3600)%24
minutos_ll=(segundos2 % 3600)//60
segundos_ll=(segundos2 % 3600)%60

print(f"El ciclista llegará a las {hora_ll}h {minutos_ll}min {segundos_ll}s")