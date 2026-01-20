productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}

productos['huevos'] = 2.0
for productos_nombre,precio in productos.items():
    print(f"{productos_nombre}: {precio}")