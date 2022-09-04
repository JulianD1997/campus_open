def suma(a,b,c):
    return a+b+c

print(suma(4,8,32))

class Coche:
    def __init__(self):
        self.puertas = 0
    def agregar_puertas(self,puertas):
        self.puertas += puertas
mi_coche = Coche()
mi_coche.agregar_puertas(6)
print("Puertas totales : ",mi_coche.puertas)