email='admin.redes@centro.edu'
a=email.find("@")
prim=email[:a]
print(f"Usuario: {prim}")
seg=email[a+1:]
b=seg.find(".")
dom=seg[:b]
print(f"Dominio: {dom}")
tld=seg[b+1:]
print(f"TLD: {tld}")