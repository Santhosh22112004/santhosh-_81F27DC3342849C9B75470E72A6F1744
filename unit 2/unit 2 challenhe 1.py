class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient balance. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__balance}")

# Creating an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000.0)

# Testing deposit and
