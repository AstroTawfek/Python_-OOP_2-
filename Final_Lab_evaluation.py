from abc import ABC, abstractmethod

class InvalidInputError(Exception) :
    """When the input is Zero or negative"""
    def __init__(self, message):
        super().__init__(self, message)

class Student(ABC) :
    def __init__(self, student_id, name, tutionFee):
        self._student_id = student_id
        self._name = name
        self._tutionFee = tutionFee

    def get_student_id(self):
        return self._student_id
    
    def get_name(self):
        return self._name
    
    def get_tutionFee(self):
        return self._tutionFee
    
    @abstractmethod
    def calculate_fee(self):
        pass


class Undergraduate(Student):
    def __init__(self, student_id, name, tutionFee, credit_hour):
        super().__init__(student_id, name, tutionFee)
        self.__credit_hour = credit_hour

    def show_studentId(self):
        return self.get_student_id()
    
    def show_name(self):
        return self.get_name()

    def calculate_fee(self):
        if self.__credit_hour < 1 :
            raise InvalidInputError("Error : Credit hour should be greater than 0")
        else :
            return self.__credit_hour*super().get_tutionFee()
        
    def totalFee(self):
        if self.__credit_hour < 1 :
            raise InvalidInputError("Error : Credit hour should be greater than 0")
        
        else :
            return 150*super().get_tutionFee()
        

class Graduate(Student) :
    def __init__(self, student_id, name, tutionFee, research_hour):
        super().__init__(student_id, name, tutionFee)
        self.__research_hour = research_hour

    def show_studentId(self):
        return self.get_student_id()
    
    def show_name(self):
        return self.get_name()

    def calculate_fee(self):
        if self.__research_hour < 1 :
            raise InvalidInputError("Error : Credit hour should be greater than 0")
        else :
            return self.__research_hour*super().get_tutionFee()
        
    def totalFee(self):
        if self.__research_hour < 1 :
            raise InvalidInputError("Error : Credit hour should be greater than 0")
        
        else :
            return 90*super().get_tutionFee()


un_gra = Undergraduate(1827, "Tawfek", 6500, 19)
gra = Graduate(18271, "Jerry", 6500, 10)

try :
    print("Undergraduate Student")
    print("Student Nmae : ", un_gra.show_name())
    print("Student Id : ", un_gra.show_studentId())
    print("Tution Fee of the running semester : ", un_gra.calculate_fee())
    print("Total Fee needed for graduation : ", un_gra.totalFee())
    print()

    print("Graduate Student")
    print("Student Nmae : ", gra.show_name())
    print("Student Id : ", gra.show_studentId())
    print("Tution Fee of the running : ", gra.calculate_fee())
    print("Total Fee needed for complete research : ", gra.totalFee())
    print()

except InvalidInputError as e :
    print(e)

except :
    print("An error occurred : There is something wrong")