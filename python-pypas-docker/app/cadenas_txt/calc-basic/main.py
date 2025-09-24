def run():
    # TODO
    x = input('Introduzca un número: ')
    y = input('Introduzca otro número: ')
    x = int(x)
    y = int(y)
    suma = x + y
    resta = x - y
    division = x / y
    multiplicacion = x * y
    print(x , '+', y, '=', suma)
    print(x , '-', y, '=', resta)
    print(x , '*', y, '=', multiplicacion)
    print(x , '/', y, '=', division)
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
