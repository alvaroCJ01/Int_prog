import modulo_alvaro

# Ejercicio 1
print("Ejercicio 1: Función mayor(n1, n2) que recibe dos números n1 y n2 y devuelve el mayor.")
print("Valores probados: 1, 2 | Salida esperada: 2")
print(modulo_alvaro.mayor(1, 2))

# Ejercicio 3
print("\nEjercicio 3: Función es_par(n) que recibe un número n y devuelve un booleano indicando si el número es par o no.")
print("Valor probado: 2 | Salida esperada: True")
print(modulo_alvaro.es_par(2))

# Ejercicio 6
print("\nEjercicio 6: Función es_mayusculas(cad) que recibe la cadena cad y devuelve un booleano indicando si la cadena está toda en mayúsculas o no.")
print('Valor probado: "ASDAD" | Salida esperada: True')
print(modulo_alvaro.es_mayusculas("ASDAD"))

# Ejercicio 7
print("\nEjercicio 7: Función potencia(base, exp) que recibe dos números, la base y un exponente exp y devuelve la potencia calculada.")
print("Valores probados: 2, 2 | Salida esperada: 4")
print(modulo_alvaro.potencia(2, 2))

# Ejercicio 9
print("\nEjercicio 9: Función ordena_mayor_menor(n1, n2, n3) que recibe tres números y devuelve una tupla con los números ordenados de mayor a menor.")
print("Valores probados: 2, 3, 4 | Salida esperada: [4, 3, 2]")
print(modulo_alvaro.ordena_mayor_menor(2, 3, 4))

# Ejercicio 10
print("\nEjercicio 10: Función clasifica_circunferencias(x1, y1, r1, x2, y2, r2) que recibe los centros y radios de dos circunferencias y las clasifica en exteriores, tangentes exteriores, secantes, tangentes interiores, interiores o concéntricas. No devuelve nada, solo imprime el tipo.")
print("Valores probados: (1,1,1) y (2,2,2) | Salida esperada: Las circunferencias son secantes")
modulo_alvaro.clasifica_circunferencias(1, 1, 1, 2, 2, 2)

# Ejercicio 11
print("\nEjercicio 11: Función clasifica_triangulo(a, b, c) que recibe la longitud de los tres lados de un triángulo e imprime el tipo de triángulo.")
print("Valores probados: 1, 2, 3 | Salida esperada: Triángulo escaleno, no es rectángulo")
modulo_alvaro.clasifica_triangulo(1, 2, 3)

# Ejercicio 12
print("\nEjercicio 12: Función es_bisiesto(anyo) que recibe un año y devuelve un booleano indicando si es bisiesto o no.")
print("Valor probado: 300 | Salida esperada: False")
print(modulo_alvaro.es_bisiesto(300))

# Ejercicio 13
print("\nEjercicio 13: Función es_fecha_correcta(dia, mes, anyo) que recibe el día, el mes y el año y devuelve un booleano indicando si la fecha es correcta.")
print("Valores probados: 20, 10, 200 | Salida esperada: True")
print(modulo_alvaro.es_fecha_correcta(20, 10, 200))

# Ejercicio 14
print("\nEjercicio 14: Función calcula_ganancias_uva(precio_kilo, kilos, tipo, tamanyo) que recibe el precio por kilo, la cantidad de kilos, el tipo y el tamaño de la uva y devuelve las ganancias del vinicultor.")
print('Valores probados: 10, 10, "A", 2 | Salida esperada: 103')
print(modulo_alvaro.calcula_ganancias_uva(10, 10, 2, "A"))

# Ejercicio 15
print("\nEjercicio 15: Función costes_viaje(n) que recibe el número de alumnos y devuelve una tupla con el coste por alumno y el coste total del autobús.")
print("Valor probado: 20 | Salida esperada: 142.5, 2850")
print(modulo_alvaro.costes_viaje(20))

# Ejercicio 16
print("\nEjercicio 16: Función coste_llamada(tiempo, es_domingo, turno) que recibe el tiempo de la llamada, si es domingo y el turno, y devuelve el coste de la llamada.")
print('Valores probados: 20, "S", "T" | Salida esperada: 1421.4')
print(modulo_alvaro.coste_llamada(20, "S", "T"))

# Ejercicio 18
print("\nEjercicio 18: Función dia_escrito(n) que recibe un número del 1 al 7 y devuelve el día de la semana escrito.")
print("Valor probado: 2 | Salida esperada: Martes")
print(modulo_alvaro.dia_escrito(2))

# Ejercicio 19
print("\nEjercicio 19: Función num_dias_mes(mes) que recibe un número de mes y devuelve el número de días que tiene.")
print("Valor probado: 2 | Salida esperada: 28 o 29 días")
print(modulo_alvaro.num_dias_mes(2))

# Ejercicio 20
print("\nEjercicio 20: Función calcula_coste_transporte(peso, zona) que recibe el peso en gramos y la zona y devuelve el coste del transporte.")
print("Valores probados: 100, 1 | Salida esperada: 24")
print(modulo_alvaro.calcula_coste_transporte(100, 1))

# Ejercicio bucles 1
print("\nEjercicio bucles 1: Función factorial(num) que recibe un número entero y devuelve su factorial.")
print("Valor probado: 2 | Salida esperada: 2")
print(modulo_alvaro.factorial(2))

# Ejercicio bucles 5
print("\nEjercicio bucles 5: Función pares_entre(num1, num2) que recibe dos números e imprime los pares entre ellos incluidos.")
print("Valores probados: 1, 3 | Salida esperada: 2")
print(modulo_alvaro.pares_entre(1, 3))

# Ejercicio bucles 6
print("\nEjercicio bucles 6: Función tabla_multiplicar(n) que imprime la tabla de multiplicar de un número.")
print("Valor probado: 10 | Salida esperada: Tabla del 10")
modulo_alvaro.tabla_multiplicar(10)

# Ejercicio bucles 10
print("\nEjercicio bucles 10: Función adivina_numero(intentos) que permite adivinar un número del 1 al 100 con un número limitado de intentos.")
print("Valor probado: 2 | Salida esperada: Minijuego con 2 intentos")
modulo_alvaro.adivina_numero(2)

# Ejercicio bucles 11
print("\nEjercicio bucles 11: Función es_primo(n) que recibe un número entero y devuelve si es primo o no.")
print("Valor probado: 7 | Salida esperada: Primo")
modulo_alvaro.es_primo(7)

# Ejercicio bucles 20
print("\nEjercicio bucles 20: Función primeros_primos(N) que recibe la cantidad de números primos a mostrar e imprime los N primeros.")
print("Valor probado: 2 | Salida esperada: 2, 3")
modulo_alvaro.primeros_primos(2)