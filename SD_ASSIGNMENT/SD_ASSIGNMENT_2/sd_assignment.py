class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance

    def set_account_holder_name(self, name):
        self.__account_holder_name = name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

account = BankAccount("C223085", "Amjad Hossain Evan", 1000)

print("Initial Balance:", account.get_balance())
account.deposit(500)
print("Balance after deposit:", account.get_balance())
account.withdraw(300)
print("Balance after withdrawal:", account.get_balance())
account.withdraw(1500)
print("Final Balance:", account.get_balance())