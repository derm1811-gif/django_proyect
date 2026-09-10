from figura import Figura

class Cilindro(Figura):
    def __init__(self, longitud,altura):
        super().__init__(longitud)
        self.altura=altura
    
    def calcularVolumen(self):
        volumen= 3.1416 * (self.longitud * self.longitud * self.longitud)* self.altura
        return volumen