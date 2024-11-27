"""
Scenario: 
You are designing a banking application that processes withdrawals from an account.
Each account has a minimum balance that must be maintained. If a withdrawal would reduce the
balance below this minimum, it should raise a custom exception called InsufficientFundsError.

Question:
Create a custom exception InsufficientFundsError with an appropriate message. Define a class
BankAccount with attributes balance and min_balance. Write a method withdraw(amount) in
BankAccount that raises an InsufficientFundsError if the withdrawal amount would bring the
balance below the minimum allowed. Test the class and custom exception with a sample account.

"""


class InsufficientFundsError(Exception) :
    """Exception raised for errors in the withdrawal process due to insufficient funds."""
    def __init__(self, message) :
        self.message = message
        super().__init__(self.message)

class BankAccount :
    def __init__(self, balance, min_balance) :
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount) :
        if self.balance - amount < self.min_balance :
            raise InsufficientFundsError("Withdrawal would reduce balance below minimum allowed.")
        self.balance -= amount
        return self.balance

# Testing the BankAccount class and InsufficientFundsError

    # Create a bank account with a balance of 100 and a minimum balance of 20
account = BankAccount(balance=100, min_balance=20)

try:
    print("Initial balance:", account.balance)
    account.withdraw(30)  # This should succeed
    print("Balance after withdrawal of 30:", account.balance)
        
    account.withdraw(60)
except InsufficientFundsError as e :
    print("Error :", e.message)