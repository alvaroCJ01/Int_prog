diccionario_vacio={}
clave=""
valor=""
for i in range(0,3):
    par=input("Introduce un par clave,valor: ")
    clave,valor = par.split(',')
    diccionario_vacio [clave] = valor

print (diccionario_vacio)