class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} Rs. are Deposited to {self.name}'s Account")
    def withdraw(self,amount):
        self.balance-=amount
        print(f"{amount} Rs. are Withdrawed from {self.name}'s Account")
    def display(self):
        print(f"{self.name}'s Account Balance: {self.balance}")
account1=Account("Vaibhav",5000)
account2=Account("Ayush",5500)
account1.display()
account2.display()
print()
account1.deposit(300)
account2.deposit(250)
print()
account1.display()
account2.display()
print()
account1.withdraw(500)
account2.withdraw(400)
print()
account1.display()
account2.display()

"""
O/p: Vaibhav's Account Balance: 5000
     Ayush's Account Balance: 5500
     
     300 Rs. are Deposited to Vaibhav's Account
     250 Rs. are Deposited to Ayush's Account
     
     Vaibhav's Account Balance: 5300
     Ayush's Account Balance: 5750
     
     500 Rs. are Withdrawed from Vaibhav's Account
     400 Rs. are Withdrawed from Ayush's Account
     
     Vaibhav's Account Balance: 4800
     Ayush's Account Balance: 5350
"""