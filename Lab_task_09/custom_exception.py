class InsufficientBalance(Exception) :
   
    pass

class BankAccount :
    def __init__(self, balance) :
        self.balance = balance
        
    def withdraw(self, x) :
        if x > self.balance :
            raise InsufficientBalance
        else :
            print("Withdrawal ammount :",)
        
    
try :
    b = BankAccount(10000)
    b.withdraw(11000)

except InsufficientBalance as e :
    print("you have not enough balance")