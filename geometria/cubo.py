from figura import Figura

class Cubo(Figura):
    def calcularVolumen(self):
        volumen= self.longitud * self.longitud * self.longitud
        return volumen