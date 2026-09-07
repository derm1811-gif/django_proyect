from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self,nombre,documento,salario):
        self.nombre =nombre
        self.documento=documento
        self.salario =salario
        
    @abstractmethod
    def calcular_bonificacion(self):
        pass
    
    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}")
        print(f"Documento:{self.documento}")
        print(f"Salario{self.salario:0.f}")
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Documento: {self.documento}"