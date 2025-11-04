import sys
import shutil

if len(sys.argv) == 2:
    uso = int(sys.argv[1])
else:
    print("No se ha introducido un parámetro, usando valor por defecto: 85")
    uso = 85
    a=shutil.disk_usage(path='/').total
    b=shutil.disk_usage(path='/').used
    #Obtener porcentaje de uso del disco
    c=b/a*100
    if c >= uso:
        print("ALERTA")
    else:
        print("OK")