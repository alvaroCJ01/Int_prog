cad="PC-AULA-23"
print(cad.startswith("PC-"))
a=cad.find("AULA")
b=cad.find("23")
print(cad[a:b-1])
print(cad[b:])