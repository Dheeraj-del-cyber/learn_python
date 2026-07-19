class Account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def show_details(self):
        print("Account holder:",self.account_holder)
        print("Balance:",self.balance)
class SavingsAccount(Account):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        self.balance+=self.balance*self.interest_rate/100
    def account_type(self):
        print("Savings Account")
s1=SavingsAccount("Dheeraj",10000,5)
s1.show_details()
print()
print("Account type:")
s1.account_type()
print()
print("After Interest:") 
s1.add_interest()
s1.show_details()                      