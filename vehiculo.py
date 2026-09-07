class vehicle:
    def __init__(self,plate,color,brand):
        self.plate=plate
        self.color=color
        self.brand=brand
        
    def mover(self):
        print("el vehiculo se mueve")
        
class car(vehicle):#herencia
    pass

class Motorbike(vehicle):
    def desplegar_gato(self):
        print("Gato desplegado")

car1=car('6767','Black','ferrari')
car1.mover()

motorbike=Motorbike('89898','green','nkd')
motorbike.mover()
motorbike.desplegar_gato()
