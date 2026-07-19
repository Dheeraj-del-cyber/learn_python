class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def show_details(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
class EBook(Book):
    def __init__(self, title, author, price,file_size):
        super().__init__(title, author, price)            
        self.file_size=file_size
    def download(self):
        print("Downloading",self.title,"...")
    def discount(self):
        self.price-=self.price*10/100
    def show_file_size(self):
        print("File Size:",self.file_size)   
    def increase_price(self):
        self.price+=100             
e1=EBook("Python Basics","John",500,25)
e2=EBook("java","dheeraj",450,35)
e1.show_details()
print()
e1.show_file_size()       
e1.download()
print()
print("After Discount:")
e1.discount()
e1.show_details()
print()
print("After increasing price:")
e1.increase_price()
e1.show_details()
print()
e2.show_details()
print()
e2.show_file_size()       
e2.download()
print()
print("After Discount:")
e2.discount()
e2.show_details()
print()
print("After increasing price:")
e2.increase_price()
e2.show_details()