import sys
from pathlib import Path

if len(sys.argv) == 2:
    q = Path(sys.argv[1])
    if q.stat().st_size >= 1048576:
        print("GRANDE")
    else:
        print("PEQUEÑO")
else:
    print("Introduzca un parámetro.")