from administrativo import Administrativo
from desarollador import Desarollador
from generente import Gerente

def main():
    administrativo=Administrativo('daniel','3456',100)
    print(administrativo)
    print(administrativo.salario)
    
    desarollador=Desarollador('andres','6400',1100)
    print(desarollador)
    print(desarollador.calcular_bonificacion())
    
    gerente=Gerente('sebastian','3435',2000)
    print(gerente)
    print(gerente.calcular_bonificacion())
    
if __name__=="__main__":
    main()