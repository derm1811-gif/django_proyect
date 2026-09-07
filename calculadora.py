class calculadora:
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: No se puede dividir entre cero"
        
calculadora1=calculadora(10,5)
print(calculadora1.sumar())
print(calculadora1.restar())
print(calculadora1.multiplicar())
print(calculadora1.dividir())
