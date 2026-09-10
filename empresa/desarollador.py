from empleado import empleado

class Desarollador(empleado):
    def __init__(self, nombre, documento, salario,lenguajes_programacion):
        super().__init__(nombre, documento, salario)
        self.lenguajes_programacion=lenguajes_programacion
        
    def calcular_bonificacion(self):
        return self.salario * 0.15
    
    def __str__(self):
        return (f"Desarollador: {self.nombre} lenguajes de programacion: {self.lenguajes_programacion}")