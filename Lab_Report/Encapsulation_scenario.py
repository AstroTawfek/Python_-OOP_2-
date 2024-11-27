"""
Scenario: Imagine you are developing a software application for a bank that includes a
BankAccount class. The class should manage customers' account balances, allowing deposits,
withdrawals, and balance checks. For security and integrity, it’s important to restrict direct access
to the account balance, ensuring only authorized methods can modify or view it.

Question:
1. Create a BankAccount class that includes the following:
○ A private variable for the account balance.
○ Public methods for:
■ Deposit: Adds a specified amount to the account balance.
■ Withdraw: Subtracts a specified amount from the account balance,
ensuring the balance does not go below zero.
■ Check Balance: Returns the current balance without allowing direct
access to the balance variable.

2. Perform the following actions:
○ Deposit money into an account.
○ Attempt a withdrawal larger than the current balance to ensure the account does
not go negative.
○ Check the balance.

"""


class BankAccount:
    def __init__(self):
        # Private variable for account balance
        self.__balance = 0.0

    def deposit(self, amount):
        """Adds a specified amount to the account balance."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited : ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts a specified amount from the account balance,
        ensuring the balance does not go below zero."""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew : ${amount:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Returns the current balance without allowing direct access to the balance variable."""
        return f"Current balance: ${self.__balance:.2f}"

# Example usage:
account = BankAccount()

# Deposit money into the account
account.deposit(100.00)

# Attempt a withdrawal larger than the current balance
account.withdraw(150.00)

# Check the balance
print(account.check_balance())