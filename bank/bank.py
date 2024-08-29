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


class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating
