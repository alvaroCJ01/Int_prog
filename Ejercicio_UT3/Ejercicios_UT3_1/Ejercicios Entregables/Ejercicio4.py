import sys

if len(sys.argv) == 2:
    hostname=sys.argv[1]
    if len(hostname) > 6 and hostname[:3] == "PC-":
        print("VÁLIDO")
    else:
        print("NO VÁLIDO")
else:
    print("Introduzca un parámetro")