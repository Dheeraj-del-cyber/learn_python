class BankBalance:
    def __init__(self,balance):
        self.__balance=balance 
    def show(self):
        print(self.__balance)    
b1=BankBalance(10000)
b1.show()