lista=[]
while True:
    print("\nGestión de Lista de la Compra") 
    print("1. Mostrar la lista") 
    print("2. Añadir elementos a la lista") 
    print("3. Borrar elementos de la lista") 
    print("4. Contar elementos de la lista") 
    print("5. Añadir una lista de elementos a la ya existente") 
    print("6. Borrar toda la lista") 
    print("7. Salir")
    selec=int(input("Introduzca su opción: "))
    match selec:
        case 1:
            print("Lista de la compra: ")
            if len(lista) == 0:
                print("La lista está vacia.")
            else:
                for producto in lista:
                    print(producto)
        case 2:
            agr=input("Elemento a añadir: ")
            lista.append(agr)
            print("Elemento añadido.")
        case 3:
            elim=input("Que elemento quieres borrar: ")
            if elim in lista:
                lista.remove(elim)
                print("Elemento eliminado.")
            else:
                print("El elemento no existe.")
        case 4:
            print(f"Llevas {lista.count()} elementos en la lista.")
        case 5:
            nueva_lista=input("Introduce la lista a añadir, (separado por comas): ")
            lista2=nueva_lista.split(',')
            lista.extend(lista2)
        case 6:
            print("Borrando lista...")
            lista.clear()
        case 7:
            print("Saliendo...")
            break
        case _:
            print("La opción introducida no es válidia.")