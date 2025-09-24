#Pide la edad actual al usuario. Calcula cuántos años tendrá en 2030 y muéstralo.
edad_us = input("Cual es tu edad: ")
import datetime
fecha=datetime.date.today()
año=int(fecha.strftime("%Y"))
edad_fut=(2030-año)+int(edad_us)
print(f"Tu edad en 2030 será {edad_fut}")