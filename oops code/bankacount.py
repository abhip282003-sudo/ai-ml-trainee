#Create a class BankAccount with deposit, withdraw, and balance check methods
class Bankaccount():
    def __init__(self,balance=0):
        self.balance=balance
    def deposite (self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient Balance!")
    def check_balance(self):
        print("ramaining is",self.balance)
b=Bankaccount(1000)
b.deposite(1000)
b.withdraw(500)
b.check_balance()