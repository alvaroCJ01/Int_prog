from pathlib import Path
import os

paths=Path.cwd()
contenido=os.listdir(path=paths)
print(paths)
print(contenido)

if 'logs' not in os.listdir('.'):
    os.mkdir('logs')
    print("Carpeta creada")
else:
    print("Carpeta ya existe.")



