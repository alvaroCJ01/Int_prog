palabra=input("Introduzca una palabra: ")
diccionario_palabra={}
for letra in palabra:
    if letra not in diccionario_palabra:
        diccionario_palabra[letra]=1
    else:
        diccionario_palabra[letra]+=1
print(diccionario_palabra)