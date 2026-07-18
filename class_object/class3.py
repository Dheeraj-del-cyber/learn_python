class Laptop:
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram
    def upgrade(self):
        self.ram+=8     
    def details(self):
        print("Brand:",self.brand)
        print("RAM:",self.ram,"GB")
l1=Laptop("HP",16)
l2=Laptop("ASUS",8)

l1.upgrade()
l1.details()
l2.upgrade()
l2.details()