nombre=input("Introduzca el nombre del alumno: ")
nombres=[]
edades=[]
while nombre != "*":
    edad=int(input("Introduzcla la edad del alumno: "))
    nombres.append(nombre)
    edades.append(edad)
    nombre=input("Introduzca el nombre del alumno: ")

edades_max=max(edades)

print("Mayores de edad:")
for nombre2,edad2 in zip(nombres,edades):
    if edad2 >= 18:
        print(nombre2,edad2)

print("Mas mayores:")
for nombre2,edad2 in zip(nombres,edades):
    if edad2 == edades_max:
        print(nombre2,edad2)