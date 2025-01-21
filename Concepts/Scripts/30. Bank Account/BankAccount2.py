class Account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} Rs. are Deposited to {self.name}'s Account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough balance!")
        else:
            self.balance-=amount
            print(f"{amount} Rs. are Withdrawed from {self.name}'s Account")
    def __str__(self):
        return f"Account Holder Name: {self.name}\nBalance: {self.balance}\n"
account1=Account("Vaibhav",5000)
account2=Account("Ayush",5500)
print(account1)
print(account2)
account1.deposit(300)
account2.deposit(250)
print()
print(account1)
print(account2)
account1.withdraw(6000)
account2.withdraw(400)
print()
print(account1)
print(account2)

"""
O/p: Account Holder Name: Vaibhav
     Balance: 5000
     
     Account Holder Name: Ayush
     Balance: 5500
     
     300 Rs. are Deposited to Vaibhav's Account
     250 Rs. are Deposited to Ayush's Account
     
     Account Holder Name: Vaibhav
     Balance: 5300
     
     Account Holder Name: Ayush
     Balance: 5750
     
     Not enough balance!
     400 Rs. are Withdrawed from Ayush's Account
     
     Account Holder Name: Vaibhav
     Balance: 5300
     
     Account Holder Name: Ayush
     Balance: 5350
     
"""