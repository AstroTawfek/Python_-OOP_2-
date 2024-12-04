class InvalidVoterException(Exception) :
    'Your age is not valid'
    def __init__(self, m) :
        self.message = m
        super().__init__(m)
    pass

class Voter :
    def __init__(self) :
        print("your system is opened")
    def check(self):
        try :
            age = int(input("Enter your age : "))
            if age < 18 :
                raise InvalidVoterException("Your age is below 18")
        
        except InvalidVoterException as e :
            print("Error : ", e)
            
        except :
            print("Something error occure in try block") 
            
        else :
            print("You are eligible as a voter")
            
v = Voter()
v.check()