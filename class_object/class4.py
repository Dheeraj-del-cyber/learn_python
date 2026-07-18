class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def show_details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
    def discount(self):
        self.price-=50000
c1=Car("Toyota","Fortuner",4500000)
c2=Car("Hyundai","Creta",1800000)
c1.show_details()
print("\n")
c2.show_details()
c1.discount()
print("\n After discount:")
c1.show_details()