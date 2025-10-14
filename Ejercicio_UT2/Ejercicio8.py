import random
nombre=' Ana '
apellido=' López '
nombre=nombre.strip()
apellido=apellido.strip()
for a, b in zip("áéíóúÁÉÍÓÚ", "aeiouAEIOU"):
    nombre = nombre.replace(a, b)
    apellido = apellido.replace(a, b)
prim_part=nombre[:3]
seg_part=apellido[:3]
terc_part=random.randrange(0,100)
print(f"Usuario: {prim_part}{seg_part}{terc_part}")
