class Cuenta:
    def __init__(self,numero,saldo):
        self.numero=numero
        self.__saldo = saldo
        
    def depositar(self,cantidad):
        if cantidad >0:
            self.__saldo+= cantidad
    
    def retirar(self,cantidad):
        if cantidad >0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Error: Saldo insuficiente o cantidad inválida")
            
    def imprimirsaldo(self):
        print(f"el saldo de la cuenta {self.numero} es: {self.__saldo}")


#Creación de objetos
cuenta1=Cuenta(1111,1000)
cuenta1.depositar(999)
print(cuenta1.imprimirsaldo()) 
