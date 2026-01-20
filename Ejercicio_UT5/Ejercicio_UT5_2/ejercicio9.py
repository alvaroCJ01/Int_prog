frase=[]
for i in range(5):
    frase_usuario=input("Introduzca una frase: ")
    frase_usuario=frase_usuario.lower()
    frase2 = frase_usuario.split()

    frase+=frase2

diccionario_palabra={}
for palabra in frase:
    if palabra not in diccionario_palabra:
        diccionario_palabra[palabra]=1
    else:
        diccionario_palabra[palabra]+=1

print(diccionario_palabra)
