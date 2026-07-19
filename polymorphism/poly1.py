class Vechile:
    def start(self):
        print("vechile is starting")
class car(Vechile):
    def start(self):
        print("car start with a key")
class bike(Vechile):                
    def start(self):
        print("bike starts with a self-start button")
c1=car()
b1=bike()
c1.start()
b1.start()        