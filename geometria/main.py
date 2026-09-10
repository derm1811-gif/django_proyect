from esfera import Esfera
from cilindro import Cilindro
from cubo import Cubo

def main():
    esfera=Esfera(30)
    esfera.calcularVolumen()
    print(esfera.calcularVolumen())
    
    cilindro=Cilindro(30,10)
    cilindro.calcularVolumen()
    print(cilindro.calcularVolumen())
    
    cubo=Cubo(30)
    cubo.calcularVolumen()
    print(cubo.calcularVolumen())

main()