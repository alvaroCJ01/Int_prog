import sys
import shutil

if len(sys.argv) != 1:
    uso = int(sys.argv[1])
    a=shutil.disk_usage(path='/').total
    b=shutil.disk_usage(path='/').used
    #Obtener porcentaje de uso del disco
    c=b/a*100
    if c >= uso:
        print("ALERTA")
    else:
        print("OK")
else:
    print("Introduzca algún argumento.")