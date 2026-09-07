from empresa.empleado import empleado

class Gerente(empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.20