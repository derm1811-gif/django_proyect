from empleado import empleado

class Administrativo(empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.10