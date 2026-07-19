class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def show(self):
        print(self.brand)
        print(self.price)
class electric(Car):
    def __init__(self,brand,price,battery):
        super().__init__(brand,price)
        self.battery=battery  
    def battery_info(self):
        print(self.battery)  
c1=Car("suzuki",100000)                    
e1=electric("tesla",1500000,50)
e1.show()
e1.battery_info()
c1.show()