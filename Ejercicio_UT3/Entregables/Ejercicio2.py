from datetime import datetime,timedelta

hoy = datetime.now().hour

if hoy < 12:
    print("Backup de mañana")
elif hoy < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")