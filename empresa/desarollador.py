from empresa.empleado import empleado

class Desarollador(empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.15