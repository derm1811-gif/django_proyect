class vehicle:
    def __init__(self,brand,color,plate):
        self.brand=brand
        self.color=color
        self.plate=plate
        self.speed=0
        
    def acelerar(self):
        self.speed+=10
        print(f"el{self.brand} acelero a {self.speed}km/h")
        
    def desacelerar(self):
        self.speed-=10
        print(f"el{self.brand} bajo la velocidad{self.speed}km/h")

#Creación de los objetos
my_vehicle=vehicle("ferrari","verde","ABC312")
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()