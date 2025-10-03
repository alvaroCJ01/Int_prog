correctas=int(input("Introduce las respuestas correctas: "))
incorrectas=int(input("Introduce las respuestas incorrectas: "))
blanco=int(input("Introduce las respuestas en blanco: "))

puntos_cor=correctas*5
puntos_in=incorrectas*-1
final=puntos_cor+puntos_in

print(f"Tu nota final es: {final}")