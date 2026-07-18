class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def boy(self):
        print(self.name,"is a boy")
    def girl(self):
        print(self.name,"is a girl")
s1=student("dheeraj",25)
s2=student("dhanush",18)
s3=student("baggu",11)
s4=student("kathik",38)
s5=student("madura",2)
s6=student("ananya",1)        

s1.boy()
s2.boy()
s3.boy()
s4.boy()
s5.girl()
s6.girl()