def mayor(n1,n2):
    if n1 > n2:
        return n2
    else:
        return n1
    
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def es_mayusculas(cad):
    if str(cad).isupper():
        return True
    else:
        return False
    

def potencia(base,exp):
    return base ** exp

def ordena_mayor_menor(a,b,c):
    if a > b and a > c:
        if b > c:
            return a,b,c
        elif c > b:
            return a,c,b
        else: 
            return a,b,c
    elif b > a and b > c:
        if a > c:
            return b,a,c
        elif c > a:
            return b,c,a
        else: 
            return b,a,c
    elif c > a and c > b:
        if a > b:
            return c,a,b
        elif b > a:
            return c,b,a
        else: 
            return c,a,b

def clasifica_circunferencias(x1,y1,r1,x2,y2,r2):
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    sr= r1+r2
    dr=abs(r1-r2)

    if d>sr:
        print("Las circunferencias son exteriores.")
    elif d==sr:
        print("Las circunferencias son tangentes exteriores.")
    elif dr < d < sr:
        print("Las circunferencias son secantes.")
    elif d == dr:
        print("Las circunferencias son tengentes interiores.")
    elif d < dr:
        print("Las circunferencias son interiores.")
    elif d == 0 and r1 == r2:
        print("Las circunferencias son identicas.")
    elif d == 0 and r1 != r2:
        print("Las circunferencias son cóncavas.")
    else:
        print("Ha ocurrido un error inesperado.")

def clasifica_triangulo(a,b,c):
    if a==b==c:
        print("El triángulo es equilátero.")
    elif a==b or b==c or c==a:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

    if a**2+b**2==c**2 or c**2+b**2==a**2 or a**2+c**2==b**2:
        print("El triángulo es rectángulo.")
    else:
        print("No es rectangualo")

def es_bisiesto(anyo):
    if anyo%4 == 0:
        if anyo%100 == 0 and anyo%400 == 0:
            return True
        elif anyo%100 != 0:
            return True
        elif anyo%100 == 0 and anyo%400 != 0:
            return False
    else:
        return False

def es_fecha_correcta(dia,mes,anyo):
    if (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
        return False
    else:
        if mes == 2:
            if dia > 29:
                return False
            elif dia == 29:
                if (anyo%4 == 0 and anyo%100 != 0) or (anyo%400 == 0):
                    return True
                else:
                    return False
            elif dia > 28:
                return False
            else:
                return True
        elif mes in[4,6,9,11] and dia > 30:
            return False
        else:
            return True
        
def calcula_ganancias_uva(precio_kilo,kilos,tamano,tipo):
    if tipo == "A":
        if tamano == 1:
            sumar=0.20
        elif tamano == 2:
            sumar=0.30
    elif tipo == "B":
        if tamano == 1:
            sumar=-0.30
        elif tamano == 2:
            sumar=-0.50

    precio_final=precio_kilo+sumar
    total=precio_final*kilos
    return total
print(calcula_ganancias_uva(10,2,2,'A'))

def costes_viaje(num_alumno):
    if num_alumno >= 100:
        b = num_alumno * 65
        return 65,b
    elif num_alumno >=50 and num_alumno < 100:
        c = num_alumno * 70
        return 70,c
    elif num_alumno >=30 and num_alumno < 50:
        d = num_alumno * 95
        return 95,d
    else:
        e = 2850/num_alumno
        return e,2850

def coste_llamada(tiempo,es_domingo,turno):

    if tiempo <= 5:
        coste = tiempo * 100
    elif tiempo <= 8:
        coste = (tiempo - 5) * 80 + 500
    elif tiempo <= 10:
        coste = (tiempo - 8) * 70 + 240 + 500
    else:
        coste = (tiempo - 10) * 50 + 140 + 240 + 500
    if es_domingo == "S":
        coste += coste * 0.03
    else:
        if turno == "M":
            coste += coste * 0.15
        elif turno == "T":
            coste += coste * 0.10
    return coste

def dia_escrito(num_dia):
    if  num_dia == 1:
        return "Lunes"
    elif  num_dia == 2:
        return "Martes"
    elif  num_dia == 3:
        return "Miércoles"
    elif  num_dia == 4:
        return "Jueves"
    elif  num_dia == 5:
        return "Viernes"
    elif  num_dia == 6:
        return "Sábado"
    elif  num_dia == 7:
        return "Domingo"

def num_dias_mes(mes):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return "31 días"
    elif mes == 2:
        return "28 o 29 días"
    elif mes in [4, 6, 9, 11]:
        return "30 días"
    
def calcula_coste_transporte(peso,zona):
    if peso > 0 and peso <= 5000:
        if zona == 1:
            return peso * 24 / 100
        elif zona == 2:
            return peso * 20 / 100
        elif zona == 3:
            return peso * 21 / 100
        elif zona == 4:
            return peso * 10 / 100
        elif zona == 5:
            return peso * 18 / 100

def factorial(num):
    b=num
    for i in range(1,num):
       b=b*i
    return b

def pares_entre(num1,num2):
    for i in range(num1,num2):
        if i % 2 == 0:
            print(i)

def tabla_multiplicar(num_mult):
    print(f"============== TABLA DE MULTIPLICAR DEL {num_mult} ==============")
    for i in range(1,11):
        print(f"\t\t     {i} x {num_mult} = {num_mult*i}")

def adivina_numero(intentos):
    import random
    numero=random.randint(1,100)
    print("Bienvenido al juego de adivinar el numero.")
    print(f"Tienes un total de {intentos} intentos.")

    while True:
        res=int(input("Introduzca un numero: "))
        if numero == res:
            print(f"Has ganado el numero era {numero}.")
            break
        else:
            intentos=intentos-1
            if intentos > 0:
                print(f"Vuelve a intentarlo, te quedan {intentos} intentos.")
            else:
                print(f" Has perdido el numero ganador era: {numero}")
                break
    
def es_primo(num_primo):
    contador=0
    for i in range(1,num_primo+1):
        if num_primo%i==0:
            contador += 1
    else:
        if contador==2:
            print("Primo")
        else:
            print("No es primo")

def prineros_primos(num_prim_prim):
    contador = 0
    for i in range(100000000000000000000000000000000000000000000000):
        if contador == num_prim_prim:
            break
        if i % 2:
            print(i)
            contador+=1
prineros_primos(6)