from figura import Figura

class Esfera(Figura):
    def calcularVolumen(self):
        volumen= 4/3 * 3.1416 * (self.longitud * self.longitud * self.longitud)
        return volumen