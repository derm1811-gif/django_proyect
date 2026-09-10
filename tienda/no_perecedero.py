from producto import Producto

class No_perecedero(Producto):
    
    def __init__(self,id,nombre,stock):
        super().__init__(id,nombre,stock)