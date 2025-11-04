import shutil
from pathlib import Path
ruta = Path('.')
conf = ruta / 'config.ini'
conf2 = ruta / 'config.example.ini'
if not conf.exists():
    if not conf2.exists():
        print("Falta el archivo de ejemplo.")
    else:
        print("Copiando archivo...")
        shutil.copy("config.example.ini","config.ini")
else:
    print("Config existente.")
