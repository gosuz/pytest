# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     def balance_check(self):
#         return f"Balance: {self.balance}"

#     def deposit(self, amount):
#         self.balance += amount
#         self.transaction_history.append(f"Deposit: {amount}. Balance : {self.balance}")
#         return f"Deposit: {amount}. Balance : {self.balance}"

#     def withdraw(self, amount):
#         if amount > self.balance:
#             self.transaction_history.append(f"Insufficient Funds. Failed to withdraw: {amount} from the balance of {self.balance}")
#             return "Insufficient Funds"
#         else:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew: {amount}. Balance : {self.balance}")
#             return f"Withdrew: {amount}. Balance : {self.balance}"

class BankAccount:
    # MANDATORY
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Not Mandatory....but very useful.
    def __str__(self):
        return f"Account Name:{self.name} Account Balance:{self.balance}"


    def balance_check(self):
        return f"{self.name}'s current balance:{self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"desposit:{amount}. Current Balance:{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "not enough funds..."
        else:
            self.balance -= amount
            return f"withdrew:{amount}. Current Balance:{self.balance}"


daniel = BankAccount('daniel', 3000)

print(daniel)
