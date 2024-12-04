class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.__balance = initial_balance  # Private attribute

    def get_balance(self):
        return self.__balance  # Public attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"New balance after deposit: {self.__balance}")
        else:
            print("Deposit amount should be greater than zero")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"New balance after withdrawal: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

account = BankAccount("Neha", 500)
account.deposit(400)
print(f"Current balance: {account.get_balance()}")
account.withdraw(200)
