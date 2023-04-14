import pickle
class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0
    
    def __init__(self,color,ruedas,puertas):
    
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self) -> str:
        return f'Mi vehiculo es de color {self.color} y tiene {self.puertas} puertas'
    
car = Vehiculo('Rojo',4,4)
print(car)

fo = open('archivo2.bin','wb')
pickle.dump(car,fo)
fo.close