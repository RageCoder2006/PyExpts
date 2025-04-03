class BankAccount():
    account_holder = ""
    bal = 0

    def __init__(self, name, balance):
        self.account_holder = name
        self.bal = balance

    def deposit(self, amt):
        self.bal += amt
        print(f"{amt} Deposited Successfully!")

    def withdraw(self, amt):
        self.bal -= amt
        print(f"{amt} Withdrawn Successfully!")

    def check_balance(self):
        print(f"Balance: {self.bal}")


acc = BankAccount("XYZ", 10000)
BankAccount.deposit(acc, 5000)
BankAccount.withdraw(acc, 2000)
BankAccount.check_balance(acc)
