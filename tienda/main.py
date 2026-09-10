from perecedero import Perecedero
from no_perecedero import No_perecedero

def main():
    perecedero1=Perecedero(1,"Leche",10,"2024-06-30")
    perecedero1.aumentar_stock(5)
    print(perecedero1.stock)
    perecedero1.disminuir_stock(3)
    print(perecedero1.stock)
    
    no_perecedero1=No_perecedero(2,"Arroz",20)
    no_perecedero1.aumentar_stock(10)
    print(no_perecedero1.stock)
    
main() 