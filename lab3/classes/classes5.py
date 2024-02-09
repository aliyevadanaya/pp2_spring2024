class kaspi:
    def __init__(a, o, b):
        a.owner = o
        a.balance = b
    def deposit(a, money):
        a.balance+=money
    def withdraw(a, tenge):
        if a.balance>=tenge:
            a.balance-=tenge
        else:
            print("you do not have enough money")
    def __str__(self):
        return f"name: {self.owner}\nbalance: {self.balance}"
    
    
