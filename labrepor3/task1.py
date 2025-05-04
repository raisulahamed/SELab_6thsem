class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
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
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrawn ${amount}. Remaining balance: ${self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount("123456", "Jhon Doe", 1000)
print(account.get_account_number())
print(account.get_balance())
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
