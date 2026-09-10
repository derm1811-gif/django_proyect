from abc import ABC , abstractmethod

class Producto:
    def __init__(self,id,nombre,stock):
        self.id=id
        self.nombre=nombre
        self.stock=stock
        

    def aumentar_stock(self,cantidad):
        self.stock+=cantidad
        return self.stock
    
    def disminuir_stock(self,cantidad):
        if cantidad>self.stock:
            print("No hay suficiente stock")
        else:
            self.stock-=cantidad
        return self.stock
