from producto import Producto 

class Perecedero(Producto):
    
    
    def __init__(self,id,nombre,stock,fecha_caducidad):
        super().__init__(id,nombre,stock)
        self.fecha_caducidad=fecha_caducidad