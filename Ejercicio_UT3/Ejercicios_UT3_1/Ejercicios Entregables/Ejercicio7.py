from datetime import datetime

a = datetime.now().weekday()
if a == 5 or a == 6:
    print("Ventana de matenimiento.")