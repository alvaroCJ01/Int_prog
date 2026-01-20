diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}
palabra=input("Introduce una palabra: ")

if palabra in diccionario:
    print (diccionario[palabra])
else:
    print("La palabra no está en la lista.")