class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit: {amount}. Balance : {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return f"Withdrew: {amount}. Balance : {self.balance}"


daniel = BankAccount("Dan", 100)
tiffany = BankAccount("Tiffany", 200)

daniel.deposit(200)

print(daniel)
