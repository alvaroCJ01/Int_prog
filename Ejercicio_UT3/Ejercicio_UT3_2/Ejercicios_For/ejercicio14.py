total=0
for i in  range(10):
    total=(i+1)*10+total
    print(f"En el mes {i+1} pagó {(i+1)*10}€")
print(f"Al final habrá pagado un total de {total}€")