from abc import ABC , abstractmethod

class Figura:
    def __init__(self,longitud):
        self.longitud=longitud
        
    @abstractmethod
    def calcularVolumen():
        pass
    
    def mostrarResultado():
        pass
