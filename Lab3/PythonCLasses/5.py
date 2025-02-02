class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
        else:
            print("Number should be positive!")
    def withdraw(self, amount1):
        if(self.balance > amount1):
            self.balance -= amount1
        elif(amount1 < 0):
            print("Number should be positive!")
        else:
            print("Not enough money!")
    def __str__(self):
        return f"Owner: {self.owner}. Balance: {self.balance}"

acc1 = BankAccount("Arystanbek", 47500)
print(acc1)

acc1.deposit(15000)
acc1.withdraw(90000)
acc1.withdraw(20000)
acc1.withdraw(-20000)
acc1.deposit(-1500)
print(acc1)
        
      