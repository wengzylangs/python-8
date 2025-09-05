"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class BankAccount: #class variable
	
   # declearing instances and methods
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			return f"{self.name}: account balance is {self.balance}"
		else:
			return "deposit amount must above 0"

	def withdraw(self, amount):
		if amount > self.balance:
			return "insufficient funds"
		elif amount <= 0:
			return "invalid amount"
		else:
			self.balance -= amount
			return f" {self.withdraw} withdrawal succesful!,current balance {self.balance}"
		
	def get_balance(self):
		return f"current balance {self.balance}"
		
account = BankAccount("Alice", 1000)
account.withdraw(200)
account.deposit(500)
print(account.get_balance()) 

