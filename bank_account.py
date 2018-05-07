class BankAccount:
	def __init__(self, first_name, last_name, middle_name, account_type):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name
		self.account_type = account_type
		self.balance = 0
		self.status = "Closed"
		print(f"{self.first_name}'s {self.account_type} account status: {self.status}")
		print("Your account has been created, but you must deposit at least $100 to open and use it")

	def open_account(self):
		if self.balance >= 100 :
			self.status = "Open"
			print(f"Your account status is: {self.status}")
		else:
			print("Insufficient funds")
			print("Please deposit at least $100 to begin using account")
			print(f"Current balance : ${self.balance}")

	def account_balance(self):
		return("Your current balance is $" + str(float(self.balance)))

	def deposit(self, amount_to_deposit):
		self.balance += amount_to_deposit
		print(f"You just deposited ${amount_to_deposit}, {self.account_balance()}")

	def withdraw(self, amount_to_withdraw):
		self.balance -= amount_to_withdraw
		print(f"You have withdrawn: ${amount_to_withdraw}")
		print(f"Current balance: ${self.balance}")
		if self.balance <= 0:
			self.balance -= 35
			print("You account has been overdrawn")
			print("You have been charged a $35 overdraw fee")
			print(f"Current balance: ${self.balance}")

	def transfer_funds(self, amount_to_transfer, account_to_transfer_to):
		self.balance -= amount_to_transfer
		account_to_transfer_to.balance += amount_to_transfer
		if self.balance <= 0:
			self.balance -= 35
			print("You account has been overdrawn")
			print("You have been charged a $35 overdraw fee")


harold = BankAccount("Harold", "Werner", "Charles", "savings")
harold.deposit(200)
harold.open_account()
print(harold.account_balance())

harold2 = BankAccount("Harold", "Werner", "Charles", "checking")
harold.transfer_funds(100, harold2)
harold2.open_account()
harold2.withdraw(150)