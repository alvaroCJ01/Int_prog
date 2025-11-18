class coche:

    def __init__(self, marca, modelo, color, matricula):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula

    def sonido(self):
        print("Brooom")

mi_coche = coche("Toyota", "Corola", "rojo", "2345BBB")

mi_coche.sonido()
