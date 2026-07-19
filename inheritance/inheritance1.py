class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def show(self):
        print(self.brand)
        print(self.price)
class ElectricCar(Car):
    def charge(self):
        print("charging....")
e1=ElectricCar("TATA",1000000)
e1.show()
e1.charge()