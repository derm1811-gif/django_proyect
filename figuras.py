class figura:
    def __init__(self,largo):
        self.largo=largo
        
class cuadrado(figura):
    def calcular_area(self):
        print(self.largo*self.largo)
        
    def calcualr_perimetro(self):
        print(self.largo*4)
        
class circulo(figura):
    def calcular_area(self):
        print(3.1416*self.largo*self.largo)
        
    def calcualr_perimetro(self):
        print(2*31416*self.largo)
        

cuadrado1=cuadrado(2)
cuadrado1.calcular_area()
cuadrado1.calcualr_perimetro()

circulo1=circulo(2)
circulo1.calcular_area()
circulo1.calcualr_perimetro()